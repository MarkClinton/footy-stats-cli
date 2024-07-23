# This file will be used to get API Key, define request headers etc
# Basically anything needed to call the API

import os
from dotenv import load_dotenv

class BaseClient:
    """
    Base API Client that handles the neccessary functionality to call the API.
    """
    SECRET_KEY_NAME = "FOOTBALL_DATA_API_KEY"
    BASE_URL = "https://api.football-data.org/"
    VERSION = "v4"

    def __init__(self, league=None, season=None, team=None):
        self._league = league
        self._season = season
        self._team = team

    @property
    def league(self):
        return self._league
    
    @league.setter
    def league(self, league):
        self._league = league

    @property
    def season(self):
        return self._season
    
    @season.setter
    def season(self, season):
        self._season = season

    @property
    def team(self):
        return self._team
    
    @team.setter
    def team(self, team):
        self._team = team

    @property
    def url(self):
        return f'{self.BASE_URL}/{self.VERSION}/'
    
    @property
    def key(self):
        return self.load_key()
    
    @property
    def header(self):
        return {
            'X-Auth-Token': self.key
        }

    def load_key(self):
        load_dotenv()
        return os.getenv(self.SECRET_KEY_NAME)
        # Should handle this better if the secret key is not found


