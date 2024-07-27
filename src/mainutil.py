"""
This class handles creating and displaying menu's for the end user
"""
from tabulate import tabulate
from simple_term_menu import TerminalMenu
import os
import textwrap
from getch import pause
from .enums import Menu

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
    
    def create_menu(self, identifier, menu_data=None):

        match identifier:
            case "main":
                data = [menu["option"] for menu in self.MAIN_MENU]
            case "league":
                data = [league["name"] for league in self.LEAGUES]
            case "season":
                data = self.list_to_menu_options(menu_data, "Name")
            case "team":
                data = self.list_to_menu_options(menu_data, "Team")

        title = self.menu_title(identifier)
        return self.menu(data, title)
    
    def get_menu_option(self, identifier, pos, menu_data=None):

        match identifier:
            case "main":
                option = self.MAIN_MENU[pos]["code"]
            case "league":
                self.league_choice = self.LEAGUES[pos]["name"]
                option = self.LEAGUES[pos]["code"]
            case "season":
                self.season_choice = menu_data[pos]["Name"]
                option = menu_data[pos]["Year"]
            case "team":
                option = menu_data[pos]["ID"]
        return option
    
    def menu_title(self, identifier):

        main_menu = Menu.MAIN_MESSAGE.value.format(comp=self.league_choice, 
                                                    season=self.season_choice)
        if identifier == "main":
            about = Menu.MAIN_ABOUT.value
            message = main_menu
        elif identifier == "league":
            about = Menu.LEAGUE_ABOUT.value
            message = Menu.LEAGUE_MESSAGE.value
        elif identifier == "season":
            about = Menu.SEASON_ABOUT.value
            message = Menu.SEASON_MESSAGE.value
        elif identifier == "team":
            about = Menu.TEAM_ABOUT.value
            message = Menu.TEAM_MESSAGE.value
        
        logo = textwrap.dedent(Menu.LOGO.value)
        title = logo + about + message
        return title
    
    # Misc functionlaity for menus
    def list_to_menu_options(self, data: list, k: str ) -> list:
        """
        Takes a list of dict items and returns a clean list of strings to use
        as menu options.

        :param data: list of dict items
        :param k: the key of the value needed
        """
        return [d[k] for d in data]

    def end_screen(self) -> str:
        """ Builds string to display when the user exits the application """

        logo = textwrap.dedent(Menu.LOGO.value)
        message = "\n Thanks for using Footy Stats CLI.\n"
        title = logo + message
        
        print(title)
    
    def league_menu(self):
        menu = self.create_menu("league")
        menu_sel = menu.show()

        if menu_sel == None:
            return False
        
        league = self.get_menu_option("league", menu_sel)
        self.client.league = league
        return True

    def season_menu(self):
        seasons = self.client.competitions.get_competition_seasons()
        menu = self.create_menu("season", seasons)
        menu_sel = menu.show()

        if menu_sel == None:
            return False
        
        client_season = self.get_menu_option("season", menu_sel, seasons)
        self.client.season = client_season
        return True   

    def main_menu(self):
        message = "\nPress any key to go back to the Main Menu..."
        menu = self.create_menu("main")  
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

    def team_menu(self):
        teams = self.client.competitions.get_list_teams()
        menu = self.create_menu("team", teams)
        menu_sel = menu.show()
        if menu_sel == None:
            return False
        self.client.team = self.get_menu_option("team", menu_sel, teams)
        return True
    
    def fetch_data(self, main_sel):
        option = self.get_menu_option("main", main_sel)

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



