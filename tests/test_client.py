"""Unit tests without network requests or real credentials."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch, Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from weather_tool.client import WeatherError, fetch_weather, format_report


class WeatherTests(unittest.TestCase):
    def test_missing_key(self):
        with self.assertRaises(WeatherError):
            fetch_weather("Abuja", "")

    @patch("weather_tool.client.requests.get")
    def test_success(self, get):
        response = Mock()
        response.json.return_value = {"main": {"temp": 29, "humidity": 65}, "weather": [{"description": "light rain"}]}
        get.return_value = response
        result = fetch_weather("Abuja", "test-key")
        self.assertEqual(result["condition"], "Light Rain")
        self.assertIn("29°C", format_report("Abuja", result))
        self.assertEqual(get.call_args.kwargs["timeout"], 10)

    @patch("weather_tool.client.requests.get")
    def test_http_failure(self, get):
        import requests
        get.return_value.raise_for_status.side_effect = requests.HTTPError("401")
        with self.assertRaises(WeatherError):
            fetch_weather("Abuja", "invalid")


if __name__ == "__main__":
    unittest.main()
