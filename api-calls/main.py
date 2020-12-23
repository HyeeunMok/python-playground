import requests
from datetime import datetime
from dateutil.parser import isoparse
import time as t


MY_LAT = 43.653225
MY_LONG = -79.383186

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


def datetime_from_utc_to_local(utc_datetime):
    now_time = t.time()
    offset = datetime.fromtimestamp(now_time) - datetime.utcfromtimestamp(now_time)
    return utc_datetime + offset


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = isoparse(data["results"]["sunrise"])
sunrise = datetime_from_utc_to_local(sunrise).hour
sunset = isoparse(data["results"]["sunset"])
sunset = datetime_from_utc_to_local(sunset).hour

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)



#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)
#
# print(iss_position)