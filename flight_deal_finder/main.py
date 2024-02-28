
import os 
from dotenv import load_dotenv
import requests

load_dotenv()

SHEET_URL = "https://api.sheety.co/fbfbd5d717d9ebe861b7db1757ba3cfe/flightDealFinder/hoja1"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
DATE_FROM="01/06/2024"
DATE_TO="08/06/2024"

"""
TEQUILA KIWI API REQUESTS
"""

header = {
    "apikey":os.getenv("API_KEY_TEQUILA")
}
json = {
    "fly_from":"airport:QRO",
    "fly_to":"CUN",
    "date_from":DATE_FROM,
    "date_to":DATE_TO
}

def lowest_price_flight(json=json):
    res = requests.get(url=TEQUILA_ENDPOINT,params=json,headers=header)
    res.raise_for_status()
    data = res.json()["data"]
    list_of_flights = []
    """
    PURGE THE DATA AND APPEND THE CREATED OBJECTS ON A LIST
    """
    for dict in data:
        current_dict = dict["route"][0]
        fly_from = current_dict["flyFrom"]
        fly_to = current_dict["flyTo"]
        flight_no = current_dict["operating_flight_no"]
        price = dict["price"]
        local_date = current_dict["local_departure"]
        arrival_date = current_dict["local_arrival"]
        flight = {
            "from":fly_from,
            "to":fly_to,
            "flight":flight_no,
            "price":price,
            "localDate":local_date,
            "arrivalDate":arrival_date
        }
        list_of_flights.append(flight)
        """
        COMPUTE THE ELEMENT WITH THE LOWEST PRICE
        """
        lowest_price = 0
        for dict in list_of_flights:
            if (lowest_price == 0):
                lowest_price = dict["price"]
            else:
                if (lowest_price > dict["price"]):
                    lowest_price = dict["price"]
            
        for dict in list_of_flights:
            if (dict["price"] == lowest_price):
                return dict

"""
SAVE FLIGHT TO SPREAD SHEET FUNCTION
"""

def save_flight_to_spreadsheet(flight):
    body = {
        "hoja1":flight
    }
    res = requests.post(url=SHEET_URL,json=body)
    res.raise_for_status()

"""
COMPARE IF THE FLIGHT IS CHEAPER THAN THE ALREADY
SAVED FLIGHT ON THE SHEETS
"""

def is_flight_cheaper(flight_to_compare):
    res = requests.get(url=SHEET_URL)
    res.raise_for_status()
    # IF THE IS NO FLIGHT REGISTERED WE SAVE IT 
    if (res.json()['hoja1'] == []):
        save_flight_to_spreadsheet(flight_to_compare)
        return False
    else:
        # COMPARE FLIGHTS
        price = res.json()['hoja1'][0]["price"]
        if (int(price) > int(flight_to_compare["price"])):
            return True
        else:
            return False

"""
FUNCTION TO FIND THE ID OF THE CURRENT SAVED FLIGHT
"""

def find_flight_id():
    res = requests.get(url=SHEET_URL)
    res.raise_for_status()
    id = res.json()["hoja1"][0]["id"]
    return id

"""
IF A FLIGHT IS ALREADY SAVED WE NEED TO UPDATE THE FLIGHT INFO
AND WE DO IT WITH A PUT REQUEST
"""
        
def update_flight(new_flight,id=find_flight_id()):
    body = {
        "hoja1":new_flight
    }
    res = requests.put(url=SHEET_URL+f"/{id}",json=body)
    res.raise_for_status()

"""
COMPUTE THE CHEAPEST FLIGHT OF TODAY
"""

flight_to_save = lowest_price_flight()

"""
MAIN LOGIC
IF THE FLIGHT FOUND TODAY IS CHEAPER THAN THE SPREED SHEET FLIGHT
IT ADDS IT TO THE SPREAD SHEET
"""

test_flight = {
    "hoja1":{
        "from":"QRO",
        "to":"CUN",
        "flight":"69",
        "price":"69",
        "localDate":"Hello",
        "arrivalDate":"World"
    }
}
    

if (is_flight_cheaper(flight_to_compare=flight_to_save) == True):
    update_flight(new_flight=flight_to_save)
    print("Flight info updated!")
else:
    print("There are no flights cheaper")

