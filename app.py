import requests

url = "https://weatherapi-com.p.rapidapi.com/timezone.json"

querystring = {"q":"<REQUIRED>"}

headers = {
    'x-rapidapi-key': "{x-rapidapi-key}",
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
