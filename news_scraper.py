import requests
from bs4 import BeautifulSoup

def get_news(city):
    rss_url = "https://www.thehindu.com/news/national/feeder/default.rss"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(rss_url, headers=headers)
    soup = BeautifulSoup(resp.content, "xml")
    items = soup.find_all("item", limit=20)

    news_list = []
    city_lower = city.lower()

    for item in items:
        title = item.title.text
        link = item.link.text
        # filter if city name appears in title
        if city_lower in title.lower():
            news_list.append({"title": title, "link": link})
        if len(news_list) == 10:
            break

    # fallback to top 10 if no city-specific
    if not news_list:
        for item in items[:10]:
            news_list.append({
                "title": item.title.text,
                "link": item.link.text
            })
    return news_list

