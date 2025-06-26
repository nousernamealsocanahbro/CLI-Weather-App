import os
import requests
import datetime as dt
from dotenv import load_dotenv, dotenv_values
load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv("MY_KEY")
if not API_KEY:
    raise("API key not found")

def get_weather():
    city = input("Input city name here: ").capitalize()
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    return(url)

def get_response(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return(response.json())
    except requests.RequestException as e:
        print(e)

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = int(round(kelvin - 273.15, 0))
    fahrenheit = int(round(celsius * (9/5) + 32, 0))

    return celsius, fahrenheit

def get_items(response):
    # prefixes to avoid redundant code
    main = response["main"]
    weather = response["weather"]
    wind = response["wind"]
    sys = response["sys"]

    temp_kelvin = main["temp"]
    feels_like_kelvin = main["feels_like"]

    humidity = main["humidity"]
    forecast = weather[0]["description"]

    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    wind_speed = wind["speed"]

    print(f"Forecast: {forecast}")
    print(f"Temperature: {temp_celsius}°c, {temp_fahrenheit}°f")
    print(f"Feels like: {feels_like_celsius}°c, {feels_like_fahrenheit}°f")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed}m/s")

while True:
    url = get_weather()

    response = get_response(url)
    get_items(response)

    input("\nPress enter to continue...")