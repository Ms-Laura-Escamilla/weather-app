from dotenv import load_dotenv
import os
import requests

# Fetch api key from .env
load_dotenv()
apikey = os.getenv("API_KEY")

def getWeatherData(city):

    # Fetch Longitude and Latitude
    geocoding_response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={}&appid={}".format(city, apikey))

    lat = geocoding_response.json()[0]["lat"]
    lon = geocoding_response.json()[0]["lon"]

    # Fetch weather data (Temp F)
    weather_response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, apikey))

    temperature = weather_response.json()["main"]["temp"]
    return str("{:.2f}".format(KelvinToF(temperature))) + "F"

def KelvinToF(temp):
    return 1.8*(temp-273) + 32

if __name__ == "__main__":
    inputCity = input("Input a city: ")
    print(getWeatherData(inputCity))