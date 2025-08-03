import requests

def get_weather(city):
    api_key = "ENTER_YOUR_OPENWEATHERMAP_API_KEY"
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"{city}: {weather}, {temp}°C"
    else:
        return "Weather info not available right now."
