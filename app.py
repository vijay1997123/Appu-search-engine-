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
    return [
        {'title': 'Example Site 1', 'link': 'https://example.com/1', 'desc': 'This is a sample result'},
        {'title': 'Example Site 2', 'link': 'https://example.com/2', 'desc': 'Another example site'},
    ]
