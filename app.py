from flask import Flask, render_template, request, jsonify
import search

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

# This is the route your search.html is trying to call
@app.route("/api/search")
def api_search():
    query = request.args.get("q", "")
    results = search.search_web(query)  # make sure your search.py has this function
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
    
