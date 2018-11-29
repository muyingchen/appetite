import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from sklearn import linear_model
import datetime
from backend.src.data_provider.csv_manager import CSVManager
import warnings

warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = 14, 10


class Trainer:
    def __init__(self, model_type=linear_model.Ridge, label='y'):
        self.columns = []
        self.regular_data = []
        self.test_data = []
        self.dataframe = None
        self.model_type = model_type
        self.model = None
        self.label = label
        self.read_file = []
    
    
    def feed_csv(self, path, columns=[]):
        if 'DATE' not in columns:
            raise Exception("Include DATE as a field")
        
        if path in self.read_file:
            raise Exception("You cannot read the same file twice. {} is already fed to this class".format(path))
            
        # update column
        self.columns += columns
        
        # read data
        csv_manager = CSVManager(path)
        csv_data = csv_manager.read()
        
        # get data per column to feed dataframe
        data_per_column = []
        for column in columns:
            # timestamp is handled specially
            if column == 'DATE':
                timestamps = [datetime.datetime.strptime(data['DATE'], "%Y-%m-%d").month * 100
                              + datetime.datetime.strptime(data['DATE'], "%Y-%m-%d").day 
                              for data in csv_data]
                data_per_column.append(timestamps)
            else:
                data_at_column = [int(data[column]) for data in csv_data]
                data_per_column.append(data_at_column)
        
        # merge new dataframe to the previous dataframe
        new_dataframe = pd.DataFrame(np.column_stack(data_per_column), columns=columns)
        if self.dataframe is None:
            self.dataframe = new_dataframe
        else:
            self.dataframe = pd.merge(self.dataframe,
                                     new_dataframe,
                                     on='DATE')
        
        self.read_file.append(path)
    
    
    def train(self, alpha=0.5):
        self.model = self.model_type(alpha=alpha)
        
        features = self.dataframe.copy().drop(columns=self.label)
        self.cof = self.model.fit(features, self.dataframe[self.label])
    
    
    def predict(self, features):
        if self.model is None:
            raise Exception("model is not trained")
        
        return self.model.predict(features)

    
    def show_dataframe_graph(self):
        plt.plot(self.dataframe['DATE'], self.dataframe[self.label], '.', ms=16);
    
    
    def test(self):
        prediction = self.model.predict(self.dataframe.copy().drop(columns=self.label))

        plt.plot(self.dataframe['DATE'], prediction, '.', ms=16);
        plt.plot(self.dataframe['DATE'], self.dataframe[self.label], '.', ms=16)
        
    
    def get_coef(self):
        if self.model == None:
            raise Exception("model hasn't been trained")
        
        return self.cof.coef_
    
    
    def get_dataframe(self):
        if self.dataframe is None:
            raise Exception("dataframe has not been defined")
            
        return self.dataframe
    
    def reset(self):
        self.columns = []
        self.regular_data = []
        self.test_data = []
        self.dataframe = None

# example code

# trainer = Trainer(model=linear_model.Ridge, label='TAVG')
#
# trainer.feed_csv(weather_path, columns=['TAVG', 'TMAX', 'TMIN', 'DATE'])
# data = trainer.get_dataframe()
#
# trainer.show_dataframe_graph()
#
# trainer.train()
# trainer.test()





