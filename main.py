"""Run the weather CLI with: python main.py Abuja."""
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))
from weather_tool.client import WeatherError, fetch_weather, format_report


def main() -> int:
    parser = argparse.ArgumentParser(description="Get live weather from OpenWeatherMap")
    parser.add_argument("city", nargs="?", help="City name (e.g. Abuja)")
    args = parser.parse_args()
    city = args.city or input("Enter a city name: ").strip()
    try:
        weather = fetch_weather(city, os.environ.get("OPENWEATHER_API_KEY", ""))
    except WeatherError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(format_report(city, weather))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
