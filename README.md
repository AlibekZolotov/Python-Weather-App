# 🌤️ Python Weather App

**A simple interactive Python application that fetches live weather data using the OpenWeatherMap API.**

---

## Overview

This Python project allows users to **get real-time weather information** for any city. It displays:

* Temperature (in Celsius)
* Weather description (e.g., cloudy, sunny)
* Humidity
* Wind speed

The app includes error handling for invalid city names, network issues, or missing API keys, and runs interactively until the user chooses to quit.

---

## Features

* Fetch live weather data using **OpenWeatherMap API**
* Display weather information in a clean, readable format
* Interactive: type city names repeatedly and quit anytime
* Error handling for invalid inputs and network problems
* Easy to extend for additional features, e.g., forecast or multiple units

---

## How It Works

1. **API Setup**: Requires a personal OpenWeatherMap API key.
2. **User Input**: Prompts user for a city name.
3. **API Request**: Sends a GET request using the `requests` library.
4. **Data Parsing**: Extracts temperature, humidity, weather description, and wind speed from JSON.
5. **Error Handling**: Detects invalid city names, network errors, and unexpected API responses.
6. **Display**: Shows weather information in a friendly, formatted output.

---

## Usage

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/python-weather-app.git
cd python-weather-app
```

2. **Install dependencies**

```bash
pip install requests
```

3. **Add your API key**

You can either:

* Directly assign it in the code:

```python
API_KEY = "YOUR_API_KEY"
```

* Or set it as an environment variable for better security:

```bash
export WEATHER_API_KEY="YOUR_API_KEY"   # Mac/Linux
set WEATHER_API_KEY="YOUR_API_KEY"      # Windows
```

4. **Run the app**

```bash
python weather_app.py
```

5. **Interact with the app**

* Type a city name to get its weather
* Type `quit` to exit

---

## Example

```
Enter a city name (or type 'quit' to exit): London

Weather in London:
Temperature: 15°C
Description: Light rain
Humidity: 82%
Wind Speed: 3.6 m/s
```

---

## Requirements

* Python 3.x
* `requests` library
* OpenWeatherMap API key (free signup [here](https://openweathermap.org/api))

---

## Best Practices

* **Never hardcode API keys** in public repos. Use environment variables.
* Always handle exceptions for network requests (`RequestException`) and JSON parsing (`KeyError`).
* Validate user input before sending API requests.
* Keep code modular and reusable (e.g., `get_weather()` function).

---

## License

MIT License – Free to use and modify.
