# This is a class that will get the competition data 
# Only deals with the info needed to call the competitions endpoint

from .baseendpoint import BaseEndPoint

class Competitions(BaseEndPoint):
    
    def getCompetitionList(self):
        print("getting competition list....")