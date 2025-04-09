import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()

def fetch_page(url):
    try:
        response = requests.get(url)
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
            print(link)
            # You can crawl deeper if needed
            # crawl(link)

if __name__ == "__main__":
    crawl("https://example.com")
    
