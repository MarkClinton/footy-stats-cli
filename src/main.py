"""
The main file that deals with the overall running of the app.
Instantiates a new APIClient to which we can call all endpoints
"""
from src.apiclient import APIClient
from src.mainutil import MenuUtil


class Main(MenuUtil):
    """
    Main() class that handles the app logic. Displaying data, fetching data
    and showing menu items.

    Creates a new APIClient when intialized.
    """

    def __init__(self):
        # Initialize a default APIClient
        self.client = APIClient("PL")
        self.start()

    def start(self):
        """
        Start of the program. Calls each menu option and progresses as
        needed.
        """
        menu_show = True
        while menu_show:
            menu_show = self.display_menu("start")
            while menu_show:
                if not self.display_menu("league"):
                    break
                while menu_show:
                    if not self.display_menu("season"):
                        break
                    while menu_show:
                        if not self.display_menu("main"):
                            break
        self.finish()
