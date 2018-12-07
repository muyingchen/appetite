"""
Prediction interface will have every function that is for /getPrediction endpoint.
"""
import datetime
import time
from pandas import DataFrame

class PredictionInterface:
    def __init__(self):
        pass

    def generate_feature_dataframe(self, start_date='2018-11-01', end_date='2018-11-07'):
        # TODO currently hardcoded. Need automation.
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        days = (end_date - start_date).days
        timestamps = [time.mktime(start_date.timetuple())]
        for _ in range(days):
            start_date += datetime.timedelta(days=1)
            timestamps.append(time.mktime(start_date.timetuple()))

        feature_dict = {
            'beer': [33.0, 28.0, 39.0, 43.0, 18.0, 29.0, 38.0],
            'TIMESTAMP': timestamps,
            'Month': [11, 11, 11, 11, 11, 11, 11],
            'day_of_week': [3, 4, 5, 6, 0, 1, 2],
            'is_weekend': [0, 0, 1, 1, 0, 0, 0],
            'Winter': [1, 1, 1, 1, 1, 1, 1],
            'Spring': [0, 0, 0, 0, 0, 0, 0],
            'Summer': [0, 0, 0, 0, 0, 0, 0],
            'Fall': [0, 0, 0, 0, 0, 0, 0]
        }

        df = DataFrame(feature_dict)
        return df