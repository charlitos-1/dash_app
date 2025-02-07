from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import database


def serve_column_defs(columns):
    column_sizes = {
        "id": {"width": 25, "minWidth": 100, "maxWidth": 500},
        "Input1": {"width": 100, "minWidth": 100, "maxWidth": 500},
        "Input2": {"width": 100, "minWidth": 100, "maxWidth": 500},
        "Input3": {"width": 100, "minWidth": 100, "maxWidth": 500},
        "Input4": {"width": 100, "minWidth": 100, "maxWidth": 500},
        "Input5": {"width": 100, "minWidth": 100, "maxWidth": 500},
        "Input6": {"width": 100, "minWidth": 100, "maxWidth": 500},
        "Status": {"width": 100, "minWidth": 100, "maxWidth": 500},
    }
    
    column_defs = [
        {
            "field": column, 
            "headerTooltip": column, 
            "tooltipField": column,
            "headerCheckboxSelection": True if idx == 0 else False,
            "checkboxSelection": True if idx == 0 else False,
            "headerCheckboxSelectionFilteredOnly": True,
            "width": column_sizes.get(column, {}).get("width", "auto"),
            "minWidth": column_sizes.get(column, {}).get("minWidth", 100),
            "maxWidth": column_sizes.get(column, {}).get("maxWidth", 500),
            "filter": True,
            "sortable": False,
        }
        for idx, column in enumerate(columns)
    ]
    return column_defs


def serve_dash_grid_options():
    grid_options = {
        "enableSorting": False,
        "enableColResize": True,
        "animateRows": True,
        "pagination": True,
        "paginationPageSize": 50,
        "paginationPageSizeSelector": True,
        "tooltipShowDelay": 100,
        "rowSelection": "multiple",
        "suppressRowClickSelection": True,
    }
    return grid_options


def serve_layout():
    layout = [
        dbc.Container([
            dbc.Row([
                html.H1("Manager")
            ]),
            dbc.Col([
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
        ]),
        dbc.Container([
            dbc.Row([
                html.H2("Database"),
            ]),
            dbc.Row([
                dag.AgGrid(id="database-table", rowData=None, columnDefs=None, dashGridOptions=serve_dash_grid_options()),
            ]),
            dcc.Store(id="database-store", data=[], storage_type="session"),
            dbc.Row([
                html.Div(id="dummy-div", style={"display":"none"}), # Dummy div to create callbacks with no outputs
                dbc.Button("Function 1", id="function-1-button", color="primary", n_clicks=0),
                dbc.Button("Function 2", id="function-2-button", color="primary", n_clicks=0),
                dbc.Button("Function 3", id="function-3-button", color="primary", n_clicks=0),
                dbc.DropdownMenu(
                    label="Function 4",
                    children=[
                        dbc.DropdownMenuItem("Function 4.1", id="function-4-1-button", n_clicks=0),
                        dbc.DropdownMenuItem("Function 4.2", id="function-4-2-button", n_clicks=0),
                        dbc.DropdownMenuItem("Function 4.3", id="function-4-3-button", n_clicks=0),
                    ],
                ),
            ])
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
