"""Legacy V2 compatibility entry point (API key loaded from environment)."""
import os
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        print("Set OPENWEATHER_API_KEY before running live weather requests.")
        return None
    try:
        response = requests.get(BASE_URL, params={"q": city, "appid": api_key, "units": "metric"}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {"temperature": data["main"]["temp"], "condition": data["weather"][0]["description"].title(), "humidity": data["main"]["humidity"]}
    except (requests.RequestException, KeyError, IndexError, ValueError):
        return None


def main():
    city = input("Enter a city name: ").strip()
    weather = get_weather(city)
    if weather:
        print(f"Weather Report for {city}: {weather['temperature']}°C, {weather['condition']}, humidity {weather['humidity']}%")
    else:
        print("Unable to retrieve weather. Check the API key, city, or connection.")


if __name__ == "__main__":
    main()
