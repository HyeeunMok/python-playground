import requests
import config
from datetime import datetime

TOKEN = config.token
USERNAME = config.username
GRAPH_ID = "graph1"


PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## CREATE USER - POST
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

## CREATE GRAPH - POST
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

## UPDATE GRAPH - PUT
GRAPH_UPDATE_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

graph_update_params = {
    "timezone": "America/Toronto"
}

# response = requests.put(url=GRAPH_UPDATE_ENDPOINT, json=graph_update_params, headers=headers)
# print(response.text)

## PIXEL CREATION - POST
PIXEL_CREATION_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")

pixel_params = {
    "date": formatted_today,
    "quantity": input("How many kilometers did you run today? ")
}
# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_params, headers=headers)
# print(response.text)
print(PIXEL_CREATION_ENDPOINT, formatted_today)


update_date = datetime(year=2020, month=12, day=25)
formatted_update_date = update_date.strftime("%Y%m%d")

PIXEL_UPDATE_ENDPOINT = f"{PIXEL_CREATION_ENDPOINT}/{formatted_update_date}"

pixel_update_params = {
    "quantity": "5"
}

## PUT - Update
# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=pixel_update_params, headers=headers)
# print(response.text)

PIXEL_DELETE_ENDPOINT = f"{PIXEL_CREATION_ENDPOINT}/{formatted_update_date}"

## DELETE
# response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
# print(response.text)