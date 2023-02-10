import requests

def get_weather(city):
    api_key = "<API_KEY>"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    weather_data = requests.get(url).json()

    if weather_data["cod"] != "404":
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        return f"Temperature in {city}: {temperature}°F\nWeather description: {weather_description}"
    else:
        return "City not found"

city = input("Enter city name: ")
print(get_weather(city))
