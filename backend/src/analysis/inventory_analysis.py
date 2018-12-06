"""
Collection of analysis functions for data analysis.

Currently, there are only very simple functions
"""
def generate_recommendation_statement(inventory,
                                      inventory_name='pumpkin',
                                      ):
    """
    TODO Currently hardcoded but we will need algorithm for this
    :param inventory: list of inventories
    :return: recommendation statement that will be rendered on dashboard.html
    """
    inventory_name = plurafy(inventory_name)
    return 'You will need to prepare {} more {} {}'.format('30', inventory_name, 'from Oct 25 to Nov 3')

def plurafy(name):
    if name != 'strawberry':
        return "{}s".format(name)
    else:
        return "strawberries"