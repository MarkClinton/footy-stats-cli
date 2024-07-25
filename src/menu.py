"""
This class handles creating and displaying menu's for the end user
"""
from tabulate import tabulate
from simple_term_menu import TerminalMenu


class Menu():

    LEAGUES = [
            {"code": "PL", "name": "Premier League"},
            {"code": "FL1", "name": "Ligue 1"},
            {"code": "PD", "name": "La Liga"},
            {"code": "BL1", "name": "Bundesliga"},
            {"code": "SA", "name": "Serie A"}
        ]
    
    MAIN_MENU = [
            {"code": "comp_teams", "option": "Show All Teams"},
            {"code": "comp_standings", "option": "Show League Table"},
            {"code": "comp_matches", "option": "Show All Results"},
            {"code": "teams_matches", "option": "Show a Teams Results"},
            {"code": "comp_goalscorers", "option": "Show Top 10 Goalscorers"}
        ] 

    def menu(self, menu_options, title):
        menu = TerminalMenu(
            menu_entries = menu_options,
            title = title,
            menu_cursor = "> ",
            menu_cursor_style = ("fg_green", "bold"),
            menu_highlight_style = ("bg_green", "fg_yellow", "bold"),
            cycle_cursor = True,
            clear_screen = True,
        )
        return menu
    
    # League menu functionality
    def get_league_option(self, pos):
        return self.LEAGUES[pos]["code"]
    
    def create_league_menu(self):
        menu_data = [league["name"] for league in self.LEAGUES]
        title = "  League Menu.\n  Select a League.\n  Press Q or Esc to quit. \n"
        return self.menu(menu_data, title)

    # Main menu functionality
    def get_main_option(self, pos):
        return self.MAIN_MENU[pos]["code"]
    
    def create_main_menu(self):
        menu_data = [menu["option"] for menu in self.MAIN_MENU]
        title = "  Main Menu.\n  Select an Option.\n  Press Q or Esc to navigate back. \n"
        return self.menu(menu_data, title)
    
    # Season menu functionality
    def create_season_menu(self, seasons_data):
        season_data = self.list_to_menu_options(seasons_data, "Name")
        title = "  Season Menu.\n  Select a Season.\n  Press Q or Esc to navigate back. \n"
        return self.menu(season_data, title)
    
    def get_season_option(self, data, pos):
        return data[pos]["Year"]
    
    # Team menu functionality
    def create_teams_menu(self, teams_data):
        team_data = self.list_to_menu_options(teams_data, "Team")
        title = "  Team Menu.\n  Select a Team.\n  Press Q or Esc to navigate back. \n"
        return self.menu(team_data, title)
    
    def get_team_option(self, data, pos):
        return data[pos]["ID"]
    
    # Misc functionlaity for menus
    def list_to_menu_options(self, data, k):
        return [d[k] for d in data]

