# The main file that deals with the overall running of the app.
# Instantiates a new APIClient to which we can call all endpoints

from .apiclient import APIClient

class Main():

    """
    Main() class that handles the app logic. Displaying data, fetching data
    and showing menu items.

    Creates a new APIClient when intialized.
    """
    
    def __init__(self):

        client = APIClient()
        print(client.competitions.get_competitions_list())
