# This is a class that will get the Team data 
# Only deals with the info needed to call the team endpoint

from datetime import datetime
from .baseendpoint import BaseEndPoint

class Teams(BaseEndPoint):
    """
    Teams() class handles fetching all Teams data. It inherits BaseEndPoint as 
    the parent to call the neccessary request functions.
    """
    
    BASE_TEAMS_RESOURCE = "teams"

    def get_teams_matches(self):
        response = self.request(self.BASE_TEAMS_RESOURCE, "matches")
        return(self.clean_matches_list(self.process_response(response, "matches")))
        
    @staticmethod
    def clean_matches_list(match_data):
        matches = []

        for m in match_data:
            home_score = m["score"]["fullTime"]["home"]
            away_score = m["score"]["fullTime"]["away"]
            result = f'{home_score}-{away_score}'

            format_date = datetime.strptime(m["utcDate"], '%Y-%m-%dT%H:%M:%SZ')
            match_date = f'{format_date.day}/{format_date.month}/{format_date.year}'
            winner = m["score"]["winner"].replace('_TEAM','')
            
            match = {
                "Date": match_date,
                "Home": m["homeTeam"]["name"],
                "Away": m["awayTeam"]["name"],
                "Winner": winner,
                "Result": result
            }
            matches.append(match)
        return matches