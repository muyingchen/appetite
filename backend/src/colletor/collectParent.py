"""
Collecter interface

Inherit it to use and override all the functions speicfied here.
"""

class CollectParent:
    def __init__(self, type=None):
        self.type = type

    def collect(self):
        """
        collect function should start collect data and pass to the proper data pipeline
        """
        pass
