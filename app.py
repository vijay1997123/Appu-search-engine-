from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        results = search_web(query)
    return render_template('index.html', results=results)

def search_web(query):
    search_url = f"https://www.bing.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for result in soup.select(".b_algo"):
        title = result.select_one("h2")
        link = title.a["href"] if title and title.a else ""
        desc = result.select_one(".b_caption p")
        if title and link:
            results.append({
                "title": title.get_text(strip=True),
                "link": link,
                "desc": desc.get_text(strip=True) if desc else ""
            })
    return results
    
