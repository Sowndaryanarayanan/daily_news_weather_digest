import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        forecast = soup.select_one(".b-forecast__table-description-content").text.strip()
        return {"Type": "Weather", "Detail": f"{city}: {forecast}", "URL": url}
    except:
        return {"Type": "Weather", "Detail": f"{city}: Not Found", "URL": url}

def scrape_weather():
    cities = ["Chennai", "Delhi", "Mumbai", "Hyderabad", "Bangalore"]
    results = [get_weather(city) for city in cities]
    return results