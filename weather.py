#pip - preferred installer program - m modules
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()       # imports the api key from th env file

def get_current_weather(city='Pune'):

    request_url = f'http://api.weatherapi.com/v1/current.json?key={os.getenv("API_KEY")}&q={city}'
    
    weather_data = requests.get(request_url).json()

    return weather_data
    # print(request_url)

    # pprint(weather_data)

    # print(f"\nCurrent weather for {weather_data['location']['name']}\n")
    # print(f"Feels Like {weather_data['current']['feelslike_c']}\n")
    # print(f"Temperature calulated around {weather_data['location']['localtime']}\n")

if __name__ == '__main__':

    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nPlease enter a city name:\n")

    # check for empty strings or strings with spaces
    if not bool(city.strip()):
        city = 'Pune'

    weather = get_current_weather(city)
    
    pprint(weather)