# This file will be used to get API Key, define request headers etc
# Basically anything needed to call the API

import requests

class BaseClient:
    """
    Base API Client that handles the neccessary functionality to call the API
    """

    def __init__(self):
        pass
        # Declare anything needed for the API to fundtion e.g locale, headers etc

    def request_header(self):
        return {
            "X-Auth-Token": "API_Token"
        }