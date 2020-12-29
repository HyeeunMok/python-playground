import requests
from pprint import pprint
import config

BEARER_TOKEN = config.bearer_token
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/4cdfef89ce12dc8f3c15d928c00419e6/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        pprint(self.destination_data)
        return self.destination_data




