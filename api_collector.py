# Module to get the API data and preprocess it
import requests
import json

def api_get(category):
    # Recives a category string: "location"; "character"; "episode"
    # Acess API and returns JSON
    get_data = requests.get(f"https://rickandmortyapi.com/api/{category}/")
    
    if get_data.status_code == 200:   
        # If request was successfull, return json response
        return get_data.json()["results"]
    
    else: 
        # If not, return empty result, notify by print
        print(f"\nCould not access the API to get {category}...\n")
        return []

if __name__ == "__main__":
    pass
    # print(json.dumps(api_get("location"), indent=4, sort_keys=True))
    # print(json.dumps(api_get("character"), indent=4, sort_keys=True))
    # print(json.dumps(api_get("episode"), indent=4, sort_keys=True))

