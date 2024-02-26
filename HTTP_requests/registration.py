import  requests
import dotenv
import os

dotenv.load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":os.getenv("PIXELA_TOKEN"),
    "username":"carlos2r",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)

