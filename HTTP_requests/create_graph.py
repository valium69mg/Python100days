import requests
from registration import user_params 

USERNAME = user_params["username"]
TOKEN = user_params["token"]

pixela_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Gym Graph",
    "unit":"Kg",
    "type":"float",
    "color":"momiji"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

response = requests.post(url=pixela_graph_endpoint,json=graph_config,headers=headers)
print(response)
