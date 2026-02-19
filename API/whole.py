import sys
import requests
import json
import os
from dotenv import load_dotenv


def configure():
    load_dotenv()


def current_weather():
    city = sys.argv[1]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('api_key')}&units=metric"
    weather_data = requests.get(url)
    data = weather_data.json()
    return data


def main():
    configure()
    data = current_weather()
    # print(data)
    print(f"City: {data["name"]}")  # This show for your City name:
    print(f"Country: {data["sys"]["country"]}")  #
    print(data["main"]["temp"])
    print(data["main"]["feels_like"])
    print(data["main"]["temp_min"])
    print(data["main"]["temp_max"])
    print(data["wind"]["speed"])
    print(data["weather"])


if __name__ == "__main__":
    main()
