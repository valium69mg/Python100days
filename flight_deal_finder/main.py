
import os 
from dotenv import load_dotenv
import requests

load_dotenv()

SHEET_URL = "https://api.sheety.co/fbfbd5d717d9ebe861b7db1757ba3cfe/flightDealFinder/hoja1"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


"""
TEQUILA KIWI API REQUESTS
"""

header = {
    "apikey":os.getenv("API_KEY_TEQUILA")
}
json = {
    "fly_from":"airport:QRO",
    "fly_to":"CUN",
    "date_from":"01/06/2024",
    "date_to":"08/06/2024"
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
    price = res.json()['hoja1'][0]["price"]
    if (price > flight_to_compare["price"]):
        return True
    else:
        return False
    
"""
COMPUTE THE CHEAPEST FLIGHT OF TODAY
"""

flight_to_save = lowest_price_flight()

"""
MAIN LOGIC
IF THE FLIGHT FOUND TODAY IS CHEAPER THAN THE SPREED SHEET FLIGHT
IT ADDS IT TO THE SPREAD SHEET
"""

if (is_flight_cheaper(flight_to_compare=flight_to_save) == True):
    save_flight_to_spreadsheet(flight_to_save)
else:
    print("There are no flights cheaper")

