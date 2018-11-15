from flask import Flask, render_template, request
from backend.config import Config
import sqlite3
import os

app = Flask(__name__)
app.config.from_object(Config)

frontend_dir = os.path.join(os.path.dirname(app.instance_path), 'frontend')
static_dir = os.path.join(frontend_dir, 'static')
template_dir = os.path.join(frontend_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)
app.static_folder = os.path.join(frontend_dir, 'static')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/getprediction')
def dashboard():
    inventory_name = request.args.get('inventory_name')
    prediction_data = [22, 20, 12, 13, 15, 14, 17]
    inventory = [20, 19, 12, 14, 13, 12, 15]
    return render_template("dashboard.html",
                           prediction_data=prediction_data,
                           inventory=inventory,
                           inventory_name=inventory_name
                           )

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


