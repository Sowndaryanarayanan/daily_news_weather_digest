import streamlit as st
from news_scraper import get_news
from weather_fetcher import get_weather
import pandas as pd
from datetime import datetime

# 🧠 Page Setup
st.set_page_config(page_title="📰 Hindu News + Weather", layout="centered")
st.title("📰 The Hindu News + Weather in 1 Click!")

# 💬 Welcome Message (So your page isn't empty before clicking!)
st.markdown("Welcome to your daily dose of 🧠 AI-powered news from [The Hindu](https://www.thehindu.com/) and live 🌤️ weather updates.")
st.info("Select your city and language below, then click the button to fetch real-time data!")

# 🙌 Tip Link (Stripe-friendly!)
st.markdown("💛 If you enjoy this project, consider [sending a tip](https://buymeacoffee.com/sowndarya) to support my work!")

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
    filename = f"news_{city}_{datetime.now().strftime('%Y%m%d')}.csv"
    st.download_button("📥 Download News CSV", df.to_csv(index=False), filename)

    # 🔐 Friendly Tip Reminder Again
    st.markdown("💙 Want more features like JSON/API access or email delivery? [Send a Tip](https://buymeacoffee.com/sowndarya) to help keep this project going!")

# 👣 Footer
st.markdown("---")
st.caption("Built with 💻 by [Sowndarya](https://buymeacoffee.com/sowndarya)")
