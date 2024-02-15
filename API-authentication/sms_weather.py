import os
from dotenv import load_dotenv
import requests

load_dotenv()

endpoint = "https://api.openweathermap.org/data/2.5/weather"
weather_parameters =  {
    "lat":20.639598356132968,
    "lon":-100.3478781548616,
    "appid": os.getenv('API_KEY'),
    "units":"metric"
}


"""
MANAGE THE REQUEST TO THE API 
"""
response = requests.get(endpoint,params=weather_parameters)
# RAISE EXCEPTION FOR EVERY ERROR CODE 
response.raise_for_status()
# IF ALL GOOD THEN SAVE THE JSON RESPONSE IN A VARIABLE
res = response.json()
# DECONSTRUCTION OF THE JSON FILE INTO VARIABLES WE CAN WORK WITH
main_weather = res['weather'][0]['main']
id_weather = res['weather'][0]['id']
current_temperature = res['main']['temp']
min_temperature = res['main']['temp_min']
max_temperature = res['main']['temp_max']
humidity = res['main']['humidity']

"""
WE WILL SEND THE WEATHER INFO THROUGH A TEXT MESSAGE 
"""
umbrella = None
if (id_weather < 800):
    umbrella = "Yes"
else:
    umbrella = "No"
txt_msg = f"The weather forecast for today is: {main_weather}\nCurrent temperature: {current_temperature}\nHumidity: {humidity}\nMax temperature: {max_temperature}\nMin temperature: {min_temperature}\nCarry umbrella: {umbrella}"
print(txt_msg)
