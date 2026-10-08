"""OpenWeatherMap client with explicit configuration and error handling."""
import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"


class WeatherError(Exception):
    """Raised when a weather report cannot be retrieved."""


def fetch_weather(city: str, api_key: str) -> dict:
    if not city.strip():
        raise WeatherError("A city name is required.")
    if not api_key.strip():
        raise WeatherError("Set OPENWEATHER_API_KEY in your environment.")
    try:
        response = requests.get(API_URL, params={"q": city.strip(), "appid": api_key, "units": "metric"}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {"temperature": data["main"]["temp"], "condition": data["weather"][0]["description"].title(), "humidity": data["main"]["humidity"]}
    except requests.RequestException as exc:
        raise WeatherError("Weather service request failed; check the city, network or API key.") from exc
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise WeatherError("Unexpected response from the weather service.") from exc


def format_report(city: str, weather: dict) -> str:
    return (f"Weather report for {city}:\\n"
            f"Temperature: {weather['temperature']}°C\\n"
            f"Condition: {weather['condition']}\\n"
            f"Humidity: {weather['humidity']}%").replace("\\n", "\n")
