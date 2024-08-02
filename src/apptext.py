"""
AppText class holds all text items needed to populate menu screens.
"""
from blessed import Terminal


class AppText():
    """
    AppText class holds all text items needed to populate menu screens.
    """
    term = Terminal()

    PROCESSING = f'{term.blink("Processing Request...")}'
    ERROR_INPUT = (
        f'{term.red}Sorry, thats not a valid action. '
        f'Please try again{term.normal}'
    )
    Q = f'{term.bold_yellow}[Q]{term.normal}'
    GREEN = f'\n{term.bold_lightgreen}'
    NORMAL = f'{term.normal}\n'
    UP_DOWN = f'{term.bold_yellow}[Up/Down]{term.normal}'
    ENTER = f'{term.bold_yellow}[Enter]{term.normal}'
    ESC = f'{term.bold_yellow}[Q/ESC]{term.normal}'
    MAIN_TITLE = "Select the option you want to view data for below:\n"
    LEAGUE_TITLE = "Select the league you want to view data for below:\n"
    SEASON_TITLE = "Select the season you want to view data for below:\n"
    TEAM_TITLE = "Select a team below to view their fixtures/results:\n"
    START_TITLE = "Select an option below:\n"

    LEAGUE_ABOUT = f"""
Footy Stats CLI has 5 League options to choose from.

Click {ESC} to go back to start menu.
                    """

    MAIN_ABOUT = f"""
Footy Stats CLI has 5 main options to choose from.

Click {ESC} to go back to season menu.
                """

    SEASON_ABOUT = f"""
Footy Stats CLI shows up to 5 seasons worth of historical data.

Click {ESC} to go back to league menu.
                    """

    TEAM_ABOUT = f"""
Click {ESC} to go back to main menu.
                """

    START_ABOUT = f"""
Footy Stats CLI is an application for all football related data. Using the
Football-Data API to gather data about Leagues, Fixtures/Results, Teams
and Goalscorers.

Navigate the app using the keyboard.
{UP_DOWN} moves through menu options. {ENTER} selects the option.
Click the Help option below for more info.

Click {ESC}to exit the app.
                """

    HELP_MESSAGE = f"""
Footy Stats CLI uses the keyboard to navigate menu options. See the
cheatsheet below on how to use Footy Stats CLI:

{UP_DOWN}: Navigate menu items. Menu's are cyclical. Pressing down on the
last menu item will navigate to the first menu item. 
{ESC}: On menu screens, pressing either Q or ESC will navigate back to the 
previous menu screen. Allowing you to choose different criteria to display, 
e.g. different Leagues or different Seasons
{ENTER}: The Enter key is used to select a menu item. Once selected the program
will either show a menu screen or display data depending where you are in the 
program. Enter can also be used when prompted, the app will ask you to click 
Enter to progress.
{Q}: Q, on its own, when viewing data from the main menu will navigate back to 
the main menu. This option is used when the data displayed is paginated. 
                """

    ABOUT_MESSAGE = f"""
Footy Stats CLI is a command line interface application built using Python.
It utilises the API from {term.link('https://www.football-data.org/',
'football-data.org')} to supply all the data.
{term.link('https://github.com/MarkClinton/footy-stats-cli', 'Github Repo')}

{term.underline_bold}Available Resources:{term.normal}
Leagues: Premier League, Ligue 1, La Liga, Bundesliga, Serie A
Seasons: From 2020 onwards.
Data: Teams, League Table, Fixtures & Results, Top 10 Goalscorers
                    """

    LOGO = f"""{term.bold_lightgreen}
   ____        __         ______       __        _______   ____
  / ___/_ ___ / /___ __  / __/ /____ _/ /____   / ___/ /  /  _/
 / _// _ / _ / __/ // / _\ \/ __/ _ `/ __(_-<  / /__/ /___/ /  
/_/  \___\___\__/\_, / /___/\__/\_,_/\__/___/  \___/____/___/ 
                /___/ {term.normal}
            """
