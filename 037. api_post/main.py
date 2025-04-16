import requests

TOKEN="awerfjawnghbowrei"
USERNAME="pythonstudy123"
GRAPHID="graph1"

pixela_base = "https://pixe.la"

create_user_endpoint = f"{pixela_base}/v1/users"
create_user_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

create_user_response = requests.post(url=create_user_endpoint, json=create_user_body)
print("Create User Response: " + create_user_response.text)