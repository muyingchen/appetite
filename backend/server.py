from flask import Flask, render_template, request
from backend.config import Config
import sqlite3
import os
import random
from backend.src.interface.collector_interface import CollectorInterface
from backend.src.train.trainer import Trainer
from sklearn import linear_model
import pickle
import datetime

app = Flask(__name__)
app.config.from_object(Config)

frontend_dir = os.path.join(os.path.dirname(app.instance_path), 'frontend')
static_dir = os.path.join(frontend_dir, 'static')
template_dir = os.path.join(frontend_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)
app.static_folder = os.path.join(frontend_dir, 'static')

data_dir = os.path.join(os.path.dirname(app.instance_path), 'backend', 'data')
csv_path = "{}/data.csv".format(data_dir)
weather_path = "{}/weather.csv".format(data_dir)
gt_path = "{}/google_trend_five_years.csv".format(data_dir)
pickle_path = "{}/model.pickle".format(data_dir)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/demo')
def form():
    return render_template("form.html")

@app.route('/getprediction')
def dashboard():
    inventory_name = request.args.get('inventory_name') or "banana"
    inventory_name = inventory_name[0].upper() + inventory_name[1:]
    random_inventory_number = random.randint(2, 6)
    with open(pickle_path, 'rb') as pk:
        trainer = pickle.load(pk)

    #datetime
    #prediction = trainer.predict({'DATE': [], 'TAVG': [], 'TMAX': [], 'TMIN': [], 'STRAWBERRIES': []})

    prediction_data = []
    for _ in range(7):
        prediction_ran_num = random.randint(18, 28)
        prediction_data.append(prediction_ran_num)

    inventory = []
    for _ in range(random_inventory_number):
        inventory_ran_num = random.randint(15, 22)
        inventory.append(inventory_ran_num)

    return render_template("dashboard.html",
                           prediction_data=prediction_data,
                           inventory=inventory,
                           inventory_name=inventory_name,
                           random_inventory_number=random_inventory_number
                           )

@app.route('/collect')
def collect_api():
    collector = CollectorInterface(csv_path)
    collector.build_csv()
    return "Hello, Collect!"

@app.route('/train')
def train_api():
    """
    training_interface = TrainingInterface()
    training_interface.train()
    """
    trainer = Trainer(model=linear_model.Ridge, label='TRANSACTION')

    trainer.feed_csv(weather_path, columns=['TAVG', 'DATE', 'TMIN', 'TMAX'])
    trainer.feed_csv(gt_path, columns=['STRAWBERRIES', 'DATE', 'TRANSACTION'])

    print('Training in progress')
    trainer.train()

    with open(pickle_path, 'wb') as pk:
        pickle.dump(trainer, pk)
    return "Training is succesfully done."

@app.route('/getPrediction')
def prediction_query():
    """
    prediction_interface = PreidctionInterface()
    prediction_interface.returnModel("food")
    """
    trainer = pickle.load(pickle_path)



