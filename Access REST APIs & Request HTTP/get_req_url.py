#Get Request with URL Parameters
#Query string 
import requests

url_get='http://httpbin.org/get'
payload = {"name": "Joseph", "ID": "123"}
r = requests.get(url_get, params=payload)
print(r.url)
print("request body:", r.request.body)
print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])

