from flask import Flask, request, jsonify
from your_crawler_module import search_function  # Use your crawler's function

app = Flask(__name__)

@app.route('/api/search')
def search_api():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])

    results = search_function(query)  # Example: list of {title, url, description}
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
    
