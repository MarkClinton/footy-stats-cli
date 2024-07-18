# The main file that deals with the overall running of the app.
# Instantiates a new APIClient to which we can call all endpoints

from .apiclient import APIClient

class Main():
    
    def __init__(self) -> None:

        client = APIClient()
        print(client.sample_request())
