from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import database


def serve_column_defs(columns):
    column_defs = [{"field": column, "headerTooltip": column, "tooltipField": column} for column in columns]
    return column_defs


def serve_dash_grid_options():
    grid_options = {
        "enableSorting": False,
        "enableColResize": True,
        "animateRows": True,
        "pagination": True,
        "paginationPageSize": 50,
        "paginationPageSizeSelector": False,
        "tooltipShowDelay": 100,
    }
    return grid_options


def serve_layout():
    layout = [
        dbc.Container([
            dbc.Row([
                html.H1("Manager")
            ]),
            dbc.Row([
                html.H2("Inputs")
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Row(html.Label("Input 1")),
                    dbc.Row(dcc.Input(id="input-1", type="text", value="", placeholder="Enter input 1", debounce=True)),
                    dbc.Row(html.Label("Input 2")),
                    dbc.Row(dcc.Input(id="input-2", type="text", value="", placeholder="Enter input 2", debounce=True)),
                ]),
                dbc.Col([
                    dbc.Row(html.Label("Input 3")),
                    dbc.Row(dcc.Input(id="input-3", type="text", value="", placeholder="Enter input 3", debounce=True)),
                    dbc.Row(html.Label("Input 4")),
                    dbc.Row(dcc.Input(id="input-4", type="text", value="", placeholder="Enter input 4", debounce=True)),
                ]),
                dbc.Col([
                    dbc.Row(html.Label("Input 5")),
                    dbc.Row(dcc.Input(id="input-5", type="text", value="", placeholder="Enter input 5", debounce=True)),
                    dbc.Row(html.Label("Input 6")),
                    dbc.Row(dcc.Input(id="input-6", type="text", value="", placeholder="Enter input 6", debounce=True)),
                ]),
                dcc.Store(id="clear-inputs-flag", data=0, storage_type="session"),
            ]),
            dbc.Row([
                dbc.Button("Add to Database", id="add-to-db", color="primary", n_clicks=0),
                dbc.Button("Clear Inputs", id="clear-inputs-button", color="secondary", n_clicks=0),
            ]),
        ]),
        dbc.Container([
            dbc.Row([
                html.H2("Database"),
            ]),
            dbc.Row([
                dag.AgGrid(id="database-table", rowData=None, columnDefs=None, dashGridOptions=serve_dash_grid_options()),
            ]),
            dcc.Store(id="database-store", data=[], storage_type="session"),
        ]),
        dbc.Container([
            dbc.Row([
                html.H2("New Entries"),
            ]),
            dbc.Row([
                dag.AgGrid(id="new-entries-table", rowData=None, columnDefs=None, dashGridOptions=serve_dash_grid_options()),
            ]),
            dcc.Store(id="new-entries-store", data=[], storage_type="session"),
            dbc.Row([
                dbc.Button("Commit Changes", id="commit-changes", color="primary", n_clicks=0),
                dbc.Button("Clear Changes", id="clear-changes-button", color="secondary", n_clicks=0),
            ]),
        ]),
    ]
    return layout
