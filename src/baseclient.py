# This file will be used to get API Key, define request headers etc
# Basically anything needed to call the API

import requests
import os
from dotenv import load_dotenv

class BaseClient:
    """
    Base API Client that handles the neccessary functionality to call the API.
    """
    SECRET_KEY_NAME = "FOOTBALL_DATA_API_KEY"
    BASE_URL = "https://api.football-data.org/"
    VERSION = "v4"

    def __init__(self, league, season=None):
        self.url = f'{self.BASE_URL}/{self.VERSION}/'
        self.key = self.load_key()
        self.header = self.request_header()
        self.league = league
        self.season = season
        self.params = {'season': self.season}

    def request_header(self):
        return {
            'X-Auth-Token': self.key
        }

    def load_key(self):
        load_dotenv()
        return os.getenv(self.SECRET_KEY_NAME)
        # Should handle this better if the secret key is not found


