"""
The main file that deals with the overall running of the app.
Instantiates a new APIClient to which we can call all endpoints
"""
from tabulate import tabulate
from .apiclient import APIClient
from .menu import Menu, ClearDisplay
from getch import pause


class Main(Menu, ClearDisplay):
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

        print("Thanks for using Footy-Stats-CLI")

    def show_league_menu(self):
        menu = self.create_league_menu()
        menu_sel = menu.show()

        if menu_sel == None:
            return False
        league = self.get_league_option(menu_sel)
        self.client = APIClient(league)
        self.league_choice = str(league)
        return True

    def show_season_menu(self):
        seasons = self.client.competitions.get_competition_seasons()
        menu = self.create_season_menu(seasons)
        menu_sel = menu.show()

        if menu_sel == None:
            return False
        client_season = self.get_season_option(seasons, menu_sel)
        self.client.season = client_season  
        self.season_choice = str(client_season)
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

        table = tabulate(data, headers="keys", colalign=("left",), 
                        tablefmt="simple")
        print(table)
        