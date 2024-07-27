"""
The main file that deals with the overall running of the app.
Instantiates a new APIClient to which we can call all endpoints
"""
from tabulate import tabulate
from .apiclient import APIClient
from .mainutil import MenuUtil, ClearDisplay


class Main(MenuUtil, ClearDisplay):
    """
    Main() class that handles the app logic. Displaying data, fetching data
    and showing menu items.

    Creates a new APIClient when intialized.
    """

    def __init__(self): 
        # Initialize default APIClient
        self.client = APIClient("PL")   
        self.start()
        

    def start(self):
        menu_show = True

        while menu_show:
            menu_show = self.show_league_menu()
            while menu_show:
                if not self.show_season_menu():
                    break
                while menu_show:
                    if not self.show_main_menu():
                        break

        self.end_screen()
        