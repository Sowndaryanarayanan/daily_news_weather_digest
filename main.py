import streamlit as st
from news_scraper import scrape_news
from weather_scraper import scrape_weather
import pandas as pd

st.set_page_config(page_title="📰 Daily Digest", layout="wide")
st.title("🌤️ Daily News & Weather Digest")

with st.spinner("Scraping news..."):
    news = scrape_news()

with st.spinner("Fetching weather info..."):
    weather = scrape_weather()

all_data = news + weather
df = pd.DataFrame(all_data)

st.subheader("📰 News & Weather Table")
st.dataframe(df, use_container_width=True)

# Optional: allow CSV download
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download Digest CSV", csv, "digest_output.csv", "text/csv")

st.success("✅ Daily Digest ready!")
