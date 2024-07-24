"""
The main file that deals with the overall running of the app.
Instantiates a new APIClient to which we can call all endpoints
"""
from tabulate import tabulate
from simple_term_menu import TerminalMenu
from .apiclient import APIClient
from .menu import Menu


class Main():
    """
    Main() class that handles the app logic. Displaying data, fetching data
    and showing menu items.

    Creates a new APIClient when intialized.
    """
    
    def __init__(self):

        leagues = [
            {"code": "PL", "name": "Premier League"},
            {"code": "FL1", "name": "Ligue 1"},
            {"code": "PD", "name": "La Liga"},
            {"code": "BL1", "name": "Bundesliga"},
            {"code": "SA", "name": "Serie A"},
        ]

        title = "  Main Menu.\n  Choose your League\n  Press Q or Esc to quit. \n"
        items = [league["name"] for league in leagues]
        exit = False
        

        menu = Menu(title, items)
        main = menu.menu()
        main_option = main.show()
        
        league_code = leagues[main_option]["code"]

        client = APIClient(league_code)
        seasons = client.competitions.get_competition_seasons()

        menu.main_menu_items = [season["Name"] for season in seasons]
        menu.main_menu_title = "Leagues"
        season = menu.menu()
        season_option = season.show()

        client.season = seasons[season_option]["Year"]

        league_options = [
            {"code": "comp_teams", "option": "Show All Teams"},
            {"code": "comp_standings", "option": "Show League Table"},
            {"code": "comp_matches", "option": "Show All Results"},
            {"code": "teams_matches", "option": "Show a Teams Results"},
            {"code": "comp_goalscorers", "option": "Show Top 10 Goalscorers"},
        ]

        menu.main_menu_items = [l_option["option"] for l_option in league_options]
        menu.main_menu_title = "Leagues"
        foo = menu.menu()
        foo_option = foo.show()
        
        endpoint = league_options[foo_option]["code"]

        if endpoint == "comp_teams":
            data = client.competitions.get_competition_teams()
            print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
        elif endpoint == "comp_standings":
            data = client.competitions.get_competition_standings()
            print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
        elif endpoint == "comp_matches":
            data = client.competitions.get_competition_matches()
            print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
        elif endpoint == "teams_matches":
            data = client.teams.get_teams_matches()
            print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
        elif endpoint == "comp_goalscorers":
            data = client.competitions.get_competition_goalscorers()
            print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
