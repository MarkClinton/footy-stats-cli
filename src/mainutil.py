"""
This class handles creating and displaying menu's for the end user
"""
from tabulate import tabulate
from simple_term_menu import TerminalMenu
import os
import textwrap
from getch import pause

class MenuUtil():
    """
    Mixin class to handle all menu functionality
    """

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

    def menu(self, menu_options: list, title: str) -> TerminalMenu:
        """
        returns a TerminalMenu

        :params menu_options: a list of options to populate the menu
        :params title: A string to use as the menu title 
        """
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
    def create_league_menu(self) -> TerminalMenu:
        """ Creates the League Menu to display to the user """

        menu_data = [league["name"] for league in self.LEAGUES]
        title = self.league_screen_info()
        return self.menu(menu_data, title)
    
    def get_league_option(self, pos: int) -> str:
        """ 
        Finds the code for the chosen league selection 
        
        :params int: postion in the list of the chosen option
        """
        self.league_choice = self.LEAGUES[pos]["name"]
        return self.LEAGUES[pos]["code"]

    # Main menu functionality
    def create_main_menu(self) -> TerminalMenu:
        """ Creates the Main Menu to display to the user """

        menu_data = [menu["option"] for menu in self.MAIN_MENU]
        title = self.main_screen_info()
        return self.menu(menu_data, title)
    
    def get_main_option(self, pos) -> str:
        """ 
        Finds the code for the chosen main menu selection 
        
        :params int: postion in the list of the chosen option
        """
        return self.MAIN_MENU[pos]["code"]

    # Season menu functionality
    def create_season_menu(self, seasons_data: list) -> TerminalMenu:
        """ 
        Creates the Season Menu to display to the user 
        
        :param season_data: List of seasons to populate the menu options
        """

        season_data = self.list_to_menu_options(seasons_data, "Name")
        title = self.season_screen_info()
        return self.menu(season_data, title)
    
    def get_season_option(self, data: list, pos: int) -> str:
        """
        Finds the code for the chosen season menu selection

        :param data: list of the data used in the menu options
        :param pos: position of the chosen selection in the list
        """
        self.season_choice = data[pos]["Name"]
        return data[pos]["Year"]

    # Team menu functionality
    def create_team_menu(self, teams_data: list) -> TerminalMenu:
        """
        Creates the Teams Menu to display to the user 

        :param teams_data: list of teams to populate the menu options
        """
        team_data = self.list_to_menu_options(teams_data, "Team")
        title = self.team_screen_info()
        return self.menu(team_data, title)
    
    def get_team_option(self, data: list, pos: int) -> str:
        """
        Return the ID of the chosen team

        :param data: List of teams
        :param pos: position of the chosen selection in the list
        """
        return data[pos]["ID"]
    
    # Misc functionlaity for menus
    def list_to_menu_options(self, data: list, k: str ) -> list:
        """
        Takes a list of dict items and returns a clean list of strings to use
        as menu options.

        :param data: list of dict items
        :param k: the key of the value needed
        """
        return [d[k] for d in data]

    def footy_stats_logo(self) -> str:
        """ 
        returns an ascii string of the Footy Stats CLI logo. dedent to 
        remove unnecessary formatting  
        """

        heading = """
              ______            __           _____ __        __          ________    ____
             / ____/___  ____  / /___  __   / ___// /_____ _/ /______   / ____/ /   /  _/
            / /_  / __ \/ __ \/ __/ / / /   \__ \/ __/ __ `/ __/ ___/  / /   / /    / /  
           / __/ / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ /_/ / /_(__  )  / /___/ /____/ /   
          /_/    \____/\____/\__/\__, /   /____/\__/\__,_/\__/____/   \____/_____/___/   
                                /____/                                                                                                
        """
        return textwrap.dedent(heading)
    
    def league_screen_info(self) -> str:
        """ 
        Builds string with information about the application and the league menu
        and returns it 
        """
        
        about = ("\nFooty Stats CLI is an application for all football related "
        "data. Using the\nFootball-Data API to gather data about Leagues, "
        "Fixtures/Results, Teams\nand Goalscorers.\n")
        instructions = ("\nTo navigate the app, use the keyboard. [Up/Down] on "
                        "the keyboard moves\nthrough menu options. [Enter] "
                        "selects the option. [Q/ESC] navigates to\nthe previous"
                        " menu or quits the app.\n")
        message = ("\nTo get started, select the LEAGUE you want to view " 
                "data for:\n")
        title = self.footy_stats_logo() + about + instructions + message
        
        return title
    
    def season_screen_info(self) -> str:
        """ 
        Builds string with information about the application and the season menu
        and returns it 
        """

        about = ("\nFooty Stats CLI shows up to 10 seasons worth of historical "
                "data.\n")
        message = ("\nSelect the SEASON you wish to view data for:\n")
        title = self.footy_stats_logo() + about + message

        return title
    
    def main_screen_info(self) -> str:
        """ 
        Builds string with information about the application and the main menu
        and returns it 
        """

        about = ("\nFooty Stats CLI has 5 main options to choose from. Select "
                "your option below\n")
                
        current_choice = (f'\nCompetition: {self.league_choice}\n'
                f'Season: {self.season_choice}\n')
        
        title = self.footy_stats_logo() + about + current_choice

        return title
    
    def team_screen_info(self) -> str:
        """ 
        Builds string with information about the application and the team menu
        and returns it 
        """

        message = ("\nSelect a team to view their Fixtures/Results:\n")
        title = self.footy_stats_logo() + message

        return title
    
    def end_screen_info(self) -> str:
        """ Builds string to display when the user exits the application """

        message = "\n Thanks for using Footy Stats CLI.\n"
        title = self.footy_stats_logo() + message
        
        print(title)
    
    def show_league_menu(self):
        menu = self.create_league_menu()
        menu_sel = menu.show()

        if menu_sel == None:
            return False
        
        league = self.get_league_option(menu_sel)
        self.client.league = league
        return True

    def show_season_menu(self):
        seasons = self.client.competitions.get_competition_seasons()
        menu = self.create_season_menu(seasons)
        menu_sel = menu.show()

        if menu_sel == None:
            return False
        
        client_season = self.get_season_option(seasons, menu_sel)
        self.client.season = client_season
        return True   

    def show_main_menu(self):
        message = "\nPress any key to go back to the Main Menu..."
        menu = self.create_main_menu()  
        menu_sel = menu.show()

        if menu_sel == None:
            return False
        elif menu_sel == 3:
            if not self.show_team_menu():
                return True
            
        self.fetch_data(menu_sel)
        pause(message)  
        self.clear_display()
        return True   

    def show_team_menu(self):
        teams = self.client.competitions.get_list_teams()
        menu = self.create_team_menu(teams)
        menu_sel = menu.show()
        if menu_sel == None:
            return False
        self.client.team = self.get_team_option(teams,menu_sel)
        return True
    
    def fetch_data(self, main_sel):
        option = self.get_main_option(main_sel)

        if option == "comp_teams":
            data = self.client.competitions.get_competition_teams()
        elif option == "comp_standings":
            data = self.client.competitions.get_competition_standings()
        elif option == "comp_matches":
            data = self.client.competitions.get_competition_matches()
        elif option == "teams_matches":
            data = self.client.teams.get_teams_matches()
        elif option == "comp_goalscorers":
            data = self.client.competitions.get_competition_goalscorers()
        
        if data:
            table = tabulate(data, headers="keys", colalign=("left",), 
                        tablefmt="simple")
        else:
            table = tabulate([], headers=["No Data Found"], 
                        tablefmt="simple")
        print(table)

class ClearDisplay():
    """ 
    Mixin class to handle clearing the terminal display. 
    """

    def clear_display(self):
        """ Determines the OS. Clears the terminal screen. """
        command = 'clear'
        if os.name in ('nt', 'dos'):  
            command = 'cls'
        os.system(command)



