
class AppText():
    LEAGUE_ABOUT = ("\nLEAGUE MENU\nFooty Stats CLI has 5 League options to ")
    LEAGUE_MESSAGE = ("choose from\n\nSelect the LEAGUE you want to view "
                      "data for:\n")
    MAIN_ABOUT = ("\nMAIN MENU\nFooty Stats CLI has 5 main options to choose "
                  "from. Select your option below\n")
    MAIN_MESSAGE = ("\nCompetition: {comp}\n"
                    "Season: {season}\n")
    SEASON_ABOUT = ("\nSEASON MENU\nFooty Stats CLI shows up to 10 seasons "
                    "worth of historical data.\n")
    SEASON_MESSAGE = ("\nSelect the SEASON you wish to view data for:\n")
    TEAM_ABOUT = ("\nTEAM MENU\nBelow shows the full list of available teams\n")
    TEAM_MESSAGE = ("\nSelect a team to view their Fixtures/Results:\n")
    START_ABOUT = ("\nSTART MENU\nFooty Stats CLI is an application for all "
                    "football related data. Using the\nFootball-Data API to "
                    "gather data about Leagues, Fixtures/Results, Teams\nand "
                    "Goalscorers.\n\nNavigate the app using the keyboard. "
                    "[Up/Down] moves through menu options.\n[Enter] selects the "
                    "option. Click the Help option below for more"
                    "\ninformation\n")
    START_MESSAGE = ("\nSelect an option below:\n")
    LOGO = ("""
              ______            __           _____ __        __          ________    ____
             / ____/___  ____  / /___  __   / ___// /_____ _/ /______   / ____/ /   /  _/
            / /_  / __ \/ __ \/ __/ / / /   \__ \/ __/ __ `/ __/ ___/  / /   / /    / /  
           / __/ / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ /_/ / /_(__  )  / /___/ /____/ /   
          /_/    \____/\____/\__/\__, /   /____/\__/\__,_/\__/____/   \____/_____/___/   
                                /____/ 
            """)
    HELP_MESSAGE = ("\nFooty Stats CLI uses the keyboard to navigate menu "
                    "options. See the\ncheatsheet below on how to use Footy "
                    "Stats CLI:\n\n[UP/DOWN] Keyboard Arrows: Navigate menu "
                    "items. The cursor will cycle\nthrough the available items "
                    "if you reach the end of the list.\n\n[ENTER]: Clicking "
                    "enter on the keyboard will select the option and\neither "
                    "display the data you have chosen or progress to the next "
                    "menu.\n\n[Q/ESC]: Click [Q] or [ESC] on the keyboard to "
                    "either go back to the\nprevious menu or exit the program "
                    "depending on what menu screen\nyou are on. Clicking [Q] "
                    "or [ESC] on the Start Menu screen will exit\nthe program."
                    "\n\n[ANY KEY]: When data is displayed to a user "
                    "(just like\nit is now) a message will appear at the bottom "
                    "of the screen.\nPressing [ANY KEY] will being them back "
                    "to the previous menu.")
    ABOUT_MESSAGE = ("\nFooty Stats CLI is a command line interface application"
                     " built using Python.\nIt utilises the football-data.org "
                     "API [https://www.football-data.org/] to\nsupply all the "
                     "data.\n\nAvailable Resources:\nLeagues: Premier League,"
                     " Ligue 1, La Liga, Bundesliga, Serie A\nSeasons: From "
                     "2020 onwards.\nData: Teams, League Table"
                     ", Fixtures & Results, Top 10 Goalscorers\n\n"
                     "Github Repo: https://github.com/MarkClinton/"
                     "footy-stats-cli")
