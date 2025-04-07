import requests

QUESTION_URL = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

response.raise_for_status()

responseData = response.json()

question_data = responseData["results"]