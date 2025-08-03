import streamlit as st
from news_scraper import get_news
from weather_fetcher import get_weather
import pandas as pd

# 🧠 Page Setup
st.set_page_config(page_title="📰 Hindu News + Weather", layout="centered")
st.title("📰 The Hindu News + Weather in 1 Click!")
st.markdown("💎 [Buy Premium - ₹49](https://buymeacoffee.com/sowndarya)")
st.markdown("Built by [Sowndarya](https://buymeacoffee.com/sowndarya) 💙")

# 📍 City Selector
city = st.selectbox("📍 Choose your city:", ["Chennai", "Bengaluru", "Hyderabad", "Delhi", "Mumbai"])

# 🌐 Language Selector
lang = st.selectbox("🈳 Choose language:", ["English", "Tamil"])

# 🧠 Main Action Button
if st.button("⚡ Fetch Headlines + Weather"):
    with st.spinner("Fetching live headlines and weather..."):
        news = get_news(city, lang)
        weather = get_weather(city)

    # 🌤️ Show Weather
    st.subheader("🌤️ Weather Today")
    st.write(weather)

    # 🗞️ Show News
    st.subheader("🗞️ Top Headlines" + (" (தமிழ்)" if lang == "Tamil" else ""))

    for i, item in enumerate(news, 1):
        st.markdown(f"**{i}. {item['title']}**")
        st.caption(f"[மேலும் படிக்க →]({item['link']})" if lang == "Tamil" else f"[Read more →]({item['link']})")

    # 📥 Download CSV
    df = pd.DataFrame(news)
    st.download_button("📥 Download News CSV", df.to_csv(index=False), "news.csv")

    # 🔒 Premium Tease
    st.markdown("🔒 Want JSON or email delivery? [Buy Premium - ₹49](https://buymeacoffee.com/sowndarya)")
