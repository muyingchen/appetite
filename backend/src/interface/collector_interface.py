"""
Collector interface will have all the functions that are for interacting with /collect endpoint
"""
TWITTER = 'twitter'

class CollectorInterface:
    def __init__(self):
        pass

    def start_collect(self, type):
        if type == TWITTER:
            pass