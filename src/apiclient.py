# This file will intialise the API and be used to get all the endpoints
# i.e. APIClient.competitions.getCompetitionsList(), APIClient.matches.getMatchesList()

from .baseclient import BaseClient
from . import endpoints

class APIClient(BaseClient):

    """
    The API Client that handles all the API operations. Accepts parameters
    for the API such as filters. 
    """
    
    def __init__(self, league, season):
        self.league = league
        self.season = season
        super().__init__(league, season)

        # Pass the instance of APIClient to the Competitions class. Provides
        # a reference of the instance allowing Competitions() to interact with 
        # it.
        self.competitions = endpoints.Competitions(self)
    