# This is a class that will get the Team data
# Only deals with the info needed to call the team endpoint

from .baseendpoint import BaseEndPoint
from .endpointutil import EndpointUtil


class Teams(BaseEndPoint, EndpointUtil):
    """
    Teams() class handles fetching all Teams data. It inherits BaseEndPoint as
    the parent to call the neccessary request functions.
    """

    BASE_TEAMS_RESOURCE = "teams"

    def get_teams_matches(self) -> list:
        """ Get a list of all matches a team played in a given season """

        response = self.request(self.BASE_TEAMS_RESOURCE, "matches")
        return (
            self.clean_matches_list(self.process_response(response, "matches"))
        )
