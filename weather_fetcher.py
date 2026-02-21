import requests

CITY_COORDS = {
    "Chennai": (13.0827, 80.2707),
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
    "Kolkata": (22.5726, 88.3639)
}

def get_weather(city):
    lat, lon = CITY_COORDS[city]

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    data = requests.get(url).json()

    return data["current_weather"]
