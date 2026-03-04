import requests
from bs4 import BeautifulSoup

URL = "https://apnews.com/article/blizzard-weather-east-coast-a9955d3581a169426ecb0d5fc2941c23"
WORDS_TO_CHECK = ["Blizzard", "Onomatopoeia", "The"]

def scrape_article(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    # Date
    date_tag = soup.find("bsp-timestamp") or soup.find("div", class_=lambda c: c and "timestamp" in c.lower())
    date = date_tag.get_text(strip=True) if date_tag else "N/A"

    # Author
    author_tag = (
        soup.find("a", class_=lambda c: c and "author" in c.lower()) or
        soup.find("span", class_=lambda c: c and "author" in c.lower()) or
        soup.find("div", class_=lambda c: c and "author" in c.lower())
    )
    author = author_tag.get_text(strip=True) if author_tag else "N/A"

    # Full text
    paragraphs = soup.find_all("p")
    article_text = " ".join(p.get_text() for p in paragraphs)

    return title, date, author, article_text

def check_words(text, words):
    print("\n--- Word Check ---")
    for word in words:
        found = word.lower() in text.lower()
        print(f"  '{word}': {'✅ Found' if found else '❌ Not found'}")

if __name__ == "__main__":
    title, date, author, article_text = scrape_article(URL)

    print("--- Article Info ---")
    print(f"  Title:  {title}")
    print(f"  Date:   {date}")
    print(f"  Author: {author}")

    check_words(article_text, WORDS_TO_CHECK)