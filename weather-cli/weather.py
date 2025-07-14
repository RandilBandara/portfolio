import requests
import argparse

# Replace with your real API key from https://openweathermap.org/api
API_KEY = "3ae31e3a9f661d9cc664523746d4b57a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="Get current weather info for a city")
parser.add_argument("city", help="City name to get the weather for")
args = parser.parse_args()
city = args.city

# Build API request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# Send the request
response = requests.get(url)
data = response.json()

# Parse and display the result
if data["cod"] == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Weather in {city}: {temp}°C, {desc}")
else:
    print(f"Error: City '{city}' not found.")
 
