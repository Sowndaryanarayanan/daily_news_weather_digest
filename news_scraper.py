import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://www.thehindu.com/news/national/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    articles = []
    for article in soup.find_all("a", class_="story-card75x1-text"):
        title = article.get_text(strip=True)
        link = article['href']
        articles.append({"title": title, "link": link})

    return articles[:10]
