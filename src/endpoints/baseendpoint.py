# This file will contain a request method to deal with getting the data and a process_response to deal with formatting the data
# It can be used by the endpoint classes i.e competitions.request() or competitions.process_request()
# Deals with the getting qand processing of the data
# It uses BaseClient as the parent class to get headers for the request

import requests
from ..baseclient import BaseClient


class BaseEndPoint:
    """
    BaseEndPoint() class handles all operations relating to fetching data. It
    uses the BaseClient as the parent to fetch the header and url to build the 
    request.
    """
    
    def __init__(self, parent: BaseClient):
        # When APIClient class creates an instanse of BaseEndPoint (Competitions)
        # it passes an instance of itself and we set self.client to the instance
        # of BaseClient 
        self.client = parent

    def request(self, resource, subresource=None):
        if(subresource):
            # uri = f'{self.client.url}{resource}/{self.client.league}/{subresource}'
            uri = f'{self.client.url}{resource}/{subresource}'
        else:
            uri = (f'{self.client.url}{resource}/{self.client.league}')

        response = requests.get(uri, headers=self.client.header, params=self.client.params)
        return response
    
    @staticmethod
    def process_response(response, data):
        """
        Accepts response data and the name we want data for 
        """
        return response.json().get(data)
        
