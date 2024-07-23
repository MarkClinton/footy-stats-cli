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

        client = APIClient("PL")
        
        seasons = client.competitions.get_competition_seasons()
        for i in seasons:
            print(i)
        
        print("\n---------------\n")
        client.season = "2022"
        teams = client.competitions.get_competition_teams()
        for i in teams:
            print(i)

        print("\n---------------\n")

        standings = client.competitions.get_competition_standings()
        for i in standings:
            print(i)
        
        print("\n---------------\n")

        scorers = client.competitions.get_competition_goalscorers()
        for i in scorers:
            print(i)

        print("\n---------------\n")
        # client.league = "BSA"
        comp_matches = client.competitions.get_competition_matches()
        for i in comp_matches:
            print(i)

        print("\n---------------\n")
        client.team = 1044
        matches = client.teams.get_teams_matches()
        for i in matches:
            print(i)

        
        
        