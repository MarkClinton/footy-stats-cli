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
            {"code": "SA", "name": "Serie A"},
        ]
    
    MAIN_MENU = [
            {"code": "comp_teams", "option": "Show All Teams"},
            {"code": "comp_standings", "option": "Show League Table"},
            {"code": "comp_matches", "option": "Show All Results"},
            {"code": "teams_matches", "option": "Show a Teams Results"},
            {"code": "comp_goalscorers", "option": "Show Top 10 Goalscorers"},
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
    
    def get_league_menu(self):
        return [league["name"] for league in self.LEAGUES]
    
    def get_league_title(self):
        return "Leagues"
    
    def get_league_option(self, pos):
        return self.LEAGUES[pos]["code"]

    def get_main_menu(self):
        return [m["option"] for m in self.MAIN_MENU]

    def get_main_title(self):
        return "Main Menu"
    
    def get_main_option(self, pos):
        return self.MAIN_MENU[pos]["code"]
    
    def list_to_menu_options(self, data, k):
        return [d[k] for d in data]
    
    def get_list_option(self, data, pos):
        return data[pos]["Year"]