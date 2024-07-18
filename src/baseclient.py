# This file will be used to get API Key, define request headers etc
# Basically anything needed to call the API

import requests

class BaseClient:
    """
    Base API Client that handles the neccessary functionality to call the API
    """

    BASE_URL = "https://api.football-data.org/"
    VERSION = "v4"

    def __init__(self):
        self.url = self.BASE_URL + self.VERSION
        

    def request_header(self):
        return {
            "X-Auth-Token": self.get_key()
        }

    def get_key():
        pass

