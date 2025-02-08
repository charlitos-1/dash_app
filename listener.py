import flask
import asyncio

import database

app = flask.Flask(__name__)


def main():
    app.run(debug=False, port=5050)
    
    
if __name__ == "__main__":
    main()