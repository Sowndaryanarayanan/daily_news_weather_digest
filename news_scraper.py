import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

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

    # Tamil translation
    if lang == "Tamil":
        translator = GoogleTranslator(source='en', target='ta')
        for article in news_list:
            try:
                article["title"] = translator.translate(article["title"])
            except:
                article["title"] = "தமிழ் மொழிபெயர்ப்பு கிடைக்கவில்லை"

    return news_list
