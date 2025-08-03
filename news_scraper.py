import requests
from bs4 import BeautifulSoup

def get_news(city, lang):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    if lang == "Tamil":
        # ✅ Go to main site and grab top stories
        url = "https://www.hindutamil.in/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # 📌 Select top headlines — verified selector
        headlines = soup.select("div.top-news h3 a")
        news_list = []

        for h in headlines[:10]:
            title = h.get_text(strip=True)
            link = h.get("href")
            full_link = "https://www.hindutamil.in" + link if link.startswith("/") else link
            news_list.append({"title": title, "link": full_link})

        return news_list

    else:
        # ✅ English headlines from RSS
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
