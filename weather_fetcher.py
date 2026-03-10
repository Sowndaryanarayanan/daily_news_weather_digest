import requests

CITY_COORDS = {
    "chennai": (13.0827, 80.2707),
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "hyderabad": (17.3850, 78.4867),
    "kolkata": (22.5726, 88.3639)
}

def get_weather(city):
    try:
        # Normalize the city name
        city = city.strip().lower()

        # Handle alternate spelling
        if city == "bengaluru":
            city = "bangalore"

        # Get coordinates safely
        lat, lon = CITY_COORDS.get(city, CITY_COORDS["chennai"])

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        return data.get("current_weather", {})

    except Exception as e:
        # If ANY error happens, return safe output instead of crashing
        return {"error": str(e)}
