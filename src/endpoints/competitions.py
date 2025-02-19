"""
This is a class that will get the competition data
Only deals with the info needed to call the competitions endpoint
"""
from datetime import datetime
from .baseendpoint import BaseEndPoint
from .endpointutil import EndpointUtil


class Competitions(BaseEndPoint, EndpointUtil):
    """
    Competitions() class handles fetching all Competition data. Uses
    BaseEndPoint as the parent to call the neccessary request functions.
    """

    BASE_COMPETITIONS_RESOURCE = "competitions"

    def get_competitions_list(self):
        """ Get a list of competitions availables """
        response = self.request(self.BASE_COMPETITIONS_RESOURCE)
        return (
            self.process_response(response, "competitions")
        )

    def get_competition_seasons(self) -> list:
        """  Get a list of seasons available for a competition """
        response = self.request(self.BASE_COMPETITIONS_RESOURCE)
        if response.status_code != 200:
            print("Oops sorry, " + response.json()["message"])
            return False
        else:
            return (
                self.clean_season_list(
                    self.process_response(response, "seasons")
                )
            )

    def get_competition_teams(self) -> list:
        """ Get a list of teams that take part in a competition """
        response = self.request(self.BASE_COMPETITIONS_RESOURCE, "teams")
        if response.status_code != 200:
            return [response.json()]
        else:
            return (
                self.clean_team_list(self.process_response(response, "teams"))
            )

    def get_competition_standings(self) -> list:
        """ Get the league table for a competition """
        response = self.request(self.BASE_COMPETITIONS_RESOURCE, "standings")
        if response.status_code != 200:
            return [response.json()]
        else:
            return (
                self.clean_standings_list(
                    self.process_response(response, "standings")
                )
            )

    def get_list_teams(self) -> list:
        """ Get a list of dicts of teams and their ID's """
        response = self.request(self.BASE_COMPETITIONS_RESOURCE, "teams")
        if response.status_code != 200:
            print("Oops sorry, " + response.json()["message"])
            return False
        else:
            return (
                self.get_team_ids(self.process_response(response, "teams"))
            )

    def get_competition_goalscorers(self) -> list:
        """ Get the top 10 goalscorers for a season """
        response = self.request(self.BASE_COMPETITIONS_RESOURCE, "scorers")
        if response.status_code != 200:
            return [response.json()]
        else:
            return (
                self.clean_scorers_list(
                    self.process_response(response, "scorers")
                )
            )

    def get_competition_matches(self) -> list:
        """ Get all matches for a competition for a certain season """
        response = self.request(self.BASE_COMPETITIONS_RESOURCE, "matches")
        if response.status_code != 200:
            return [response.json()]
        else:
            return (
                self.clean_matches_list(
                    self.process_response(response, "matches")
                )
            )

    @staticmethod
    def clean_scorers_list(scorers_data: list) -> list:
        """
        Returns a list of dicts with goalscorer data

        :params scorers_data: list of  goalscorers
        """
        scorers = []

        for s in scorers_data:
            scorer = {
                "Name": s["player"]["name"],
                "Team": s["team"]["name"],
                "Matches Played": s["playedMatches"],
                "Goals": s["goals"]
            }
            scorers.append(scorer)
        return scorers

    @staticmethod
    def clean_standings_list(standings_data: list) -> list:
        """
        Returns a list of dicts with league table data

        :params standings_data: list of teams with league table data
        """
        standings = []

        for s in standings_data[0]["table"]:
            standing = {
                "Team": s["team"]["name"],
                "Played": s["playedGames"],
                "Won": s["won"],
                "Draw": s["draw"],
                "Lost": s["lost"],
                "Points": s["points"]
            }
            standings.append(standing)
        # Sort list of dict items in descending order by Points
        sorted(standings, key=lambda x: x['Points'], reverse=True)
        return standings

    @staticmethod
    def clean_team_list(team_data: list) -> list:
        """
        Returns a list of dicts with team data

        :params team_data: list of teams with team data
        """
        teams = []

        for t in team_data:
            team = {
                "Team": t["name"],
                "Founded": t["founded"],
                "Stadium": t["venue"]
            }
            teams.append(team)
        return teams

    @staticmethod
    def get_team_ids(team_data: list) -> list:
        """
        Returns a list of dicts with team data

        :params team_data: list of teams with team data
        """
        teams = []

        for t in team_data:
            team = {
                "ID": t["id"],
                "Team": t["name"]
            }
            teams.append(team)
        return teams

    @staticmethod
    def clean_season_list(season_data: list) -> list:
        """
        Returns a list of dicts with season data

        :params season_data: list of seasons with season data
        """
        seasons = []
        # Due to limitations with the API we can only offer seasons
        # from 2020 onward.
        amount = len(season_data) if len(season_data) < 5 else 5

        for i in range(amount):
            start_year = datetime.strptime(
                    season_data[i]["startDate"], '%Y-%m-%d'
                ).year
            end_year = datetime.strptime(
                    season_data[i]["endDate"], '%Y-%m-%d'
                ).year
            season = {
                "Year": start_year,
                "Name": f'{start_year}/{end_year}'
            }
            seasons.append(season)
        return seasons
