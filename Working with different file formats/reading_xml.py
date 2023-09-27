import xml.etree.ElementTree as etree
import pandas as pd

tree = etree.parse("./Sample-employee-XML-file.xml")

root = tree.getroot()

columns = ["firstname", "lastname", "title", "division", "building","room"]

dataframe = pd.DataFrame(columns = columns)

for node in root:
    firstname = node.find("firstname").text
    
    lastname = node.find("lastname").text
    
    title = node.find("title").text 
    
    division = node.find("division").text 
    
    building = node.find("building").text
    
    room = node.find("room").text
    
    dataframe = dataframe.append(pd.Series([firstname, lastname, title, division, building, room], index = columns), ignore_index = True)

print(dataframe)

df = pd.read_xml("Sample-employee-XML-file.xml", xpath = "/employees/details")

#Saving Data

dataframe.to_csv("employee.csv", index = False)

#Read/Save to Other data Formats



