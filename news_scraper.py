import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://www.thehindu.com/news/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return [{"Type": "News", "Detail": "Failed to fetch news", "URL": ""}]

    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.select("h3 a")  # May need to tweak this selector
    news_list = []

    for headline in headlines[:10]:
        title = headline.text.strip()
        link = headline['href']
        news_list.append({"Type": "News", "Detail": title, "URL": link})

    return news_list
