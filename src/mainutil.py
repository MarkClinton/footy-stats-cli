"""
This class handles creating and displaying menu's for the end user
"""
import os
import textwrap
from tabulate import tabulate
from simple_term_menu import TerminalMenu
from getch import pause
from .enums import Menu


class MenuUtil():

    """
    Mixin class to handle all menu functionality
    """

    LEAGUE_MENU_OPTIONS = [
            {"code": "PL", "option": "Premier League"},
            {"code": "FL1", "option": "Ligue 1"},
            {"code": "PD", "option": "La Liga"},
            {"code": "BL1", "option": "Bundesliga"},
            {"code": "SA", "option": "Serie A"}
        ]

    MAIN_MENU_OPTIONS = [
            {"code": "comp_teams", "option": "Show All Teams"},
            {"code": "comp_standings", "option": "Show League Table"},
            {"code": "comp_matches", "option": "Show All Fixtures/Results"},
            {"code": "teams_matches", "option": "Show Teams Fixtures/Results"},
            {"code": "comp_goalscorers", "option": "Show Top 10 Goalscorers"}
        ]
    
    START_MENU_OPTIONS = [
        {"code": "start", "option": "Start"},
        {"code": "help", "option": "Help"},
        {"code": "about", "option": "About Footy Stats CLI"}
    ]

    START_MENU = "start"
    LEAGUE_MENU = "league"
    MAIN_MENU = "main"
    SEASON_MENU = "season"
    TEAM_MENU = "team"

    def menu(self, menu_options: list, title: str) -> TerminalMenu:
        """
        returns a TerminalMenu

        :params menu_options: a list of options to populate the menu
        :params title: A string to use as the menu title
        """
        menu = TerminalMenu(
            menu_entries=menu_options,
            title=title,
            menu_cursor="> ",
            menu_cursor_style=("fg_green", "bold"),
            menu_highlight_style=("bg_green", "fg_yellow", "bold"),
            cycle_cursor=True,
            clear_screen=True,
        )
        return menu

    def create_menu(self, identifier: str,
                    menu_data: str = None) -> TerminalMenu:
        """
        Create a TerminalMenu with the necessary menu options. Returns a
        Terminal Menu.

        :params identifier: the name of the menu
        :params menu_data: the data to use to populate menu
        """

        match identifier:
            case self.MAIN_MENU:
                data = [menu["option"] for menu in self.MAIN_MENU_OPTIONS]
            case self.LEAGUE_MENU:
                data = [league["option"] for league in self.LEAGUE_MENU_OPTIONS]
            case self.START_MENU:
                data = [start["option"] for start in self.START_MENU_OPTIONS]
            case self.SEASON_MENU:
                data = self.list_to_menu_options(menu_data, "Name")
            case self.TEAM_MENU:
                data = self.list_to_menu_options(menu_data, "Team")

        title = self.get_menu_title(identifier)
        return self.menu(data, title)

    def get_menu_option(self, identifier: str, pos: int,
                        menu_data: list = None) -> str:
        """
        Return the users selected menu option

        :param identifier: the name of the menu
        :param pos: the position of the item in the list
        :param menu_data: the list used to populate the menu
        """
        match identifier:
            case self.MAIN_MENU:
                option = self.MAIN_MENU_OPTIONS[pos]["code"]
            case self.LEAGUE_MENU:
                self.league_choice = self.LEAGUE_MENU_OPTIONS[pos]["option"]
                option = self.LEAGUE_MENU_OPTIONS[pos]["code"]
            case self.START_MENU:
                option = self.START_MENU_OPTIONS[pos]["code"]
            case self.SEASON_MENU:
                self.season_choice = menu_data[pos]["Name"]
                option = menu_data[pos]["Year"]
            case self.TEAM_MENU:
                option = menu_data[pos]["ID"]
        return option

    def get_menu_title(self, identifier: str) -> str:
        """
        Returns the title for a menu

        :param identifier: the menu name
        """

        if identifier == self.MAIN_MENU:
            main_menu = Menu.MAIN_MESSAGE.value.format(
                                            comp=self.league_choice,
                                            season=self.season_choice)
            about = Menu.MAIN_ABOUT.value
            message = main_menu
        elif identifier == self.LEAGUE_MENU:
            about = Menu.LEAGUE_ABOUT.value
            message = Menu.LEAGUE_MESSAGE.value
        elif identifier == self.START_MENU:
            about = Menu.START_ABOUT.value
            message = Menu.START_MESSAGE.value
        elif identifier == self.SEASON_MENU:
            about = Menu.SEASON_ABOUT.value
            message = Menu.SEASON_MESSAGE.value
        elif identifier == self.TEAM_MENU:
            about = Menu.TEAM_ABOUT.value
            message = Menu.TEAM_MESSAGE.value

        logo = textwrap.dedent(Menu.LOGO.value)
        title = logo + about + message
        return title

    def display_menu(self, identifier: str) -> bool:
        """
        Logic to display a menu and fetch menu options. Logs users selection
        for League & Seasonand sets the corresponding APIClient instance
        variable. Returns bool to tell the manu while loop how to progress.
        """
        message = "\nPress any key to go back to the Main Menu..."

        if identifier == self.SEASON_MENU:
            seasons = self.client.competitions.get_competition_seasons()
            menu = self.create_menu(identifier, seasons)
        elif identifier == self.TEAM_MENU:
            teams = self.client.competitions.get_list_teams()
            menu = self.create_menu(identifier, teams)
        else:
            menu = self.create_menu(identifier)

        menu_sel = menu.show()
        if menu_sel is None:
            return False

        match identifier:
            case self.MAIN_MENU:
                if menu_sel == 3:
                    if not self.display_menu(self.TEAM_MENU):
                        return True
                self.fetch_data(menu_sel)
                pause(message)
                self.clear_display()
            case self.LEAGUE_MENU:
                league = self.get_menu_option(identifier, menu_sel)
                self.client.league = league
            case self.START_MENU:
                if menu_sel != 0:
                    if not self.handle_start_menu(menu_sel):
                        return self.display_menu(self.START_MENU)
            case self.SEASON_MENU:
                season = self.get_menu_option(identifier, menu_sel,
                                              seasons)
                self.client.season = season
            case self.TEAM_MENU:
                self.client.team = self.get_menu_option(identifier, menu_sel,
                                                        teams)
        return True

    def handle_start_menu(self, sel: int) -> bool:
        """
        Functionality for the start menu. Depending on the selection show the 
        corresponding information. Returns false to signal to show the start
        menu again.

        :param sel: int of the users menu selection
        """
        message = "\nPress any key to go back to the Start Menu..."
        logo = textwrap.dedent(Menu.LOGO.value)
        if sel == 1:
            help_message = Menu.HELP_MESSAGE.value
            print(logo + help_message)
            pause(message)
        elif sel == 2:
            about_message = Menu.ABOUT_MESSAGE.value
            print(logo + about_message)
            pause(message)
        self.clear_display()
        return False

    def list_to_menu_options(self, data: list, k: str) -> list:
        """
        Takes a list of dict items and returns a clean list of strings to use
        as menu options.

        :param data: list of dict items
        :param k: the key of the dict value
        """
        return [d[k] for d in data]

    def finish(self) -> str:
        """ Builds string to display when the user exits the application """

        logo = textwrap.dedent(Menu.LOGO.value)
        message = "\n Thanks for using Footy Stats CLI.\n"
        title = logo + message

        print(title)

    def fetch_data(self, main_sel: str):
        """
        Using the MAIN_MENU_OPTIONS list it selects the option chosen by the
        user and fetches the data from the API. Python-tabulate is used to
        display the data in table format.
        """
        option = self.get_menu_option(self.MAIN_MENU, main_sel)

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

    def clear_display(self):
        """ Determines the OS. Clears the terminal screen. """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
