import requests

QUESTION_URL = "https://opentdb.com/api.php"

parameter = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(QUESTION_URL, params=parameter)

response.raise_for_status()

responseData = response.json()

question_data = responseData["results"]