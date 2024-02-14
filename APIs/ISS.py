import requests

"""
VARIABLES FOR THE APP
"""
URL = "http://api.open-notify.org/iss-now.json"
exception_message_404 = "The content your looking for does not exist."
exception_message_401 = "You are not authorised to access this data."

"""
MAKE THE GET REQUEST TO THE URL OF THE API
"""
res = requests.get(url=URL)

"""
MANAGE THE RESPONSE
"""
res.raise_for_status() #THIS HANDLES ALL KINDS EXCEPTIONS FOR US
if (res.status_code == 404):
    raise Exception(exception_message_404)
elif (res.status_code == 401):
    raise Exception(exception_message_401)
else:
    data = res.json()
    iss_position = data['iss_position']
    print(f"The ISS is at: \nlat. {iss_position['latitude']}, lon. {iss_position['longitude']}")