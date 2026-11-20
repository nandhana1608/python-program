import csv
from collections import Counter
from datetime import datetime
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.bbc.com"

CATEGORIES = {
    "World": BASE_URL + "/news/world",
    "Business": BASE_URL + "/business",
    "Technology": BASE_URL + "/innovation/technology",
    "Science": BASE_URL + "/innovation/science"
}

HEADERS = {"User-Agent": "Mozilla/5.0"}
CSV_FILE = "news_headlines.csv"


def fetch_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Could not fetch:", e)
        return None


def find_date(tag):
    card = tag

    for _ in range(5):
        if card.parent is None:
            break

        card = card.parent

        time_tag = card.find("time")
        if time_tag:
            return time_tag.get("datetime") or time_tag.get_text(strip=True)

    return datetime.now().strftime("%Y-%m-%d")


def scrape_category(category, url):
    html = fetch_page(url)

    if html is None:
        return []

    soup = BeautifulSoup(html, "html.parser")
    articles = []
    seen = set()

    headline_tags = soup.find_all(attrs={"data-testid": "card-headline"})

    if not headline_tags:
        headline_tags = soup.find_all(["h2", "h3"])

    for tag in headline_tags:
        text = tag.get_text(strip=True)

        if len(text) < 15 or text in seen:
            continue

        seen.add(text)

        link_tag = tag.find_parent("a")
        link = ""

        if link_tag and link_tag.get("href"):
            href = link_tag["href"]
            link = href if href.startswith("http") else BASE_URL + href

        articles.append({
            "headline": text,
            "date": find_date(tag),
            "category": category,
            "link": link
        })

    return articles


def save_to_csv(articles, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["headline", "date", "category", "link"]
        )
        writer.writeheader()
        writer.writerows(articles)

    print("Saved", len(articles), "headlines to", filename)


def analyse(articles):
    print("\n===== ANALYSIS =====")
    print("Headlines per category:")

    for cat, count in Counter(a["category"] for a in articles).items():
        print(cat, ":", count)

    stop_words = {"the", "a", "an", "of", "to", "in", "and", "for", "on"}

    words = []

    for a in articles:
        for w in a["headline"].lower().split():
            w = w.strip(".,:;!?'\"()")

            if w.isalpha() and w not in stop_words:
                words.append(w)

    print("\nTop 10 keywords:")

    for word, count in Counter(words).most_common(10):
        print(word, ":", count)


def main():
    all_articles = []

    for category, url in CATEGORIES.items():
        print("Scraping", category, "...")
        items = scrape_category(category, url)
        print("Found", len(items), "headlines")
        all_articles.extend(items)

    if not all_articles:
        print("No headlines extracted. Check internet connection.")
        return

    print("\nSample headlines:")

    for a in all_articles[:5]:
        print(a["category"], a["headline"], a["date"])

    save_to_csv(all_articles, CSV_FILE)
    analyse(all_articles)


if __name__ == "__main__":
    main()
