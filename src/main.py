"""
The main file that deals with the overall running of the app.
Instantiates a new APIClient to which we can call all endpoints
"""
from tabulate import tabulate
from simple_term_menu import TerminalMenu
from .apiclient import APIClient
from .menu import Menu
from getch import pause


class Main(Menu):
    """
    Main() class that handles the app logic. Displaying data, fetching data
    and showing menu items.

    Creates a new APIClient when intialized.
    """
    
    def __init__(self):     
        self.test()


    def test(self):

        league_menu = self.create_league_menu()
        main_menu = self.create_main_menu()
        league_exit = True
        season_exit = True
        main_menu_exit = True

        while league_exit:
            league_sel = league_menu.show()

            if league_sel == None:
                break
            else:
                league = self.get_league_option(league_sel)
                client = APIClient(league)
                
                while season_exit:
                    seasons = client.competitions.get_competition_seasons()
                    season_menu = self.create_season_menu(seasons)
                    season_sel = season_menu.show()

                    if season_sel == None:
                        break
                    else:
                        client_season = self.get_season_option(seasons, season_sel)
                        client.season = client_season

                        while main_menu_exit:
                            main_sel = main_menu.show()

                            if main_sel == None:
                                break
                            elif main_sel == 3:
                                teams = client.competitions.get_competition_teams()
                                team_menu = self.create_teams_menu(teams)
                                team_sel = team_menu.show()
                                client_team = self.get_team_option(teams,team_sel)
                                client.team = client_team
                                self.gather_info(main_sel, client)
                                pause("\nPress any key to go back to "
                                    "the main menu...")
                            else:
                                self.gather_info(main_sel, client)
                                pause("\nPress any key to go back to "
                                    "the main menu...")

        print("Thanks for using Foot-Stats-CLI")

    def gather_info(self, main_sel, client):
        option = self.get_main_option(main_sel)
            
        if option == "comp_teams":
            data = client.competitions.get_competition_teams()
        elif option == "comp_standings":
            data = client.competitions.get_competition_standings()
        elif option == "comp_matches":
            data = client.competitions.get_competition_matches()
        elif option == "teams_matches":
            data = client.teams.get_teams_matches()
        elif option == "comp_goalscorers":
            data = client.competitions.get_competition_goalscorers()

        print(tabulate(data, headers="keys", colalign=("left",), 
                        tablefmt="rounded_outline"))