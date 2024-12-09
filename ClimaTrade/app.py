from flask import Flask
from dash import Dash
from app.routes import create_layout

server = Flask(__name__)
app = Dash(server=server, suppress_callback_exceptions=True)
app.title = "NYC Weather Prediction Dashboard"
app.layout = create_layout()

if __name__ == "__main__":
    app.run_server(debug=True)
