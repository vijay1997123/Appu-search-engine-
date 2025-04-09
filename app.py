from flask import Flask, render_template, request

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
    # Dummy search logic – will replace later with real crawler
    return [
        {"title": "Appu Result 1", "link": "https://example.com/1", "snippet": "First dummy result for your query."},
        {"title": "Appu Result 2", "link": "https://example.com/2", "snippet": "Another dummy result with info."},
    ]

if __name__ == '__main__':
    app.run(debug=True)
