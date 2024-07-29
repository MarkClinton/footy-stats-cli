"""
This file contains a request method to deal with getting the data and a
process_response to deal with formatting the data. It can be used by the
endpoint classes i.e competitions.request() or competitions.process_request()
Deals with the getting and processing of the data
It uses BaseClient as the parent class to get headers for the request
"""

import requests
from ..baseclient import BaseClient


class BaseEndPoint:
    """
    BaseEndPoint() class handles all operations relating to fetching data. It
    uses the BaseClient as the parent to fetch the header and url to build the
    request.
    """

    def __init__(self, parent: BaseClient):
        """
        Initialize the BaseEndPoint class with the BaseClient as an attribute

        :param parent: BaseClient class
        """
        self.client = parent
        # When APIClient class creates an instanse of BaseEndPoint
        # (Competitions) it passes an instance of itself and we set self.client
        # to the instance of BaseClient

    def request(self, resource: str,
                subresource: str = None) -> requests.Response:
        """
        Request and fetch data from the endpoint

        :param resource: The endpoint to fetch data from
        :param subresource: the name of the object in the json response
        """
        uri, params = self.url_builder(resource, subresource)
        response = requests.get(uri, headers=self.client.header, params=params)
        return response

    def url_builder(self, resource: str, subresource: str) -> list:
        """
        Dynamically build the request needed to fetch data

        :param resource: The endpoint to fetch data from
        :param subresource: the name of the object in the json response
        """

        params = {}
        params["season"] = self.client.season
        match(resource):
            case "teams":
                uri = f'{self.client.url}{resource}/{self.client.team}/'
                '{subresource}'
                params["competition"] = self.client.league
            case "competitions":
                if (subresource):
                    uri = f'{self.client.url}{resource}/{self.client.league}/'
                    '{subresource}'
                else:
                    uri = f'{self.client.url}{resource}/{self.client.league}'
        return [uri, params]

    @staticmethod
    def process_response(response: requests.Response, data: str) -> list:
        """
        Get the JSON() repsonse data

        :param response: The response from the request
        :param data: the object in the JSON
        """

        return response.json().get(data)
