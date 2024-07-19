# This is a class that will get the competition data 
# Only deals with the info needed to call the competitions endpoint

from .baseendpoint import BaseEndPoint

class Competitions(BaseEndPoint):
    """
    Competitions() class handles fetching all Competition data. Uses 
    BaseEndPoint as the parent to call the neccessary request functions.
    """

    COMPETITIONS_ENDPOINT = "/competitions"

    def getCompetitionsList(self):
        response = self.request(self.COMPETITIONS_ENDPOINT)
        self.process_response(response, "competitions")