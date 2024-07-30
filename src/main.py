"""
The main file that deals with the overall running of the app.
Instantiates a new APIClient to which we can call all endpoints
"""
from tabulate import tabulate
from .apiclient import APIClient
from .mainutil import MenuUtil


class Main(MenuUtil):
    """
    Main() class that handles the app logic. Displaying data, fetching data
    and showing menu items.

    Creates a new APIClient when intialized.
    """

    def __init__(self): 
        # Initialize a default APIClient
        self.client = APIClient("PL", "2023")
        data = self.client.competitions.get_competition_matches()
        for num in self.paginate(data):
            print(num)
            input()
            self.clear_display()
        # self.start()
        # self.test()
        

    def start(self):
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


    def test(self):
        def nextSquare():
            i = 1
        
            # An Infinite loop to generate squares
            while True:
                yield i*i
                print("hey")
                i += 1  # Next execution resumes
                # from this point
        
        
        # Driver code to test above generator
        # function
        for num in nextSquare():
            if num > 100:
                break
            print(num)
            input()
