#filter
from bs4 import BeautifulSoup
import requests

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')
print(table_bs.prettify())

#find_all

table_rows = table_bs.find_all('tr')
print("table rows:", table_rows)

first_row = table_rows[0]
print("first row:", first_row)

print(type(first_row))

print(first_row.td)

for i,row in enumerate(table_rows):
    print("row",i,"is",row)
    
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)
        
list_input=table_bs.find_all(name=["tr", "td"])
print("list input:", list_input)


#Attributes
z = table_bs.find_all(id="flight")
print(z)

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print("list input:", list_input)

x = table_bs.find_all(href=True)
print(x)

#Exercise

print("Without Href",table_bs.find_all(href=False))

#Find element with id attribute set to the boldest
print("Boldest:", table_bs.find_all(id="boldest"))

#elements with florida

print("Florida:", table_bs.find_all(string="Florida"))