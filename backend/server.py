from flask import Flask, render_template, request
from backend.config import Config, dir_path
from backend.src.ml_model.model_utils import get_model, save_model, is_valid_model

from backend.src.ml_model.inventory_model import InventoryModel
from sklearn import linear_model

import os
import random

# initialize app
app = Flask(__name__)

# find directory locations
frontend_dir = dir_path['frontend']
static_dir = os.path.join(frontend_dir, 'static')
template_dir = os.path.join(frontend_dir, 'templates')

# setup app
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(Config)
app.static_folder = os.path.join(frontend_dir, 'static')

# setup data path
data_dir = dir_path['data']
csv_path = "{}/data.csv".format(data_dir)
weather_path = "{}/weather.csv".format(data_dir)
gt_path = "{}/google_trend_five_years.csv".format(data_dir)

# model deployment
models = {

}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo')
def form():
    return render_template("form.html")

@app.route('/getprediction')
def dashboard():
    #TODO It should use our prediction api
    inventory_name = request.args.get('inventory_name') or "strawberry"
    inventory_name = inventory_name[0].upper() + inventory_name[1:]
    random_inventory_number = random.randint(2, 4)

    inventory_type = inventory_name.lower()
    model = None

    if is_valid_model(inventory_type):
        model = get_model(inventory_type)

    #datetime
    #prediction = trainer.predict({'DATE': [], 'TAVG': [], 'TMAX': [], 'TMIN': [], 'STRAWBERRIES': []})

    prediction_data = []
    for _ in range(7):
        prediction_ran_num = random.randint(18, 24)
        prediction_data.append(prediction_ran_num)

    inventory = []
    for _ in range(random_inventory_number):
        inventory_ran_num = random.randint(18, 22)
        inventory.append(inventory_ran_num)

    return render_template("dashboard.html",
                               prediction_data=prediction_data,
                               inventory=inventory,
                               inventory_name=inventory_name,
                               random_inventory_number=random_inventory_number
                           )


"""
Model REST API. 
    Models are supposed to be offline process, but since our goal is the quick prototyping, 
        we added all of them in the main web server. It should eventually be migrated to a different service application. 
"""
@app.route('/predict')
def predict_api():
    """
    Predict the inventory demand and return as a json data

    :param inventory_type

    :return: demand of <inventory_type>
    """
    pass

@app.route('/collect')
def collect_api():
    """
    Collect the data
    :return: json data that specifies the collection has been successfully done
    """
    return "Hello, Collect!"


@app.route('/deploy_model')
def deploy_model_api():
    """
    Actual machine learning model should be trained and deployed in offline.
        For our application, we are just adding models to the list and saying they are "deployed"
        for the quick prototyping.
    :return: json data that specifies the deployment has been successfully done
    """
    inventory_name = request.args.get('inventory_name') or "strawberry"
    inventory_name = inventory_name.lower()

    model = None
    if is_valid_model(inventory_name):
        model = get_model(inventory_name)

    models[inventory_name] = model
    return "Deployment of {} model is successfully done.".format(inventory_name)


@app.route('/train')
def train_api():
    """

    :return: json data that specifies the training has been successfully done
    """
    inventory_model = InventoryModel(model=linear_model.Ridge, label='TRANSACTION')

    inventory_model.feed_csv(weather_path, columns=['TAVG', 'DATE', 'TMIN', 'TMAX'])
    inventory_model.feed_csv(gt_path, columns=['STRAWBERRIES', 'DATE', 'TRANSACTION'])

    print('Training in progress...')
    inventory_model.train()

    # save model
    save_model(inventory_model, 'strawberry')
    return "Training is succesfully done."




