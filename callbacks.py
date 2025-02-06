from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

import database


def register_callbacks(app):
    @app.callback(
        Output(component_id="database-table", component_property="data", allow_duplicate=True),
        Input(component_id="database-table", component_property="data"),
        prevent_initial_call="initial_call_duplicate"
    )
    def refresh_database_table(database_table):
        database_table = database.get_table_as_df()
        if database_table.empty:
            database_table = database.get_empty_database_df(columns=20, rows=100, header_text="Empty Data", cell_text="asdfasdfasdfasdfasdfasdfasdfasdf")
        print(database_table)
        return database_table.to_dict("records")
    
    pass