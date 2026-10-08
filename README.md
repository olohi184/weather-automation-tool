# Weather Automation Tool — Python CLI

A Python command-line application that retrieves live city weather from the OpenWeatherMap API. This repository documents a learning progression from mock weather data (V1) to a live API integration (V2) and now a structured Python application.

## Features
- Live temperature, weather condition and humidity for a city
- API credentials loaded from the environment (not stored in code)
- HTTP timeouts and readable error messages
- Mocked unit tests that do not need an API key or internet connection

## Security notice
An earlier version of this repository included an API key in a committed file. **Treat that key as compromised. Revoke it in the OpenWeatherMap dashboard and issue a new key.** Removing the key from current source files does not remove it from Git history. Do not put your new key in a notebook, commit, screenshot or README.

## Setup
Requires Python 3.10+.

```bash
git clone https://github.com/olohi184/weather-automation-tool.git
cd weather-automation-tool
python -m pip install -r requirements.txt
```

Set `OPENWEATHER_API_KEY` in your terminal. On macOS/Linux:
```bash
export OPENWEATHER_API_KEY="your-new-key"
python main.py Abuja
```

On Windows PowerShell:
```powershell
$env:OPENWEATHER_API_KEY="your-new-key"
python main.py Abuja
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Structure
- `main.py` — command-line entry point
- `src/weather_tool/client.py` — reusable API client and report formatter
- `tests/` — mocked unit tests
- `.env.example` — configuration variable example (not a credential)
- Earlier notebooks and versioned scripts — retained as learning history

## Author
Olohimai Juliet Michael · [GitHub](https://github.com/olohi184)
