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
        
        seasons = client.competitions.get_competition_seasons()
        for i in seasons:
            print(i)

        matches = client.teams.get_teams_matches()
        for i in matches:
            print(i)

        
        
        