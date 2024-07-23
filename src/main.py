"""
The main file that deals with the overall running of the app.
Instantiates a new APIClient to which we can call all endpoints
"""
from tabulate import tabulate
from simple_term_menu import TerminalMenu
from .apiclient import APIClient


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

        options = [league["name"] for league in leagues]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        code = leagues[menu_entry_index]["code"]
        print(f"You have selected {code}!")

        client = APIClient(code)
        seasons = client.competitions.get_competition_seasons()
        print(seasons)
        season_list = [season["Name"] for season in seasons]
        terminal_menu = TerminalMenu(season_list)
        s = terminal_menu.show()
        e = seasons[s]["Year"]
        print(f"You have selected {e}!")
        client.season = e
        self.team(client)




    def season(self, client):
        
        print("\n---------------\n")
        print("Seasons")
        print("\n---------------\n")
        seasons = client.competitions.get_competition_seasons()
        print(tabulate(seasons, headers="keys", colalign=("left",), tablefmt="rounded_outline"))

    def data(self, client):
        print("\n---------------\n")
        print("League Standings")
        print("\n---------------\n")
        standings = client.competitions.get_competition_standings()
        print(tabulate(standings, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
        
        print("\n---------------\n")
        print("Top 10 Goalscorers")
        print("\n---------------\n")
        scorers = client.competitions.get_competition_goalscorers()
        print(tabulate(scorers, headers="keys", colalign=("left",), tablefmt="rounded_outline"))

        print("\n---------------\n")
        print("All Competition Matches")
        print("\n---------------\n")
        comp_matches = client.competitions.get_competition_matches()
        print(tabulate(comp_matches, headers="keys", colalign=("left",), tablefmt="rounded_outline"))

    def match(self, client):
        print("\n---------------\n")
        print("Team Matches (Team: Arsenal)")
        print("\n---------------\n")
        matches = client.teams.get_teams_matches()
        print(tabulate(matches, headers="keys", colalign=("left",), tablefmt="rounded_outline"))

    def team(self, client):
        print("\n---------------\n")
        print("Teams")
        print("\n---------------\n")
        teams = client.competitions.get_competition_teams()
        print(tabulate(teams, headers="keys", colalign=("left",), tablefmt="rounded_outline"))