import sqlite3
import pandas as pd
import os

taperunner_db = "taperunner.db"
taperunner_table_name = "taperunner"
taperunner_columns = [
    "Input1",
    "Input2",
    "Input3",
    "Input4",
    "Input5",
    "Input6",
]


def get_empty_database_df(rows=1, columns=1, header_text="Empty", cell_text="No data"):
    return pd.DataFrame({f"{header_text} {i}": [cell_text]*rows for i in range(columns)})


def get_db_connection(db_file=None):
    """Returns a connection to the SQLite database."""
    if db_file is None:
        db_file = taperunner_db

    return sqlite3.connect(db_file)


def initialize_database(db_file=None, table_name=None, columns=None):
    """Initializes the database with a default table."""
    if db_file is None:
        db_file = taperunner_db

    if table_name is None:
        table_name = taperunner_table_name

    if columns is None:
        columns = [column for column in taperunner_columns]

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    columns_definition = ", ".join(columns)
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {columns_definition}
        )
        """
    )
    conn.commit()
    conn.close()
    print(
        f"Database '{db_file}' initialized with table '{table_name}' and columns '{columns}'."
    )


def add_row(row_data, db_file=None, table_name=None):
    """Adds a single row to the specified table."""
    if db_file is None:
        db_file = taperunner_db

    if table_name is None:
        table_name = taperunner_table_name

    conn = get_db_connection(db_file)
    cursor = conn.cursor()
    columns = ", ".join(row_data.keys())
    placeholders = ", ".join(["?"] * len(row_data))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, tuple(row_data.values()))
    conn.commit()
    conn.close()


def get_table_as_df(db_file=None, table_name=None):
    """Returns the specified table as a pandas DataFrame."""
    if db_file is None:
        db_file = taperunner_db

    if table_name is None:
        table_name = taperunner_table_name

    conn = get_db_connection(db_file)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df