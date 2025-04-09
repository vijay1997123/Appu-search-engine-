@app.route("/search")
def search():
    query = request.args.get("q", "")
    print("Query received:", query)  # Debug

    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT url, title FROM pages WHERE title LIKE ?", ('%' + query + '%',))
    results = c.fetchall()
    conn.close()

    print("Results found:", results)  # Debug
    return render_template("search.html", results=results, query=query)
