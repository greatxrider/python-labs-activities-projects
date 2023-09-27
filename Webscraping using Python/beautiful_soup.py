from bs4 import BeautifulSoup
import requests

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')

print(soup.prettify())

tag_object = soup.title
print("tag object:", tag_object)
print("tag object type:",type(tag_object))

tag_object = soup.h3
print("tag object:", tag_object)

tag_child = tag_object.b
print("tag child:", tag_child)

parent_tag = tag_child.parent
print("parent tag:", parent_tag)

print(tag_object.parent)

sibling_1 = tag_object.next_sibling
print("sibling of tag object:", sibling_1)

sibling_2 = sibling_1.next_sibling
print("sibling of tag object:", sibling_2)

# Exercise
# Use the object sibling_2 and the method next_sibling 
# to find the salary of Stephen Curry:

next_sibling = sibling_2.next_sibling
print("next sibling:", next_sibling)

print('Attirubtes of b',tag_child['id'])

print(tag_child.attrs)

print(tag_child.get('id'))

tag_string = tag_child.string
print("tag string:", tag_string)

print(tag_string)

unicode_string = str(tag_string)
print("unicode string:", unicode_string)