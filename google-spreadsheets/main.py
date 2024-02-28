import os
import dotenv
import requests
import datetime as dt

dotenv.load_dotenv()

"""
CONSTANTS FOR THE APP
"""
API_KEY_NUTRITIONIX = os.getenv("API_KEY")
APP_ID_NUTRITIONIX = os.getenv("APP_ID")
API_HOST_DOMAIN = "https://trackapi.nutritionix.com"
API_ENDPOINT = "/v2/natural/exercise"
header = {
    "x-app-id":APP_ID_NUTRITIONIX,
    "x-app-key":API_KEY_NUTRITIONIX
}
WORKOUTS_ENDPOINT = "https://api.sheety.co/fbfbd5d717d9ebe861b7db1757ba3cfe/myWorkouts/workouts"

"""
FUNCTIONS
"""
def ask_for_workout():
    query = input("Register your workout: ")
    body = {
    "query":query
    }
    return body



def get_workout_info(json):
    response = requests.post(url=API_HOST_DOMAIN+API_ENDPOINT,json=json,headers=header)
    response.raise_for_status()
    calories = response.json()["exercises"][0]["nf_calories"]
    exercise = response.json()["exercises"][0]["name"]
    duration = response.json()["exercises"][0]["duration_min"]
    dict = {
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }
    return dict

def get_datetime():
    now = dt.datetime.now()
    now_date = now.strftime("%d/%m/%Y")
    now_time = now.strftime("%H:%M:%S")
    return now_time,now_date

body = ask_for_workout()
dict = get_workout_info(json=body)
time,date = get_datetime()
dict["time"] = time
dict["date"] = date
sheet_inputs = {
    "workout": dict
}

response = requests.post(url=WORKOUTS_ENDPOINT,json=sheet_inputs)
