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

@app.route('/getprediction')
def dashboard():
    return render_template("dashboard.html")

@app.route('/collect')
def collect_api():
    return "Hello, Collect!"

@app.route('/train')
def train_api():
    return "Hello, Train!"

@app.route('/getPrediction')
def prediction_query():
    return "Hello prediction"

