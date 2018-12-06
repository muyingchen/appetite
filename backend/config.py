import os

class Config(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "appetite"

config_wd = os.getcwd()
dir_path = {
    'frontend': os.path.join(config_wd, '..', 'frontend'),
    'data': os.path.join(config_wd, 'data'),
    'model': os.path.join(config_wd, 'model')
}