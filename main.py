from news_scraper import scrape_news
from weather_scraper import scrape_weather
import pandas as pd

news = scrape_news()
weather = scrape_weather()

all_data = news + weather

df = pd.DataFrame(all_data)
df.to_csv("digest_output.csv", index=False)

print("✅ Daily Digest ready! Check digest_output.csv")