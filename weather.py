import requests
import config
from pprint import pprint
api_key = config.API_KEY

def city_weather():
    city = input("Enter the city: ")
    req_url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric'
    print(req_url)
    weather = requests.get(req_url).json()
    # pprint(weather)
    print(f"Current weather for {weather['name']}")
    print(f"Country {weather['sys']['country']}")
    print(f"The temprature is {weather['main']['temp']}")
    print(f"Feels like {weather['main']['feels_like']}")
    print(f"Overcast {weather['weather'][0]['description']}")
    print(f"Mostly {weather['weather'][0]['main']}")
city_weather()