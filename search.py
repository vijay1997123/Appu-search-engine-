from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def search_db(query):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT url, title FROM pages WHERE title LIKE ?", ('%' + query + '%',))
    results = c.fetchall()
    conn.close()
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        query = request.form.get("query", "")
        results = search_db(query)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
  
