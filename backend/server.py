from flask import Flask
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/collect')
def collect_api():
    """
    collector_interface = CollectorInterface()
    collector_interface.setType("facebook")
    collector_interface.collect()
    """
    return "Hello, Collect!"

@app.route('/train')
def train_api():
    """
    training_interface = TrainingInterface()
    training_interface.train()
    """
    return "Hello, Train!"

@app.route('/getPrediction')
def prediction_query():
    """
    prediction_interface = PreidctionInterface()
    prediction_interface.returnModel("food")
    """
    return "Hello prediction"


