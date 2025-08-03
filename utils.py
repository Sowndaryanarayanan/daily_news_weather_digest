def format_news(news_list):
    return "\n\n".join([f"{i+1}. {item['title']} - {item['link']}" for i, item in enumerate(news_list)])
