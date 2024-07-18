# This file will intialise the API and be used to get all the endpoints
# i.e. APIClient.competitions.getCompetitionsList(), APIClient.matches.getMatchesList()
from .baseclient import BaseClient
from . import endpoints

class APIClient(BaseClient):
    pass