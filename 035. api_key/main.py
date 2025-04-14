import requests

OWM_URL = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""

OWM_PARAMS = {
    "lat": 37.28,
    "lon": 132.3,
    "appid": api_key,
    "cnt": 2
}

response = requests.get(OWM_URL, params=OWM_PARAMS)
response.raise_for_status()
responseData = response.json()
daily_list = (responseData["list"][:-1])

for daily_info in daily_list:
    weather_list = daily_info["weather"]
    for weather in weather_list:
        weather_code = (weather["id"])
        if weather_code < 700:
            print("Bring an Umbrella")