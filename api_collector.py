# Module to get the API data and preprocess it
import requests

def api_get(category):
    # Recives a category string: "location"; "character"; "episode"
    # Acess API and with GET query
    get_data = requests.get(f"https://rickandmortyapi.com/api/{category}/")
    
    results = []

    # Iterate untill all pages have been requested
    while get_data.status_code == 200: 
        # If request was successfull, parse as json
        get_data = get_data.json()
        # Save result and next page
        results += get_data["results"]
        next_page = get_data["info"]["next"]

        if next_page:
            # We get the next page from the request
            get_data = requests.get(next_page)
        # If all pages have been visited (next == null) return 
        else: 
            return results
    
    else: 
        # If not, return empty result, notify by print
        print(f"\nCould not access the API to get {category}...\n")
        return []

if __name__ == "__main__":
    pass
    import json
    # print(json.dumps(api_get("location"), indent=4))
    # print(json.dumps(api_get("character"), indent=4))
    # print(json.dumps(api_get("episode"), indent=4))

