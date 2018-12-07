import numpy as np
import pandas as pd
import random

from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

from backend.src.data_provider.csv_manager import CSVManager

import datetime
import warnings
from backend.src.ml_model.inventory_type import inventory_type

warnings.filterwarnings('ignore')


class InventoryModel:
    def __init__(self, model=linear_model.Ridge, label='y', inventory_type=inventory_type['strawberry']):
        self.columns = []
        self.dataframe = None
        self.test_dataframe = None
        self.model_type = model
        self.model = None
        self.label = label
        self.read_file = []
        self.inventory_type = inventory_type

    def feed_csv(self, path, columns=[]):
        if path in self.read_file:
            raise Exception("You cannot read the same file twice. {} is already fed to this class".format(path))

        # update column
        self.columns += columns

        # read data
        csv_manager = CSVManager(path)
        csv_data = csv_manager.read()

        csv_data_len = int(len(csv_data))

        def create_data_frame(csv_data, df):
            # get data per column to feed dataframe
            data_per_column = []
            for column in columns:
                data_at_column = [int(float(data[column])) for data in csv_data]
                data_per_column.append(data_at_column)

            # merge new dataframe to the previous dataframe
            new_dataframe = pd.DataFrame(np.column_stack(data_per_column), columns=columns)
            if df is None:
                return new_dataframe
            else:
                return pd.merge(df, new_dataframe, on='DATE')

        # training_data ==================================================
        self.dataframe = create_data_frame(csv_data, self.dataframe)

        self.read_file.append(path)

    def train(self, C=1, cache_size=500, epsilon=1, kernel='rbf'):
        self.model = self.model_type(C=C, cache_size=cache_size, epsilon=epsilon, kernel=kernel)

        features = self.dataframe.copy().drop(columns=self.label)

        # normalize the value
        scaler = StandardScaler()
        scaler.fit(features)
        features = scaler.transform(features)

        self.cof = self.model.fit(features, self.dataframe[self.label])

    def predict(self, features):
        if self.model is None:
            raise Exception("model is not trained")
        # normalize the value
        scaler = StandardScaler()
        scaler.fit(features)
        features = scaler.transform(features)

        return self.model.predict(features)


    def get_coef(self):
        if self.model == None:
            raise Exception("model hasn't been trained")

        return self.cof.coef_


    def get_dataframe(self):
        if self.dataframe is None:
            raise Exception("dataframe has not been defined")

        return self.dataframe


    def get_inventory_type(self):
        return self.inventory_type


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





