from bs4 import BeautifulSoup
import requests

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

z = two_tables_bs.find("table")
print(z)

x = two_tables_bs.find("table", class_ = "pizza")
print(x)

url = "http://www.ibm.com"

data = requests.get(url).text

soup = BeautifulSoup(data, "html5lib")

for link in soup.find_all('a', href = True):
    print(link.get('href'))

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))

#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data  = requests.get(url).text
soup1 = BeautifulSoup(data,"html5lib")

table = soup1.find('table')

for row in table.find_all('tr'): 
    cols = row.find_all('td') 
    color_name = cols[2].string 
    color_code = cols[3].text 
    print("{}--->{}".format(color_name,color_code))