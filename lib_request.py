import requests

url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/'
response = requests.get(url)
data = response.json()
for i in data:
    print(f' 1 {i['Ccy']}" = {i['Rate']} uzs')