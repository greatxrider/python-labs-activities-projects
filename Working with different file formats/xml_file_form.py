#XML file format

import xml.etree.ElementTree as ET

employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

mydata1 = ET.ElementTree(employee)

with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

print(mydata1)