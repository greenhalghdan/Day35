import os
import requests
from twilio.rest import Client

api_key = os.environ.get("api_key")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

url = "https://api.openweathermap.org/data/3.0/onecall?"

params = {
    "lat": 52.056736,
    "lon": 1.148220,
    "appid": api_key,
    "exclude": "daily,minutely,current"
}

response = requests.get(url=url, params=params)
response.raise_for_status()

weather_data = response.json()
weather = []
hour = 0
umbrella = False
# while hour <= 12:
#     #code = weather_data["hourly"][hour]["weather"][0]["id"]

#     weather.append(code)
#     hour += 1
# for code in weather:
#     if code < 700:
#         umbrella = True

#     #Slice:

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        umbrella = True


if umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It going to rain today!",
        from_='+447723613314',
        to='+############'
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It not going to rain today!",
        from_='+447723613314',
        to='+#########'
    )
    print(message.status)