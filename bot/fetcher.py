import feedparser

FEEDS = [
    "https://www.ansa.it/sito/ansait_rss.xml"
]

def fetch_articles():
    articles = []
    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            articles.append({
                "title": entry.title,
                "link": entry.link
            })
    return articles
