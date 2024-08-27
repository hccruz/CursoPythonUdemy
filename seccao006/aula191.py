# requests para requisições HTTP no Python
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> porta:80
# https:// -> porta:443

url = "https://docs.python.org/3/"
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)
# print(response.json())
