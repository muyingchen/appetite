import os
import pickle
from backend.src.ml_model.inventory_type import inventory_type
from backend.config import dir_path


def get_model(inventory_type):
    model_path = get_model_path(inventory_type)
    model = None

    with open(model_path, 'rb') as pk:
        print('loading {} model...'.format(inventory_type))
        model = pickle.load(pk)

    pk.close()
    return model


def save_model(model, inventory_type):
    model_path = get_model_path(inventory_type)
    with open(model_path, 'wb') as pk:
        pickle.dump(model, pk)


def get_model_path(inventory_type):
    model_dir = dir_path['model']

    print("model directory is {}".format(model_dir))
    return "{}/{}_model.pickle".format(model_dir, inventory_type)


def is_valid_model(type):
    return type in inventory_type
