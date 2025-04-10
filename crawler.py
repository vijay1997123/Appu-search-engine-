# crawler.py
import requests
from bs4 import BeautifulSoup
import json

def crawl_site(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"
        description = ""
        desc_tag = soup.find("meta", attrs={"name": "description"})
        if desc_tag and "content" in desc_tag.attrs:
            description = desc_tag["content"]

        return {
            "title": title,
            "url": url,
            "description": description or "No description available."
        }

    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return None

# Sample seed list
seed_urls = [
    "https://en.wikipedia.org/wiki/Hanuman",
    "https://www.python.org",
    "https://example.com"
]

def crawl_and_save():
    results = []
    for url in seed_urls:
        data = crawl_site(url)
        if data:
            results.append(data)

    # Save to JSON
    with open("data.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    crawl_and_save()
    
