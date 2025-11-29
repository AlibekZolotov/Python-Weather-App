import requests
import os
API_KEY = "YOUR API KEY"
def get_weather(city):
    try:
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        if data.get("cod") !=200:
            print(f"Error: {data.get('message')}")
            return None
        
        weather_info={
            "city":data ["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        
        return weather_info
    except requests.exceptions.RequestException as e:
        print("Network error", e)
        return None
    except KeyError as e:
        print("Unexpected response structure ",e)
        return None 
    
while True:
    city = input("\nEnter a city name (or type 'quit' to exit): ")
    if city.lower() == "quit":
        print("Exiting... Bye!")
        break

    weather = get_weather(city)

    if weather:
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description'].capitalize()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Could not fetch weather. Please try again.")

        
