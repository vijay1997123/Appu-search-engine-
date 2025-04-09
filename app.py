from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import os  # Importing os for environment variable access

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results')
def results():
    query = request.args.get('q')
    results = search_function(query)
    return render_template('results.html', query=query, results=results)

def search_function(query):
    websites = [
        "https://en.wikipedia.org/wiki/Web_crawler",
        "https://www.geeksforgeeks.org/web-crawling-in-python/",
        "https://realpython.com/beautiful-soup-web-scraper-python/"
    ]

    results = []

    for site in websites:
        try:
            response = requests.get(site, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.title.string.strip() if soup.title else "No Title"
            desc_tag = soup.find('meta', attrs={'name': 'description'}) or soup.find('p')
            desc = desc_tag['content'].strip() if desc_tag and desc_tag.has_attr('content') else desc_tag.text.strip() if desc_tag else "No Description"

            if query.lower() in title.lower() or query.lower() in desc.lower():
                results.append({
                    'title': title,
                    'link': site,
                    'snippet': desc
                })

        except Exception as e:
            print(f"Error crawling {site}: {e}")

    if not results:
        results.append({
            'title': "No matching results found",
            'link': "#",
            'snippet': "Try a different keyword or wait for more crawling."
        })

    return results

# This is where the change should be made
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render sets the PORT environment variable
    app.run(host='0.0.0.0', port=port)  # Make sure the app listens on 0.0.0.0 and the correct port
