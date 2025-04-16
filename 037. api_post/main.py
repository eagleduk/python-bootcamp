import requests

TOKEN="awerfjawnghbowrei"
USERNAME="pythonstudy123"
GRAPHID="graph1"

pixela_base = "https://pixe.la"

TOKENHEADERS = {
    "X-USER-TOKEN": TOKEN
}

create_user_endpoint = f"{pixela_base}/v1/users"
create_user_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# create_user_response = requests.post(url=create_user_endpoint, json=create_user_body)
# print("Create User Response: " + create_user_response.text)

create_graph_endpoint = f"{pixela_base}/v1/users/{USERNAME}/graphs"
create_graph_body = {
    "id": GRAPHID,
    "name": "Python Study",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}

# create_graph_response = requests.post(url=create_graph_endpoint, json=create_graph_body, headers=TOKENHEADERS)
# print("Create Graph Response: " + create_graph_response.text)

post_graph_pixel_endpoint = f"{create_graph_endpoint}/{GRAPHID}"
post_graph_pixel_body = {
    "date": "20250416",
    "quantity": "2.3"
}
post_graph_pixel_response = requests.post(url=post_graph_pixel_endpoint, json=post_graph_pixel_body, headers=TOKENHEADERS)
print("Post Graph Pixel Response: " + post_graph_pixel_response.text)