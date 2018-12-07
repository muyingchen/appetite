"""
Collection of analysis functions for data analysis.

Currently, there are only very simple functions
"""
def generate_recommendation_statement(inventory,
                                      prediction_data,
                                      start_date,
                                      end_date,
                                      inventory_name='pumpkin',
                                      ):
    """
    TODO Currently hardcoded but we will need algorithm for this
    :param inventory: list of inventories
    :return: recommendation statement that will be rendered on dashboard.html
    """
    inventory_name = plurafy(inventory_name)
    inventory_length = len(inventory)

    needed_amount = sum(prediction_data[:inventory_length]) - sum(inventory)
    return 'You will need to prepare {} more {} from {} to {}'\
        .format(int(needed_amount), inventory_name, start_date, end_date)

def plurafy(name):
    if name != 'strawberry':
        return "{}s".format(name)
    else:
        return "strawberries"