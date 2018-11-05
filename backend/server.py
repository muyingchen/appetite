from flask import Flask
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/collect')
def collect_api():
    return "Hello, Collect!"

@app.route('/train')
def train_api():
    return "Hello, Train!"

@app.route('/getPrediction')
def prediction_query():
    return "Hello prediction"

