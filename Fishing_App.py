import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import pytz


Spot = input("Where would you like to check?: ")

params = {
  'access_key': '3d6a9b28608ad2bce335fe43be34810f',
  'query': Spot.lower(),
  'units': 'f',
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()

#print(f'Current temperature in {api_response["location"]["name"]} is {api_response["current"]["temperature"]}F and {api_response["current"]["weather_descriptions"]}')
Place = api_response["location"]["name"]
Temp = api_response["current"]["temperature"]
CloudCover = api_response["current"]["weather_descriptions"]
CloudCoverList = ', '.join(CloudCover)
Clouds = CloudCoverList.lower()

#Checks if it is good weather for Bass
def Check_Temp():
    if Temp >= 55 and Temp < 65:
        print(f"The weather in {Place} seems good for Bass today. It's {Temp}")
        return True
    elif Temp > 65:
        print(f"A little too warm for Bass right now in {Place}. It's {Temp}")
        return False
    else: 
        print(f"Probably too cold for Bass in {Place}. It's {Temp}")
        return False


# Checks if it is raining
def Check_Rain():
    if "rain" in Clouds:
        print("A little rain right now. Wait it out for a bit.")
        return True
    else:
        print("No rain today")
        return False


# Main Code

def Check_Times():

    time = api_response["location"]["timezone_id"]
    tz = pytz.timezone(time)

    dt = datetime.datetime.now(tz)
    print(dt.time())

    if dt.time() < datetime.time(9):
        print("Fishing might be good it's still morning")
        return True
    else:
        print("Fishing might be rougher it's after 9 A.M.")
        return False


if Check_Times() == True:
    t = Check_Rain()

    if t == False:
        Check_Temp()








 




