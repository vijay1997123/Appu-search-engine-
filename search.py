import json

def search_web(query):
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    # Match title or description with query
    results = []
    for item in data:
        if query.lower() in item["title"].lower() or query.lower() in item["description"].lower():
            results.append(item)
    return results
    
