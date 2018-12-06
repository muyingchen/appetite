import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from sklearn import linear_model
import datetime
from backend.src.data_provider.csv_manager import CSVManager
import warnings
from backend.src.ml_model.inventory_type import inventory_type

warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = 14, 10


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
        if 'DATE' not in columns:
            raise Exception("Include DATE as a field")

        if path in self.read_file:
            raise Exception("You cannot read the same file twice. {} is already fed to this class".format(path))

        # update column
        self.columns += columns

        # read data
        csv_manager = CSVManager(path)
        csv_data = csv_manager.read()

        csv_data_len = int(len(csv_data))
        csv_data, csv_test_data = csv_data[:csv_data_len - 365], csv_data[csv_data_len - 365:]

        def create_data_frame(csv_data, df):
            # get data per column to feed dataframe
            data_per_column = []
            for column in columns:
                # timestamp is handled specially
                if column == 'DATE':
                    timestamps = [datetime.datetime.strptime(data['DATE'], "%Y-%m-%d").month * 100
                                  + datetime.datetime.strptime(data['DATE'], "%Y-%m-%d").day
                                  for data in csv_data]
                    data_per_column.append(timestamps)
                elif column == 'TRANSACTION':
                    data_at_column = [int(data['STRAWBERRIES']) + random.randint(-3, 3) for data in csv_data]
                    data_per_column.append(data_at_column)
                else:
                    data_at_column = [int(data[column]) for data in csv_data]
                    data_per_column.append(data_at_column)

            # merge new dataframe to the previous dataframe
            new_dataframe = pd.DataFrame(np.column_stack(data_per_column), columns=columns)
            if df is None:
                return new_dataframe
            else:
                return pd.merge(df, new_dataframe, on='DATE')

        # training_data ==================================================
        self.dataframe = create_data_frame(csv_data, self.dataframe)
        # testing_data =======================================================
        self.test_dataframe = create_data_frame(csv_test_data, self.test_dataframe)

        self.read_file.append(path)

    def train(self, alpha=.1):
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
        prediction = self.model.predict(self.test_dataframe.copy().drop(columns=self.label))

        plt.plot(self.test_dataframe['DATE'], prediction, '.', ms=16);
        # plt.plot(self.dataframe['DATE'], self.dataframe[self.label], '.', ms=16)

        rss = sum((prediction - self.test_dataframe[self.label]) ** 2) / self.test_dataframe.shape[0]  # num_of_rows
        print("rss: {}".format(rss))

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





