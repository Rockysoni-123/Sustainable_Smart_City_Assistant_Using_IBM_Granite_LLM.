# services/weather.py

def get_weather_info():
    print("\n[Weather Service]")
    # Simulate weather data (can connect to OpenWeatherMap, AccuWeather, etc.)
    weather_info = {
        "temperature": "27°C",
        "condition": "Sunny",
        "humidity": "45%",
        "wind": "10 km/h NW"
    }
    print(f"Current temperature: {weather_info['temperature']}")
    print(f"Condition: {weather_info['condition']}")
    print(f"Humidity: {weather_info['humidity']}")
    print(f"Wind: {weather_info['wind']}")
