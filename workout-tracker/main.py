import requests
import config
from datetime import datetime

GENDER = config.gender
WEIGHT_KG = config.weight_kg
HEIGHT_CM = config.weight_kg
AGE = config.age

#Nutritionix
APP_ID = config.application_id
APP_KEY = config.application_key

#Sheety
BEARER_TOKEN = config.bearer_token

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/4cdfef89ce12dc8f3c15d928c00419e6/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_header = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_header)
    print(sheet_response.text)