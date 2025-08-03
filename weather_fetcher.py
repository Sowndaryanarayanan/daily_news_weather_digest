import requests

def get_weather(city):
    api_key = "01a863fe45b7808757e9941867178a5d"  # keep this safe later
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"].title()
            temp = data["main"]["temp"]
            return f"🌤️ {city}: {weather}, {temp}°C"
        else:
            return f"⚠️ Couldn't fetch weather for {city}."
    except Exception as e:
        return f"❌ Error: {e}"
