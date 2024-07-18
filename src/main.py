# The main file that deals with the overall running of the app.
# Instantiates a new APIClient to which we can call all endpoints

from .apiclient import APIClient

class Main():
    
    def __init__(self) -> None:
        print("Main")

        client = APIClient()
        client.competitions.getCompetitionList()