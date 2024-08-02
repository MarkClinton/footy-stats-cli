"""
This class handles creating and displaying menu's for the end user
"""
import os
from typing import Generator
from blessed import Terminal
from tabulate import tabulate
from simple_term_menu import TerminalMenu
from src.apptext import AppText


class MenuUtil():
    """ Mixin class to handle all menu functionality """

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

    term = Terminal()

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
            menu_cursor_style=("fg_yellow", "bold"),
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
                data = [
                    league["option"] for league in self.LEAGUE_MENU_OPTIONS
                ]
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
        """
        Returns the string to be displayed on a screen

        :params identifier: the menu name
        """
        if identifier == self.MAIN_MENU:
            user_choice = (
                f'{AppText.GREEN}{self.league_choice} '
                f'Season {self.season_choice}{AppText.NORMAL}'
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
            print(AppText.PROCESSING)
            seasons = self.client.competitions.get_competition_seasons()
            if not seasons:
                return False
            menu = self.create_menu(identifier, seasons)
        elif identifier == self.TEAM_MENU:
            print(AppText.PROCESSING)
            teams = self.client.competitions.get_list_teams()
            if not teams:
                return False
            menu = self.create_menu(identifier, teams)
        else:
            menu = self.create_menu(identifier)

        self.clear_display()
        if identifier != self.TEAM_MENU:
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
                season = self.get_menu_option(identifier, menu_sel, seasons)
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
        self.clear_display()
        message = f'\nPress {AppText.ENTER} to go back to the start menu..'
        logo = AppText.LOGO
        if sel == 1:
            help_message = AppText.HELP_MESSAGE
            print(logo + help_message)
            self.user_enter_action(message)
            return False
        elif sel == 2:
            about_message = AppText.ABOUT_MESSAGE
            print(logo + about_message)
            self.user_enter_action(message)
            return False
        self.clear_display()
        return True

    def list_to_menu_options(self, data: list, k: str) -> list:
        """
        Takes a list of dict items and returns a clean list of strings to use
        as menu options.

        :param data: list of dict items
        :param k: the key of the dict value
        """
        return [d[k] for d in data]

    def user_enter_action(self, message: str):
        """
        Displays to the user a message and accepts only valid input.

        :param message: message to display before validating input.
        """
        print(message)
        with self.term.cbreak():
            val = self.term.inkey()
            while val.name != 'KEY_ENTER':
                print(AppText.ERROR_INPUT)
                val = self.term.inkey()

    def user_enter_or_action(self) -> bool:
        """
        Returns boolean to determine if the user wants to continue
        to the next page or exit. Used on results that are paginated.
        Print error message if input is not valid.
        """
        valid = ['KEY_ENTER', 'q']
        with self.term.cbreak():
            val = self.term.inkey()
            while val.name not in (valid):
                if val.name == 'KEY_ENTER':
                    return False
                elif val.lower() == 'q':
                    return True
                else:
                    print(AppText.ERROR_INPUT)
                    val = self.term.inkey()

    def finish(self) -> str:
        """ Builds string to display when the user exits the application """
        self.clear_display()
        logo = AppText.LOGO
        message = "\nThanks for using Footy Stats CLI.\n"
        title = logo + message
        print(title)

    def fetch_data(self, main_sel: str):
        """
        Using the MAIN_MENU_OPTIONS list it selects the option chosen by the
        user and fetches the data from the API. Python-tabulate is used to
        display the data in table format.
        """
        print(AppText.PROCESSING)
        option = self.get_menu_option(self.MAIN_MENU, main_sel)
        if option == "comp_teams":
            data = self.client.competitions.get_competition_teams()
            header = (
                f'{AppText.GREEN}{self.league_choice} Teams '
                f'{self.season_choice}{AppText.NORMAL}'
            )
        elif option == "comp_standings":
            data = self.client.competitions.get_competition_standings()
            header = (
                f'{AppText.GREEN}{self.league_choice} Table '
                f'{self.season_choice}{AppText.NORMAL}'
            )
        elif option == "comp_matches":
            data = self.client.competitions.get_competition_matches()
            header = (
                f'{AppText.GREEN}{self.season_choice} '
                f'{self.league_choice} Matches{AppText.NORMAL}'
            )
        elif option == "teams_matches":
            data = self.client.teams.get_teams_matches()
            header = (
                f'{AppText.GREEN}{self.team_choice} {self.season_choice} '
                f'Matches{AppText.NORMAL}'
            )
        elif option == "comp_goalscorers":
            data = self.client.competitions.get_competition_goalscorers()
            header = (
                f'{AppText.GREEN}Top 10 {self.league_choice} '
                f'Goalscorers {self.season_choice}{AppText.NORMAL}'
            )
        self.clear_display()
        self.print_data(data, header)

    def print_data(self, data: list, header: str):
        """
        Accepts a list of data, string of header to display on screen.
        Processes the data and prints to screen.

        :params data: list of data
        :params header: identifier str of the data printed
        """
        message = f'\nPress {AppText.ENTER} to go back to the main menu..'
        if data and len(data) >= 20:
            for items, current_page, pages in self.paginate(data):
                table = tabulate(
                        items, headers="keys", tablefmt="simple"
                        )
                print(header)
                print(table)
                print(f'\nPage {current_page} of {pages}')
                if current_page == pages:
                    print(
                        f'Press {AppText.ENTER} to go back to the '
                        f'main menu..'
                    )
                else:
                    print(
                        f'Press {AppText.ENTER} for next page or '
                        f'{AppText.Q} for main menu..'
                    )
                if self.user_enter_or_action():
                    break
                self.clear_display()
                self.clear_display()
        elif data:
            table = tabulate(data, headers="keys", tablefmt="simple")
            print(header)
            print(table)
            self.user_enter_action(message)
        else:
            table = tabulate(
                    data, headers=["No Data Found"], tablefmt="simple"
                    )
            print(header)
            print(table)
            self.user_enter_action(message)

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

    def clear_display(self):
        """ Determines the OS. Clears the terminal screen. """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
        # Below ensures nothing is left in the scrollback buffer
        print("\033[3J\033[H\033[2J", end='')
        os.sys.stdout.flush()
