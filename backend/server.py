from flask import Flask, render_template, request
from backend.config import Config
import sqlite3
import os
import random

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
    inventory_name = request.args.get('inventory_name') or "banana"
    inventory_name = inventory_name[0].upper() + inventory_name[1:]
    prediction_data = []
    for _ in range(7):
        prediction_ran_num = random.randint(18, 28)
        prediction_data.append(prediction_ran_num)

    inventory = []
    for _ in range(7):
        inventory_ran_num = random.randint(15, 22)
        inventory.append(inventory_ran_num)

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

