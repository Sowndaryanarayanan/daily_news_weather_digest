import requests

CITY_COORDS = {
    "chennai": (13.0827, 80.2707),
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "kolkata": (22.5726, 88.3639)
}

def get_weather(city):

    # normalize input (avoid case problems)
    city = city.strip().lower()

    # spelling alias
    if city == "bengaluru":
        city = "bangalore"

    # safe lookup (prevents KeyError)
    coords = CITY_COORDS.get(city)

    # if city not found, fallback to Chennai
    if coords is None:
        coords = CITY_COORDS["chennai"]

    lat, lon = coords

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    response = requests.get(url)
    data = response.json()

    return data.get("current_weather", {})
