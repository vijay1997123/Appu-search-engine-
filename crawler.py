import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Simple in-memory index
index = []

def crawl(url, depth=1):
    if depth == 0 or not url.startswith("http"):
        return

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else url
        description = soup.meta.get('content') if soup.find('meta', attrs={"name": "description"}) else "No description"
        
        index.append({
            "title": title,
            "url": url,
            "description": description
        })

        # Crawl links inside the page
        for link_tag in soup.find_all('a', href=True):
            link = urljoin(url, link_tag['href'])
            # Stay within same domain
            if urlparse(link).netloc == urlparse(url).netloc:
                crawl(link, depth=depth-1)

    except Exception as e:
        print("Failed to crawl:", url, str(e))

def build_index(start_url):
    global index
    index = []  # clear index
    crawl(start_url, depth=2)
    return index

def search_function(query):
    results = []
    for item in index:
        if query.lower() in item['title'].lower() or query.lower() in item['description'].lower():
            results.append(item)
    return results
    
