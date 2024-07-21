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

        client = APIClient("PL", "2023")
        
        teams = client.competitions.get_competition_teams()
        print(teams)

        client2 = APIClient("PL")
        # print(client.competitions.get_competition_seasons())
        
        
        