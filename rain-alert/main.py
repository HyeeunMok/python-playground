import requests
from twilio.rest import Client
import config

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = config.OWM_api_key

#Twilio
account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token
twilio_phone_number = config.twilio_phone_num
recipient_phone_number = config.recipient_phone_num

#Toronto
MY_LAT = -5.653225
MY_LONG = 160.383186

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=twilio_phone_number,
        to=recipient_phone_number
    )

    print(message.status)


# # For pythonanywhere.com
#
# import requests
# import os
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
#
# OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = os.environ.get("OWM_API_KEY")
#
# account_sid = "AC3747096d6428d3cddbfe034e4b96bbeb"
# auth_token = os.environ.get("AUTH_TOKEN")
#
#
# #Toronto
# MY_LAT = -5.653225
# MY_LONG = 160.383186
#
#
# weather_params = {
#     "lat": MY_LAT,
#     "lon": MY_LONG,
#     "appid": api_key,
#     "exclude": "current,minutely,daily"
# }
#
# response = requests.get(OWM_endpoint, params=weather_params)
# response.raise_for_status()
# weather_data = response.json()
# weather_slice = weather_data["hourly"][:12]
#
# will_rain = False
#
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#
#     client = Client(account_sid, auth_token, http_client=proxy_client)
#     message = client.messages \
#         .create(
#         body="It's going to rain today. Remember to bring an ☔️",
#         from_="+****",
#         to="+*****"
#     )
#
#     print(message.status)


