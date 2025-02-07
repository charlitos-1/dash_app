from dash import html, dcc, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import pandas as pd

import database
import layout

def register_callbacks(app):
    @app.callback(
        Output(component_id="database-table", component_property="rowData", allow_duplicate=True),
        Output(component_id="database-table", component_property="columnDefs", allow_duplicate=True),
        Output(component_id="database-store", component_property="data", allow_duplicate=True),
        Input(component_id="database-store", component_property="data"),
        prevent_initial_call="initial_call_duplicate"
    )
    def refresh_database_table(database_store):
        database_store = database.get_table_as_df().to_dict("records")
        row_data = [_ for _ in database_store]
        column_defs = layout.serve_column_defs(database.get_columns())
        
        return row_data, column_defs, database_store

    @app.callback(
        Output(component_id="new-entries-table", component_property="rowData", allow_duplicate=True),
        Output(component_id="new-entries-table", component_property="columnDefs", allow_duplicate=True),
        Output(component_id="new-entries-store", component_property="data", allow_duplicate=True),
        Input(component_id="new-entries-store", component_property="data"),
        prevent_initial_call="initial_call_duplicate"
    )
    def refresh_new_entries_table(new_entries_store):
        row_data = [_ for _ in new_entries_store]
        column_defs = layout.serve_column_defs(database.get_columns()) 
        return row_data, column_defs, new_entries_store

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
    
    @app.callback(
        Output("new-entries-store", "data", allow_duplicate=True),
        Input("add-to-db", "n_clicks"),
        State("input-1", "value"),
        State("input-2", "value"),
        State("input-3", "value"),
        State("input-4", "value"),
        State("input-5", "value"),
        State("input-6", "value"),
        State("new-entries-store", "data"),
        prevent_initial_call=True
    )
    def add_to_new_entries(n_clicks, input1, input2, input3, input4, input5, input6, new_entries_store):
        if not all([input1, input2, input3, input4, input5, input6]):
            return no_update

        new_entry = {
            "id": None,
            "Input1": input1,
            "Input2": input2,
            "Input3": input3,
            "Input4": input4,
            "Input5": input5,
            "Input6": input6,
        }
        
        if new_entries_store is None:
            new_entries_store = []

        new_entries_store.append(new_entry)
        return new_entries_store
    
    @app.callback(
        Output("database-store", "data", allow_duplicate=True),
        Output("new-entries-store", "data", allow_duplicate=True),
        Input("commit-changes", "n_clicks"),
        State("new-entries-store", "data"),
        prevent_initial_call=True
    )
    def commit_changes(n_clicks, new_entries_store):
        if not new_entries_store:
            return no_update

        for entry in new_entries_store:
            database.add_row(entry)
        
        database_store = []
        new_entries_store = []

        return database_store, new_entries_store
    
    @app.callback(
        Output("new-entries-store", "data"),
        Input("clear-changes", "n_clicks"),
        prevent_initial_call=True
    )
    def clear_changes(n_clicks):
        return []

    pass
