import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_news(city, lang):
    headers = {"User-Agent": "Mozilla/5.0"}
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

    # Translate to Tamil if selected
    if lang == "Tamil":
        translator = Translator()
        for article in news_list:
            translated = translator.translate(article["title"], src="en", dest="ta")
            article["title"] = translated.text

    return news_list


