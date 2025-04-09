import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sqlite3
import os

visited = set()

# DB setup
def init_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pages
                 (url TEXT UNIQUE, title TEXT)''')
    conn.commit()
    conn.close()

def save_to_db(url, title):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    try:
        c.execute("INSERT OR IGNORE INTO pages (url, title) VALUES (?, ?)", (url, title))
        conn.commit()
    except Exception as e:
        print("DB Error:", e)
    finally:
        conn.close()

def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_page(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for a_tag in soup.find_all('a', href=True):
        absolute_url = urljoin(base_url, a_tag['href'])
        links.add(absolute_url)
    title = soup.title.string.strip() if soup.title else "No Title"
    save_to_db(base_url, title)
    return links

def crawl(url):
    if url in visited:
        return
    print(f"Crawling: {url}")
    visited.add(url)
    html = fetch_page(url)
    if html:
        links = parse_page(html, url)
        print(f"Found {len(links)} links.")
        for link in links:
            crawl(link)  # optional: limit depth here

if __name__ == "__main__":
    init_db()
    crawl("https://example.com")
    
