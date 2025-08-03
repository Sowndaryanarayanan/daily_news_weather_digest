# news_scraper.py
import requests
from bs4 import BeautifulSoup

def get_news(city, lang):
    headers = {"User-Agent": "Mozilla/5.0"}

    if lang == "Tamil":
        url = "https://www.dinamani.com/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.select("div.other-news h3 a")  # verified tag style for Dinamani
        news_list = []

        for h in headlines[:10]:
            title = h.get_text(strip=True)
            link = h.get("href")
            if not link.startswith("http"):
                link = "https://www.dinamani.com" + link
            news_list.append({"title": title, "link": link})

        return news_list

    else:
        # English - The Hindu RSS
        url = "https://www.thehindu.com/news/national/feeder/default.rss"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "xml")
        items = soup.find_all("item", limit=20)

        news_list = []
        city_lower = city.lower()

        for item in items:
            title = item.title.text.strip()
            link = item.link.text.strip()
            if city_lower in title.lower():
                news_list.append({"title": title, "link": link})
            if len(news_list) == 10:
                break

        if not news_list:
            for item in items[:10]:
                news_list.append({
                    "title": item.title.text.strip(),
                    "link": item.link.text.strip()
                })

        return news_list

