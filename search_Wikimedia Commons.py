import requests

def search_commons(query, limit=1):
    # 1. Базовый URL API
    url = "https://commons.wikimedia.org/w/api.php"


    params = {
        "action": "query",  
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srnamespace": 6,
        "srlimit": limit         
    }

    response = requests.get(url, params=params, 
                          headers={"User-Agent": "CourseworkBot/1.0"})
    
    return response.json()

result = search_commons("software diagram", limit=1)
    
print(result)
