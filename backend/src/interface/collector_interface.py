"""
Collector interface will have all the functions that are for interacting with /collect endpoint
"""
from backend.src.data_provider.csv_manager import CSVManager

class CollectorInterface:
    def __init__(self, path):
        self.path = path

    def build_csv(self):
        fields = ['data', 'label', 'actual']
        csv_manager = CSVManager(self.path, fields)

        