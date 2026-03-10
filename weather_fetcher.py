import requests

CITY_COORDS = {
    "chennai": (13.0827, 80.2707),
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "kolkata": (22.5726, 88.3639)
}

def get_weather(city):
    
    # normalize input
    city = city.strip().lower()

    # alias fix
    if city == "bengaluru":
        city = "bangalore"

    # fallback if city not in dictionary
    if city not in CITY_COORDS:
        city = "chennai"

    lat, lon = CITY_COORDS[city]

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    data = requests.get(url).json()

    return data["current_weather"]
