import requests
from bs4 import BeautifulSoup

def get_news(city):
    url = "https://www.thehindu.com/news/national/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    headlines = soup.find_all("a", class_="story-card75x1-text", limit=50)

    news_list = []

    for h in headlines:
        title = h.get_text(strip=True)
        link = h.get("href")

        if city.lower() in title.lower():
            news_list.append({"title": title, "link": link})

        if len(news_list) == 10:
            break

    if len(news_list) == 0:
        # fallback to top 10 headlines
        for h in headlines[:10]:
            title = h.get_text(strip=True)
            link = h.get("href")
            news_list.append({"title": title, "link": link})

    return news_list

