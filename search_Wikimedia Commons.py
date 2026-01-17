import requests

def search_commons(query, limit=10):
    # 1. Базовый URL API
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
result = search_commons("C++ compilers",)
print (result)
# 1. Извлекаем название файла
first_result = result["query"]["search"][0]
filename = first_result["title"]  # "File:Compiling in C-ar.svg"
clean_filename = filename.replace("File:", "")  # "Compiling in C-ar.svg"

print(f"Название файла: {clean_filename}")

# 2. Формируем URL для скачивания
download_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{clean_filename}"
print(f"🔗 URL для скачивания: {download_url}")

# 3. Скачиваем файл
headers = {"User-Agent": "CourseworkBot/1.0"}
response = requests.get(download_url, headers=headers)

# 4. Сохраняем
save_as = "compiling_diagram.svg"
with open(save_as, "wb") as f:
    f.write(response.content)

#print(f"Файл сохранён как: {save_as} ({len(response.content)} байт)")
