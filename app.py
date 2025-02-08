from dash import Dash

import database, layout, callbacks

app = Dash(__name__)
app.layout = layout.serve_layout()
callbacks.register_callbacks(app)


def main():
    database.initialize_database()
    app.run_server(debug=False, port=5000)


if __name__ == "__main__":
    main()