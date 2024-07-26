import requests
response = requests.get("https://lust.scathach.id/youporn/search?key=sister&page=1")
print(response.status_code)
print(response.json()["data"])