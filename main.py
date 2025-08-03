import streamlit as st
from news_scraper import get_news
from weather_fetcher import get_weather
import pandas as pd

st.set_page_config(page_title="📰 Hindu News + Weather", layout="centered")
st.title("📰 The Hindu News + Weather in 1 Click!")
st.markdown("💎 [Buy Premium - ₹49](https://buymeacoffee.com/sowndarya)")
city = st.selectbox("📍 Choose your city:", ["Chennai", "Bengaluru", "Hyderabad", "Delhi", "Mumbai"])

if st.button("🧠 Fetch Headlines + Weather"):
    with st.spinner("Fetching live headlines and weather..."):
        news = get_news(city)
        weather = get_weather(city)
    st.subheader("🌤️ Weather Today")
    st.write(weather)
    st.subheader("🗞️ Top Headlines")
    for i, item in enumerate(news, 1):
        st.markdown(f"**{i}. {item['title']}**")
        st.caption(f"[Read more →]({item['link']})")
    df = pd.DataFrame(news)
    st.download_button("📥 CSV Download", df.to_csv(index=False), "news.csv")
    st.markdown("🔒 Want JSON or email reports? [Buy Premium - ₹49](https://buymeacoffee.com/sowndarya)")



