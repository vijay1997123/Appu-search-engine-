import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad responses (4xx, 5xx)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Example: Get all the links in the page
    links = soup.find_all('a', href=True)
    return links

def crawl(url):
    print(f"Crawling URL: {url}")
    html = fetch_page(url)
    if html:
        links = parse_page(html)
        print(f"Found {len(links)} links.")
        # You can now add the links to your index or process them
        for link in links:
            print(link['href'])

if __name__ == "__main__":
    starting
  
