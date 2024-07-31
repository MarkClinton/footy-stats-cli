"""
This class handles creating and displaying menu's for the end user
"""
import os
import textwrap
from typing import Generator
from tabulate import tabulate
from simple_term_menu import TerminalMenu
import getch
from .apptext import AppText


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
            clear_screen=False,
        )
        return menu

    def create_menu(
        self, 
        identifier: str,
        menu_data: str = None
    ) -> TerminalMenu:
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

    def get_menu_option(
        self, 
        identifier: str, 
        pos: int,
        menu_data: list = None
    ) -> str:
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
                self.team_choice = menu_data[pos]["Team"]
                option = menu_data[pos]["ID"]
        return option

    def get_menu_title(self, identifier: str) -> str:
        """
        Returns the title for a menu

        :param identifier: the menu name
        """

        if identifier == self.MAIN_MENU:
            title = AppText.MAIN_TITLE
        elif identifier == self.LEAGUE_MENU:
            title = AppText.LEAGUE_TITLE
        elif identifier == self.START_MENU:
            title = AppText.START_TITLE
        elif identifier == self.SEASON_MENU:
            title = AppText.SEASON_TITLE
        elif identifier == self.TEAM_MENU:
            title = AppText.TEAM_TITLE
        return title

    def get_screen_info(self, identifier: str) -> str:
        if identifier == self.MAIN_MENU:
            user_choice = (
                f'\n{self.league_choice} ' 
                f'Season {self.season_choice}'
            )
            about = AppText.MAIN_ABOUT + user_choice
        elif identifier == self.LEAGUE_MENU:
            about = AppText.LEAGUE_ABOUT
        elif identifier == self.START_MENU:
            about = AppText.START_ABOUT
        elif identifier == self.SEASON_MENU:
            about = AppText.SEASON_ABOUT
        elif identifier == self.TEAM_MENU:
            about = AppText.TEAM_ABOUT

        return about

    def display_menu(self, identifier: str) -> bool:
        """
        Logic to display a menu and fetch menu options. Logs users selection
        for League & Seasonand sets the corresponding APIClient instance
        variable. Returns bool to tell the manu while loop how to progress.
        """
        self.clear_display()
        print(AppText.LOGO)
        if identifier == self.SEASON_MENU:
            print("Processing Request....")
            seasons = self.client.competitions.get_competition_seasons()
            if not seasons:
                return False
            menu = self.create_menu(identifier, seasons)
        elif identifier == self.TEAM_MENU:
            print("Processing Request....")
            teams = self.client.competitions.get_list_teams()
            if not teams:
                return False
            menu = self.create_menu(identifier, teams)
        else:
            menu = self.create_menu(identifier)
        
        self.clear_display()
        print(AppText.LOGO)
        print(self.get_screen_info(identifier))
        menu_sel = menu.show()
        if menu_sel is None:
            return False

        match identifier:
            case self.MAIN_MENU:
                if menu_sel == 3:
                    if not self.display_menu(self.TEAM_MENU):
                        return True
                self.fetch_data(menu_sel)
                self.clear_display()
            case self.LEAGUE_MENU:
                league = self.get_menu_option(identifier, menu_sel)
                self.client.league = league
            case self.START_MENU:
                if menu_sel != 0:
                    if not self.handle_start_menu(menu_sel):
                        return self.display_menu(self.START_MENU)
            case self.SEASON_MENU:
                season = self.get_menu_option(
                    identifier, menu_sel,seasons
                    )
                self.client.season = season
            case self.TEAM_MENU:
                self.client.team = self.get_menu_option(
                    identifier, menu_sel, teams
                )
        return True

    def handle_start_menu(self, sel: int) -> bool:
        """
        Functionality for the start menu. Depending on the selection show the 
        corresponding information. Returns false to signal to show the start
        menu again.

        :param sel: int of the users menu selection
        """
        message = "\nPress [ANY KEY] to go back to the Start Menu..."
        logo = textwrap.dedent(AppText.LOGO)
        if sel == 1:
            help_message = AppText.HELP_MESSAGE
            print(logo + help_message)
            getch.pause(message)
        elif sel == 2:
            about_message = AppText.ABOUT_MESSAGE
            print(logo + about_message)
            getch.pause(message)
        self.clear_display()
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
        self.clear_display()
        logo = AppText.LOGO
        message = "\n Thanks for using Footy Stats CLI.\n"
        title = logo + message

        print(title)

    def fetch_data(self, main_sel: str):
        """
        Using the MAIN_MENU_OPTIONS list it selects the option chosen by the
        user and fetches the data from the API. Python-tabulate is used to
        display the data in table format.
        """
        print("Processing Request....")
        option = self.get_menu_option(self.MAIN_MENU, main_sel)
        if option == "comp_teams":
            data = self.client.competitions.get_competition_teams()
            header = f'All {self.league_choice} Teams {self.season_choice}\n'
        elif option == "comp_standings":
            data = self.client.competitions.get_competition_standings()
            header = f'{self.league_choice} Table {self.season_choice}\n'
        elif option == "comp_matches":
            data = self.client.competitions.get_competition_matches()
            header = f'All {self.season_choice} {self.league_choice} Matches\n'
            self.clear_display()
        elif option == "teams_matches":
            data = self.client.teams.get_teams_matches()
            header = f'{self.team_choice} {self.season_choice} Matches\n'
            self.clear_display()
        elif option == "comp_goalscorers":
            data = self.client.competitions.get_competition_goalscorers()
            header = (
                f'Top 10 {self.league_choice}' 
                f' Goalscorers {self.season_choice}\n'
            )
        self.clear_display()
        self.print_data(data, header)

    def print_data(self, data: list, header: str):
        message = "\nPress [ANY KEY] to go back to the main menu.."

        if data and len(data) >= 20:
            for items, current_page, pages in self.paginate(data):
                table = tabulate(
                        items, headers="keys", tablefmt="simple"
                        )
                print(header)
                print(table)
                print(f'\nPage {current_page} of {pages}')
                if current_page == pages:
                    print ("Press [ANY KEY] to go back to the main menu..")
                else:
                    print(
                        "Press [ANY KEY] to continue or [Q] to go back to "
                        "main menu.."
                    )
                if self.paginate_navigate():
                    break
                self.clear_display()
                self.clear_display()
        elif data:
            table = tabulate(data, headers="keys",tablefmt="simple")
            print(header)
            print(table)
            getch.pause(message)
        else:
            table = tabulate(data, headers=["No Data Found"],tablefmt="simple")
            print(header)
            print(table)
            getch.pause(message)

    def paginate(
            self, 
            data: list
    ) -> Generator[tuple[list, int, int], None, None]:
        """
        Pagination method used to only display 15 results at a time.

        :param data: list data to paginate.
        """
        results_per_page = 15
        total_pages = (len(data) // results_per_page) + 1
        page = 0
        
        for d in range(0, len(data), results_per_page):
            page = (d // results_per_page) + 1
            yield data[d:d + results_per_page], page, total_pages
    
    def paginate_navigate(self) -> bool:
        """ 
        Determines if the user wants to continue to the next page or exit
        """
        char = getch.getch()
        if char == 'q':
            self.clear_display()
            return True
        return False

    def clear_display(self):
        """ Determines the OS. Clears the terminal screen. """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
