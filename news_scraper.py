import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_news():
    url = "https://www.thehindu.com/news/"  # or Sun News if structured
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.select("h3 a")  # Change this to real selector
    news_list = []

    for headline in headlines[:10]:
        title = headline.text.strip()
        link = headline['href']
        news_list.append({"Type": "News", "Detail": title, "URL": link})

    return news_list