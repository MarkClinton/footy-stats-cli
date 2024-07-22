# This is a class that will get the Team data 
# Only deals with the info needed to call the team endpoint

from .baseendpoint import BaseEndPoint

class Teams(BaseEndPoint):
    """
    Teams() class handles fetching all Teams data. It inherits BaseEndPoint as 
    the parent to call the neccessary request functions.
    """
    
    BASE_TEAMS_RESOURCE = "teams"

    def get_teams_matches(self):
        pass