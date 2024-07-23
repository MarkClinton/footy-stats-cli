"""
This file will intialise the API and be used to get all the endpoints
i.e. APIClient.competitions.getCompetitionsList(), 
APIClient.matches.getMatchesList()
"""

from .baseclient import BaseClient
from . import endpoints


class APIClient(BaseClient):

    """
    The API Client that handles all the API operations. Accepts parameters
    for the API such as league, season and team. 
    """
    
    def __init__(self, league: str, season: str=None, team: int=None):
        """
        Initialize the APIClient with a league to start. Optional for season and
        team.

        :param league: league name or identifier
        :param season: season year
        :param team: team identifier
        """

        super().__init__(league, season, team)
        self.competitions = endpoints.Competitions(self)
        self.teams = endpoints.Teams(self)
        # Pass the instance of APIClient to the Competitions class. Provides
        # a reference of the instance allowing Competitions() to interact with 
        # it.
