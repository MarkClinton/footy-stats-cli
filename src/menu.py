"""
This class handles creating and displaying menu's for the end user
"""
from tabulate import tabulate
from simple_term_menu import TerminalMenu
import os

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
            {"code": "comp_matches", "option": "Show All Fixtures/Results"},
            {"code": "teams_matches", "option": "Show Teams Fixtures/Results"},
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
    def create_league_menu(self):
        menu_data = [league["name"] for league in self.LEAGUES]
        title = self.start_screen_info()
        return self.menu(menu_data, title)
    
    def get_league_option(self, pos):
        return self.LEAGUES[pos]["code"]

    # Main menu functionality
    def create_main_menu(self):
        menu_data = [menu["option"] for menu in self.MAIN_MENU]
        title = self.main_screen_info()
        return self.menu(menu_data, title)
    
    def get_main_option(self, pos):
        return self.MAIN_MENU[pos]["code"]

    # Season menu functionality
    def create_season_menu(self, seasons_data):
        season_data = self.list_to_menu_options(seasons_data, "Name")
        title = self.season_screen_info()
        return self.menu(season_data, title)
    
    def get_season_option(self, data, pos):
        return data[pos]["Year"]

    # Team menu functionality
    def create_team_menu(self, teams_data):
        team_data = self.list_to_menu_options(teams_data, "Team")
        title = self.team_screen_info()
        return self.menu(team_data, title)
    
    def get_team_option(self, data, pos):
        return data[pos]["ID"]
    
    # Misc functionlaity for menus
    def list_to_menu_options(self, data, k):
        return [d[k] for d in data]

    def footy_stats_logo(self):
        return """
              ______               __            _____  __          __           ______ __     ____
             / ____/____   ____   / /_ __  __   / ___/ / /_ ____ _ / /_ _____   / ____// /    /  _/
            / /_   / __ \ / __ \ / __// / / /   \__ \ / __// __ `// __// ___/  / /    / /     / /  
           / __/  / /_/ // /_/ // /_ / /_/ /   ___/ // /_ / /_/ // /_ (__  )  / /___ / /___ _/ /   
          /_/     \____/ \____/ \__/ \__, /   /____/ \__/ \__,_/ \__//____/   \____//_____//___/   
                                    /____/                                                         
            """
    
    def start_screen_info(self):
        about = ("\nFooty Stats CLI is an application for all football related "
        "data. Using the Football-Data API\nto gather data about Leagues, "
        "Fixtures/Results, Teams and Goalscorers.\n")

        instructions = ("\nTo navigate the app, use the keyboard. [Up/Down] on "
                        "the keyboard moves through menu options.\n[Enter] "
                        "selects the option. [Q/ESC] navigates to the previous"
                        " menu or quits the app.\n")
        
        title = ("\nTo get started, select the LEAGUE you want to view " 
                "data for:\n")
        return self.footy_stats_logo() + about + instructions + title
    
    def season_screen_info(self):
        about = ("\nFooty Stats CLI shows up to 10 seasons worth of historical "
                "data.\n")
        title = ("\nSelect the SEASON you wish to view data for:\n")

        return self.footy_stats_logo() + about + title
    
    def main_screen_info(self):
        about = ("\nFooty Stats CLI has 5 main options to choose from. For more "
                "information on each option press [h]\n")

        title = "\nSelect an option below:\n"
        return self.footy_stats_logo() + about + title
    
    def team_screen_info(self):
        title = ("\nSelect a team to view their Fixtures/Results:\n")

        return self.footy_stats_logo() + title

class ClearDisplay():

    def clear_display(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  
            command = 'cls'
        os.system(command)



