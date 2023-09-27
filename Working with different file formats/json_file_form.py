import json

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open('person.json', 'w') as f:
    json.dump(person, f)
    
json_object = json.dumps(person, indent = 4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)
    
print(json_object)

#Reading JSON to a file

with open('sample.json', 'r') as openfile:
    json_object = json.load(openfile)
    
print(json_object)
print(type(json_object))