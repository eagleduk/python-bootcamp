import requests
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

OWM_URL = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_APPKEY")

OWM_PARAMS = {
    "lat": 37.28,
    "lon": 132.3,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_URL, params=OWM_PARAMS)
response.raise_for_status()
responseData = response.json()
daily_list = (responseData["list"][1:])

rainy = False

for daily_info in daily_list:
    weather_list = daily_info["weather"]
    for weather in weather_list:
        weather_code = (weather["id"])
        if rainy is False and weather_code < 700:
            rainy = True

if rainy:
    print("Bring an Umbrella")