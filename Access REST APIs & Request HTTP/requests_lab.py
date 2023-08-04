#RequestsinPython
import requests
import os 
from PIL import Image
from IPython.display import IFrame

url = 'https://www.ibm.com/'
r = requests.get(url)

# Status code
S = r.status_code
print(S)
#request Headers
print(r.request.headers)
#request body
print("request body:", r.request.body)
#response headers
header = r.headers
print(r.headers)

#header_date
print('This is header date',header['date'])

#content-type
print('this is encoding:', r.encoding)

#show attribute text to display the HTML in the body
print('html in body', r.text[0:100])

#non-text requests (images)
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

#get-request
r = requests.get(url)
print('headers of non-text requests', r.headers)
print('content type of the non text',r.headers['Content-Type'])
path=os.path.join(os.getcwd(),'IDSNlogo.png')

with open(path,'wb') as f:
    f.write(r.content)
    
Image.open(path)






