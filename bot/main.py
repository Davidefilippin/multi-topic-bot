from fetcher import fetch_articles
from publisher import send_message

def main():
    articles = fetch_articles()
    for article in articles:
        send_message(article["title"], article["link"])

if __name__ == "__main__":
    main()
