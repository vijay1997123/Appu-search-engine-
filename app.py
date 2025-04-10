from flask import Flask, jsonify, request, send_from_directory
import json

app = Flask(__name__)

# Serve HTML file
@app.route("/search.html")
def search_page():
    return send_from_directory("static", "search.html")

# API to fetch data.json results
@app.route("/api/search")
def api_search():
    query = request.args.get("q", "").lower()
    results = []

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            for item in data:
                if query in item["title"].lower() or query in item["description"].lower():
                    results.append(item)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
    
