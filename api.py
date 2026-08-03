import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("AIRLABS_API_KEY")

url = "https://airlabs.co/api/v9/flight"

params = {
    "api_key": api_key,
    "flight_iata": "BA117"
}

response = requests.get(url, params=params)

print(response.status_code)
data = response.json()
if "response" in data:
    flight = data["response"]

    print(f"Flight: {flight["flight_iata"]}")
    print(f"Airline: {flight["airline_name"]}")
    print(f"From: {flight["dep_name"]}")
    print(f"To: {flight["arr_name"]}")
    print(f"Status: {flight["status"]}")
else:
    print(data["error"]["message"])
