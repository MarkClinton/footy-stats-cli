# This file will intialise the API and be used to get all the endpoints
# i.e. APIClient.competitions.getCompetitionsList(), APIClient.matches.getMatchesList()

from .baseclient import BaseClient
from . import endpoints

class APIClient(BaseClient):

    """
    The API Client that handles all the API operations. Accepts parameters
    for the API such as filters. 
    """
    
    def __init__(self):
        super().__init__()

        self.competitions = endpoints.Competitions()