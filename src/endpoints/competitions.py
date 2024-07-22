# This is a class that will get the competition data 
# Only deals with the info needed to call the competitions endpoint

from datetime import datetime
from .baseendpoint import BaseEndPoint

class Competitions(BaseEndPoint):
    """
    Competitions() class handles fetching all Competition data. Uses 
    BaseEndPoint as the parent to call the neccessary request functions.
    """

    BASE_COMPETITIONS_RESOURCE = "competitions"

    def get_competitions_list(self):
        response = self.request(self.BASE_COMPETITIONS_RESOURCE)
        return(self.process_response(response, "competitions"))
    
    def get_competition_seasons(self):
        response = self.request(self.BASE_COMPETITIONS_RESOURCE)
        return(self.clean_season_list(self.process_response(response, "seasons")))
    
    def get_competition_teams(self):
        response = self.request(self.BASE_COMPETITIONS_RESOURCE, "teams")
        return(self.clean_team_list(self.process_response(response, "teams")))
    
    def get_competition_standings(self):
        response = self.request(self.BASE_COMPETITIONS_RESOURCE, "standings")
        return(self.clean_standings_list(self.process_response(response, "standings")))
    
    def get_competition_goalscorers(self):
        response = self.request(self.BASE_COMPETITIONS_RESOURCE, "scorers")
        return(self.clean_scorers_list(self.process_response(response, "scorers")))
    
    @staticmethod
    def clean_scorers_list(scorers_data):
        scorers = []

        for s in scorers_data:
            scorer = {
                "Name": s["player"]["name"],
                "Team": s["team"]["name"],
                "Matches Played": s["playedMatches"],
                "Goals": s["goals"],
                "Assists": s["assists"],
                "Penalties": s["penalties"]
            }
            scorers.append(scorer)
        return scorers

    @staticmethod
    def clean_standings_list(standings_data):
        standings = []

        for s in standings_data[0]["table"]:
            standing = {
                "Team": s["team"]["name"],
                "Games Played": s["playedGames"],
                "Won": s["won"],
                "Draw": s["draw"],
                "Lost": s["lost"],
                "Points": s["points"],
                "Goals For": s["goalsFor"],
                "Goals Against": s["goalsAgainst"],
                "Goal Difference": s["goalDifference"]
            }
            standings.append(standing)
        # Sort list of dict items in descending order with respect to Points value
        list(sorted(standings, key=lambda x: x['Points'], reverse=True))
        return standings

    @staticmethod
    def clean_team_list(team_data):
        teams = []

        for t in team_data:
            team = {
                "Team": t["name"],
                "Founded": t["founded"],
                "Stadium": t["venue"],
                "Current Manager": t["coach"]["name"]
            }
            teams.append(team)

        return teams

    @staticmethod
    def clean_season_list(season_data):
        seasons = []
        amount = len(season_data) if len(season_data) < 10 else 10

        for i in range(amount):
            start_year = datetime.strptime(season_data[i]["startDate"], '%Y-%m-%d').year
            end_year =  datetime.strptime(season_data[i]["endDate"], '%Y-%m-%d').year
            season = {
                "Year": start_year, 
                "Name": f'{start_year}/{end_year}'
            }
            seasons.append(season)
            
        return seasons
