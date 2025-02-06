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
            database_table = database.get_empty_database_df(columns=20, rows=100, header_text="Empty Data", cell_text="asdfasdf")
        print(database_table)
        return database_table.to_dict("records")

    @app.callback(
        Output(component_id="new-entries-table", component_property="data", allow_duplicate=True),
        Input(component_id="new-entries-table", component_property="data"),
        prevent_initial_call="initial_call_duplicate"
    )
    def refresh_database_table(new_entries_table):
        new_entries_table = database.get_table_as_df()
        if new_entries_table.empty:
            new_entries_table = database.get_empty_database_df(columns=20, rows=100, header_text="New Data", cell_text="jkl;jkl;")
        print(new_entries_table)
        return new_entries_table.to_dict("records")

    @app.callback(
        Output(component_id="input-1", component_property="value", allow_duplicate=True),
        Output(component_id="input-2", component_property="value", allow_duplicate=True),
        Output(component_id="input-3", component_property="value", allow_duplicate=True),
        Output(component_id="input-4", component_property="value", allow_duplicate=True),
        Output(component_id="input-5", component_property="value", allow_duplicate=True),
        Output(component_id="input-6", component_property="value", allow_duplicate=True),
        Input("clear-inputs", "n_clicks"),
        prevent_initial_call=True,
    )
    def clear_inputs(n_clicks):
        return "", "", "", "", "", ""

    pass
