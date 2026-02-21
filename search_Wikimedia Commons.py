import requests
import sys

cnt = 0 
query = sys.argv[1] # Данные с названием из основной части кода

def search_commons(query, limit=1):
    url = "https://commons.wikimedia.org/w/api.php"


    params = {
        "action": "query",  
        "format": "json",
        "list": "search",
        "srnamespace": 6,
        "srlimit": limit ,
        "srlanguage": "en",
        "srsearch": query
    }

    response = requests.get(url, params=params, 
                          headers={"User-Agent": "CourseworkBot/1.0"})
    return response.json()
##
result = search_commons(query)
print (result)
# 1. Извлекаем название файла
first_result = result["query"]["search"][0]
filename = first_result["title"]  # "File:Compiling in C-ar.svg"
clean_filename = filename.replace("File:", "")  # "Compiling in C-ar.svg"

print(f"Название файла: {clean_filename}")

# 2. Формируем URL для скачивания
download_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{clean_filename}"
print(f"URL для скачивания: {download_url}")

# 3. Скачиваем файл
headers = {"User-Agent": "CourseworkBot/1.0"}
response = requests.get(download_url, headers=headers)

# 4. Сохраняем
cnt += 1
save_as = f"{query} {cnt}"
with open(save_as, "wb") as f:
    f.write(response.content)

