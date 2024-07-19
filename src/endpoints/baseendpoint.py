# This file will contain a request method to deal with getting the data and a process_response to deal with formatting the data
# It can be used by the endpoint classes i.e competitions.request() or competitions.process_request()
# Deals with the getting qand processing of the data
# It uses BaseClient as the parent class to get headers for the request

import requests
from ..baseclient import BaseClient


class BaseEndPoint(BaseClient):
    """
    BaseEndPoint() class handles all operations relating to fetching data. It
    uses the BaseClient as the parent to fetch the header and url to build the 
    request.
    """
    
    def __init__(self):
        super().__init__()

    def request(self, endpoint):
        response = requests.get(f'{self.url}{endpoint}', headers=self.header)
        return response
    
    @staticmethod
    def process_response(response, data):
        """
        Accepts response data and the name of the object we want data for 
        """
        return response.json().get(data)
        
