"""
The main file that deals with the overall running of the app.
Instantiates a new APIClient to which we can call all endpoints
"""
from tabulate import tabulate
from simple_term_menu import TerminalMenu
from .apiclient import APIClient
from .menu import Menu


class Main(Menu):
    """
    Main() class that handles the app logic. Displaying data, fetching data
    and showing menu items.

    Creates a new APIClient when intialized.
    """
    
    def __init__(self):

        league_menu = self.menu(self.get_league_menu(), self.get_league_title())
        league_sel = league_menu.show()
        league = self.get_league_option(league_sel)

        client = APIClient(league)
        seasons = client.competitions.get_competition_seasons()
        season_options = self.list_to_menu_options(seasons, "Name")

        season_menu = self.menu(season_options, "Seasons")
        season_sel = season_menu.show()

        client_season = self.get_list_option(seasons, season_sel)
        client.season = client_season

        main_menu = self.menu(self.get_main_menu(), self.get_main_title())
        main_sel = main_menu.show()

        endpoint = self.get_main_option(main_sel)

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
