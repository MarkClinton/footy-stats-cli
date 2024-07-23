# This file will be used to get API Key, define request headers etc
# Basically anything needed to call the API

import os
from dotenv import load_dotenv


class BaseClient:
    """
    Base API Client that handles the neccessary functionality to call the API.
    Holds common attrinbutes and methods to make requests.
    """
    SECRET_KEY_NAME = "FOOTBALL_DATA_API_KEY"
    BASE_URL = "https://api.football-data.org/"
    VERSION = "v4"

    def __init__(self, league: str=None, season: str=None, team: int=None):
        """
        Initialise the BaseClient with optional leage, season and team data.

        :param league: league name or identifier
        :param season: season year
        :param team: team identifier
        """
        # Protected attributes
        self._league = league 
        self._season = season
        self._team = team
        # Private attribute
        self.__key = self.load_key()

    @property
    def league(self) -> str:
        """ Get or set the league """
        return self._league
    
    @league.setter
    def league(self, league):
        self._league = league

    @property
    def season(self) -> str:
        """ Get or set the season """
        return self._season
    
    @season.setter
    def season(self, season):
        self._season = season

    @property
    def team(self) -> str:
        """ Get or set the team """
        return self._team
    
    @team.setter
    def team(self, team):
        self._team = team

    @property
    def url(self) -> str:
        return f'{self.BASE_URL}/{self.VERSION}/'
    
    @property
    def header(self) -> dict:
        """ Get the header """
        return {
            'X-Auth-Token': self.__key
        }

    def load_key(self) -> str:
        load_dotenv()
        return os.getenv(self.SECRET_KEY_NAME)
        # Should handle this better if the secret key is not found
