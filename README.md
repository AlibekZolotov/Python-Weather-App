# Python-Weather-App
Simple interactive Python app that fetches live weather data using the OpenWeatherMap API.

Description

This project is a Python-based weather application that allows users to input a city name and get real-time weather information, including:

Temperature (in Celsius)

Weather description (e.g., cloudy, sunny)

Humidity

Wind speed

The app handles errors gracefully, such as:

Invalid city names

Network issues

Missing or incorrect API key

Unexpected API response structure

The program is fully interactive: users can repeatedly query weather for different cities and exit when they choose.

Features

Fetch live weather data using OpenWeatherMap API

Display weather information in a clean, readable format

Input validation and error handling for a smooth user experience

Continuous loop until user chooses to quit

Easy to extend (forecast, multiple units, graphical output)

How it works

API Setup: The app uses the OpenWeatherMap API and requires a personal API key.

User Input: The user types a city name.

API Request: Python requests library sends a GET request to OpenWeatherMap.

Data Processing: The app parses JSON response to extract temperature, humidity, description, and wind speed.

Error Handling: Handles invalid city names, network errors, or unexpected responses.

Output: Displays the weather information in a friendly format.
