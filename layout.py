from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

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
            ]),
            dbc.Row([
                dbc.Button("Add to Database", id="add-to-db", color="primary", n_clicks=0),
                dbc.Button("Clear Inputs", id="clear-inputs", color="secondary", n_clicks=0),
            ]),
        ]),
        dbc.Container([
            dbc.Row([
                html.H2("Database"),
            ]),
            dbc.Row([
                dash_table.DataTable(id="database-table", data=None),
            ]),
        ]),
        dbc.Container([
            dbc.Row([
                html.H2("New Entries"),
            ]),
            dbc.Row([
                dash_table.DataTable(id="new-entries-table", data=None),
            ]),
        ]),
    ]
    return layout
