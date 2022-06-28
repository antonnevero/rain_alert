import requests
import os
from twilio.rest import Client

#You need to get your own sid and token from https://twilio.com/
account_sid = 'account_sid'
auth_token = 'auth_token'

parameters = {
    "lat": 47,
    "lon": 33,
    "appid": "appid", #You need to get your own appid from https://openweathermap.org/
    "exclude": "current,minutely,daily",
    "units": "metric"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data = response.json()
weather_list = data["hourly"][:12]
hourly_id = [id_weather["weather"][0]["id"] for id_weather in weather_list]

will_rain = False

for code in hourly_id:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today",
        from_='tel', # From twilio.com
        to='myTel' # Your phone number
    )

    print(message.status)
