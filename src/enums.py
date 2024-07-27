from enum import Enum

class Menu(Enum):
    LEAGUE_ABOUT = ("\nFooty Stats CLI is an application for all football "
            "related data. Using the\nFootball-Data API to gather data about "
            "Leagues, Fixtures/Results, Teams\nand Goalscorers.\n"
            "\nTo navigate the app on the keyboard. [Up/Down] on moves\nthrough"
            " menu options. [Enter] selects the option. [Q/ESC] navigates to\n"
            "the previous menu or quits the app.\n")
    LEAGUE_MESSAGE = ("\nTo get started, select the LEAGUE you want to view " 
            "data for:\n")
    MAIN_ABOUT = ("\nFooty Stats CLI has 5 main options to choose from. "
                    "Select your option below\n")
    MAIN_MESSAGE = ("\nCompetition: {comp}\n"
                    "Season: {season}\n")
    SEASON_ABOUT = ("\nFooty Stats CLI shows up to 10 seasons worth of"
                    " historical data.\n")
    SEASON_MESSAGE = ("\nSelect the SEASON you wish to view data for:\n")
    TEAM_ABOUT = ("\nBelow shows the full list of available teams\n")
    TEAM_MESSAGE = ("\nSelect a team to view their Fixtures/Results:\n")
    LOGO = """
              ______            __           _____ __        __          ________    ____
             / ____/___  ____  / /___  __   / ___// /_____ _/ /______   / ____/ /   /  _/
            / /_  / __ \/ __ \/ __/ / / /   \__ \/ __/ __ `/ __/ ___/  / /   / /    / /  
           / __/ / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ /_/ / /_(__  )  / /___/ /____/ /   
          /_/    \____/\____/\__/\__, /   /____/\__/\__,_/\__/____/   \____/_____/___/   
                                /____/                                                                                                
        """