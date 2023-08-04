#In the previous section, we used the wget function to retrieve 
# content from the web server as shown below. Write the python 
# code to perform the same task. The code should be the same as 
# the one used to download the image, but the file name should be 
# 'Example1.txt'.
import requests
import os 
from PIL import Image

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'

r = requests.get(url)
path = os.path.join(os.getcwd(),'Example1.txt')

with open(path,'wb') as f:
    f.write(r.content)
    
Image.open(path)