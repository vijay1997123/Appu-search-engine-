import requests
from bs4 import BeautifulSoup
import sqlite3
from urllib.parse import urljoin, urlparse

# Connect to SQLite DB
conn = sqlite3.connect("data/pages.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS pages (
    url TEXT PRIMARY KEY,
    title TEXT,
    content TEXT
)
""")
conn.commit()

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def crawl(url, visited=set()):
    if url in visited:
        return
    print(f"Crawling: {url}")
    visited.add(url)
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No Title"
        content = soup.get_text()

        # Store in DB
        cursor.execute("INSERT OR IGNORE INTO pages (url, title, content) VALUES (?, ?, ?)", (url, title, content))
        conn.commit()

        # Extract and crawl internal links
        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link['href'])
            if is_valid(full_url) and "http" in full_url:
                crawl(full_url, visited)
    except Exception as e:
        print(f"Failed to crawl {url}: {e}")

# Start point
start_url = "https://example.com"
crawl(start_url)

conn.close()
            
