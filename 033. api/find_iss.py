from time import sleep
import datetime as dt
import requests

LATITUDE = 37.384851
LONGITUDE = 127.123486

SUNSET_URL = "https://api.sunrise-sunset.org/json"
ISS_URL = "http://api.open-notify.org/iss-now.json"

while True:
    sleep(10)

    iss_response = requests.get(ISS_URL)
    iss_response.raise_for_status()
    iss_data = iss_response.json()["iss_position"]

    iss_latitude = float(iss_data["latitude"])
    iss_longitude = float(iss_data["longitude"])

    if abs(iss_longitude - LONGITUDE) < 5 and abs(iss_latitude - LATITUDE):

        parameters = {
            "lat": LATITUDE,
            "lng": LONGITUDE,
            "formatted": 0
        }

        sunset_response = requests.get(SUNSET_URL, params=parameters)
        sunset_response.raise_for_status()
        sunset_data = sunset_response.json()["results"]
        sunset = int(sunset_data["sunset"])

        now_hour = dt.datetime.now().hour

        if sunset < now_hour:
            print("You can see ISS")
        else:
            print("Sorry, You can't see ISS, Now is sunset yet.")
            print(f"ISS Position: Latitude - {iss_latitude}, Longitude - {iss_longitude}")
            print(f"Now Hour: {now_hour}, Sunset Hour: {sunset}")
    else:
        print("Sorry, You can't see ISS, ISS is so far.")
        print(f"ISS Position: Latitude - {iss_latitude}, Longitude - {iss_longitude}")



