"""
Data Pipeline Parent should be inherited to all the data pipeline classes.

All the children classes should implement all the functions that are defined here.
"""

class DataPipelineParent:
    def __init__(self, type=None):
        self.type = type

    def run_pipeline(self, data):
        """
        run_pipeline function should get the data from collector class and
            format it properly. It should save the data to database using model handler
        """
        pass
