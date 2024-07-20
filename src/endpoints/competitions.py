# This is a class that will get the competition data 
# Only deals with the info needed to call the competitions endpoint

from datetime import datetime
from .baseendpoint import BaseEndPoint

class Competitions(BaseEndPoint):
    """
    Competitions() class handles fetching all Competition data. Uses 
    BaseEndPoint as the parent to call the neccessary request functions.
    """

    BASE_COMPETITIONS_ENDPOINT = "/competitions/"

    def get_competitions_list(self):
        response = self.request(self.BASE_COMPETITIONS_ENDPOINT)
        return(self.process_response(response, "competitions"))
    
    def get_competition_seasons(self):
        response = self.request(self.BASE_COMPETITIONS_ENDPOINT)
        return(self.clean_season_list(self.process_response(response, "seasons")))
        
    @staticmethod
    def clean_season_list(season_data):
        seasons = []
        amount = len(season_data) if len(season_data) < 10 else 10

        for i in range(amount):
            start_year = datetime.strptime(season_data[i]["startDate"], '%Y-%m-%d').year
            end_year =  datetime.strptime(season_data[i]["endDate"], '%Y-%m-%d').year
            seasons.append({'year': start_year, 'name': f'{start_year}/{end_year}'})
            
        return seasons
