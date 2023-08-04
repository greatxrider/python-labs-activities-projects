#Get Request with URL Parameters
#Query string 
import requests
import os 
from PIL import Image
from IPython.display import IFrame

url_post='http://httpbin.org/post'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_post,params=payload)

r_post=requests.post(url_post,data=payload)

print("POST request URL:",r_post.request.body )
print(r_post.json()['form'])
print(r.url)