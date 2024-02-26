import requests
from create_graph import graph_config
from registration import user_params
from datetime import datetime

GRAPH_ID = graph_config["id"]
USERNAME = user_params["username"]
TOKEN = user_params["token"]

"""
REQUEST HEADER
"""
header = {
    "X-USER-TOKEN":TOKEN,
}

"""
REQUEST BODY
"""

now = datetime.now()
formatted_now = now.strftime("%Y%m%d")
json = {
    "date":formatted_now,
    "quantity":"76"
}


post_value_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=post_value_endpoint,json=json,headers=header)
print(response.text)