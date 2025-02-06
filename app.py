from dash import Dash

import database, layout, callbacks

app = Dash(__name__)
app.layout = layout.serve_layout()
callbacks.register_callbacks(app)


def main():
    app.run_server(debug=True, port=5000)


if __name__ == '__main__':
    main()