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
        # pprint(data)
        self.destination_data = data["prices"]
        # pprint(self.destination_data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id  from sheet_data
    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)


