import json

import requests

def get_weather():
    response=requests.get("https://gorest.co.in/public/v2/users/")
    if response.status_code==200:
        return response.json()

    else:
        raise ValueError("Could not fetch weather data")