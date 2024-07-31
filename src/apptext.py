"""
AppText class holds all text items needed to populate menu screens.
"""
from blessed import Terminal

class AppText():
    """
    AppText class holds all text items needed to populate menu screens.
    """
    term = Terminal()

    LEAGUE_TITLE = (f"""
Select the league you want to view data for below:
                    """)
    LEAGUE_ABOUT = (f"""
LEAGUE MENU
Footy Stats CLI has 5 League options to choose from.
Click [Q/ESC] to go back to start menu.
                    """)

    MAIN_ABOUT = (f"""
MAIN MENU
Footy Stats CLI has 5 main options to choose from. 
Click [Q/ESC] to go back to season menu.
                """)
    MAIN_TITLE = (f"""
Select the option you want to view data for below:
                """)
    SEASON_ABOUT = (f"""
SEASON MENU
Footy Stats CLI shows up to 10 seasons worth of historical data.
Click [Q/ESC] to go back to league menu.
                    """)
    SEASON_TITLE = (f"""
Select the season you want to view data for below:
                    """)
    TEAM_ABOUT = (f"""
TEAM MENU
Below shows the full list of available teams.
Click [Q/ESC] to go back to main menu.
                """)
    TEAM_TITLE = (f"""
Select a team below to view their fixtures/results:
                """)
    START_ABOUT = (f"""
START MENU
Footy Stats CLI is an application for all football related data. Using the
Football-Data API to gather data about Leagues, Fixtures/Results, Teams
and Goalscorers.

Navigate the app using the keyboard. [Up/Down] moves through menu options.
[Enter] selects the option. Click the Help option below for more info.
Click [Q/ESC] to exit the app.
                """)
    START_TITLE = (f"""Select an option below:""")

    LOGO = (f"""{term.chartreuse3}
   ____        __         ______       __        _______   ____
  / ___/_ ___ / /___ __  / __/ /____ _/ /____   / ___/ /  /  _/
 / _// _ / _ / __/ // / _\ \/ __/ _ `/ __(_-<  / /__/ /___/ /  
/_/  \___\___\__/\_, / /___/\__/\_,_/\__/___/  \___/____/___/  
                /___/ {term.normal}""")

    HELP_MESSAGE = (f"""
Footy Stats CLI uses the keyboard to navigate menu options. See the
cheatsheet below on how to use Footy Stats CLI:

[UP/DOWN]: Navigate menu items.

[ENTER]: Select the option and either display 
the data you have chosen or progress to the next menu.

[Q/ESC]: Click [Q] or [ESC] on the keyboard to 
either go back to the previous menu or exit the program depending on what menu 
screen you are on. Clicking [Q] or [ESC] on the Start Menu screen will exit the 
program.

[ANY KEY]: Progress to the part of the app
                """)

    ABOUT_MESSAGE = (f"""
Footy Stats CLI is a command line interface application built using Python.
It utilises the football-data.org API [https://www.football-data.org/] to
supply all the data.

Available Resources:
Leagues: Premier League, Ligue 1, La Liga, Bundesliga, Serie A
Seasons: From 2020 onwards.
Data: Teams, League Table, Fixtures & Results, Top 10 Goalscorers

Github Repo: https://github.com/MarkClinton/footy-stats-cli""")
