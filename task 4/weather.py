import requests
import json

API_KEY = "cf45402b55cb605ab961ee6029dc2a2e" # replace with your actual API key

def get_weather(location):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather_desc = data["weather"][0]["description"]
        print(f"Temperature: {main['temp']}°K")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather Conditions: {weather_desc}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("City not found.")

if __name__ == "__main__":
    location = input("Enter city or ZIP code: ")
    get_weather(location)