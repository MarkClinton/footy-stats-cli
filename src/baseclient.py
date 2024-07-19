# This file will be used to get API Key, define request headers etc
# Basically anything needed to call the API

import requests
import io

class BaseClient:
    """
    Base API Client that handles the neccessary functionality to call the API.
    """

    BASE_URL = "https://api.football-data.org/"
    VERSION = "/v4"

    def __init__(self):
        self.url = self.BASE_URL + self.VERSION
        self.key = self.load_key()
        self.header = self.request_header()
        

    def request_header(self):
        return {
            'X-Auth-Token': self.key
        }

    def load_key(self):
        path = ".env.default"
        try:
            with io.open(path) as stream:
                for line in stream:
                    key = line.split('=')
                    return key[1].strip()
        except IOError as e:
            print(e)

    def sample_request(self):
        r = requests.get(f'{self.url}/competitions/PL/', headers=self.header)
        return r


