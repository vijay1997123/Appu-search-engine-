import sqlite3
import sys

def search(query):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    # Search for the query in title and content (case-insensitive)
    cursor.execute("SELECT url, title FROM pages WHERE title LIKE ? OR content LIKE ?", 
                   (f"%{query}%", f"%{query}%"))
    
    results = cursor.fetchall()
    conn.close()

    return results

# For testing directly
if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = " ".join(sys.argv[1:])
        matches = search(q)
        for url, title in matches:
            print(f"{title}\n{url}\n")
    else:
        print("Please enter a search query.")
        
