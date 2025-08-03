import requests
from bs4 import BeautifulSoup

def get_news(city, lang):
    headers = {"User-Agent": "Mozilla/5.0"}

    if lang == "Tamil":
        url = "https://www.hindutamil.in/news/rssfeed"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "xml")
        items = soup.find_all("item", limit=20)

        news_list = []
        for item in items:
            title = item.title.text.strip()
            link = item.link.text.strip()
            # Tamil version: Skip city filter to avoid mismatch
            news_list.append({"title": title, "link": link})
            if len(news_list) == 10:
                break

        return news_list

    else:
        # English News - Filter by city
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

        # fallback to top 10 if nothing matched
        if not news_list:
            for item in items[:10]:
                news_list.append({
                    "title": item.title.text.strip(),
                    "link": item.link.text.strip()
                })

        return news_list

