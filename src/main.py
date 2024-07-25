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

        league_menu = self.menu(self.get_league_menu(), self.get_league_title())
        main_menu = self.menu(self.get_main_menu(), self.get_main_title())
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
                    season_options = self.list_to_menu_options(seasons, "Name")
                    season_menu = self.menu(season_options, 
                                            self.get_season_title())
                    season_sel = season_menu.show()

                    if season_sel == None:
                        break
                    else:
                        client_season = self.get_list_option(seasons, 
                                                            season_sel, "Year")
                        client.season = client_season

                        while main_menu_exit:
                            main_sel = main_menu.show()
                            if main_sel == None:
                                break
                            elif main_sel == 3:
                                teams = client.competitions.get_competition_teams()
                                team_options = self.list_to_menu_options(teams, "Team")
                                team_menu = self.menu(team_options, "Teams")
                                team_sel = team_menu.show()
                                client_team = self.get_list_option(teams, 
                                                            team_sel, "ID")
                                client.team = client_team
                                data = client.teams.get_teams_matches()
                                print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
                                pause()
                            else:
                                self.gather_info(main_sel, client)
                                pause("\nPress any key to go back to "
                                    "the main menu...")

        print("Thanks for using Foot-Stats-CLI")

    def gather_info(self, main_sel, client):
        endpoint = self.get_main_option(main_sel)
            
        if endpoint == "comp_teams":
            data = client.competitions.get_competition_teams()
            print(tabulate(data, headers="keys", colalign=("left",)))
        elif endpoint == "comp_standings":
            data = client.competitions.get_competition_standings()
            print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
        elif endpoint == "comp_matches":
            data = client.competitions.get_competition_matches()
            print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
        elif endpoint == "teams_matches":
            data = client.teams.get_teams_matches()
            print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
        elif endpoint == "comp_goalscorers":
            data = client.competitions.get_competition_goalscorers()
            print(tabulate(data, headers="keys", colalign=("left",), tablefmt="rounded_outline"))
