#
# DICTIONARY
#

# Creating a Dictionary (1)
thisdict = {"brand": "Ford",
            "model":"Mustang",
            "year": 1964}
print(thisdict)

# Creating a Dictionary (2)
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

# Accessing the items
x = thisdict["model"]
y = thisdict.get("model")
print(x,y)

# Change values
thisdict["year"] = 2018
print(thisdict)

# Loop (1): Print all key names
for x in thisdict:
    print(x, end=" ")

# Loop (2): Print all values
for y in thisdict:
    print(thisdict[y], end=" ")

# Loop (3): Using values()
for y in thisdict.values():
    print(y)

# Loop (4): Using items() to loop thru keys and values
for x, y in thisdict.items():
    print(x,y)


# Length
print(len(thisdict))

# Adding items
thisdict["color"] = "red"
print(thisdict)


# Removing items (1): pop()
thisdict = dict(brand="Ford", model="Mustang", year=1964)
thisdict.pop("model")
print(thisdict)

# Removing items (2): del
thisdict = dict(brand="Ford", model="Mustang", year=1964)
del thisdict["model"]
print(thisdict)

# What is the difference between pop() and del


# Removing items (3): popitem()
thisdict = dict(brand="Ford", model="Mustang", year=1964)
thisdict.popitem()
print(thisdict)

# Removing items (4): clear()
thisdict = dict(brand="Ford", model="Mustang", year=1964)
thisdict.clear()
print(thisdict)


#
#
#   CHALLENGES
#
#

# Challenge 1
# Create a dictionary called "car1" with the following parameters
# brand = "Ford"
# model = "EcoSport"
# year = 2014

# Challenge 2
# Create a dictionary called "car2" with the following parameters
# brand = "Mazda"
# model = "CX-3"
# year = 2019

# Challenge 3
# Create a dictionary called "cars" that contains both "car1" and "car2"

# Challenge 4
# Create a dictionary called "motorcycle1" with the ff. parameters
# brand = "Yamaha"
# model = "Sniper"
# year = 2015

# Challenge 5
# Create a dictionary called "motorcycles" that contains "motorcycle1"

# Challenge 6
# Create a dictionary called "vehicles" that contains both "cars" and "motorcycles"

# Challenge 7
# Access all models of the cars from "vehicles"

# Challenge 8
# Create "motorcycle2" with ff. parameters:
# brand = "Suzuki"
# model = "Raider"
# year = 2012
# Then add it to "vehicles"

# Challenge 9
# Access all brands of the motorcycles from "vehicles"

# Challenge 10
# Change released year for Raider from 2012 to 2011 from "vehicles"



#
#
#   ANSWERS TO CHALLENGES
#
#
# Challenge 1
# Create a dictionary called "car1" with the following parameters
# brand = "Ford"
# model = "EcoSport"
# year = 2014
car1 = dict(brand="Ford", model="EcoSport", year=2014)
print("car1 = ", car1)


# Challenge 2
# Create a dictionary called "car2" with the following parameters
# brand = "Mazda"
# model = "CX-3"
# year = 2019
car2 = dict(brand="Mazda", model="CX-3", year=2019)
print("car2 = ", car2)

# Challenge 3
# Create a dictionary called "cars" that contains both "car1" and "car2"
cars = dict()
cars['1'] = car1
cars['2'] = car2
print("cars = ", cars)

# Challenge 4
# Create a dictionary called "motorcycle1" with the ff. parameters
# brand = "Yamaha"
# model = "Sniper"
# year = 2015
motorcycle1 = dict(brand="Yamaha", model="Sniper", year=2015)
print("motorcycle1 = ", motorcycle1)

# Challenge 5
# Create a dictionary called "motorcycles" that contains "motorcycle1"
motorcycles = dict()
motorcycles["1"] = motorcycle1
print("motorcycles = ", motorcycles)

# Challenge 6
# Create a dictionary called "vehicles" that contains both "cars" and "motorcycles"
vehicles = dict(cars=cars, motorcycles=motorcycles)
print("vehicles = ", vehicles)

# Challenge 7
# Access all models of the cars from "vehicles"
# 1
car_models = [car.get("model") for car in vehicles.get("cars").values()]
print(car_models)
# 2
for car in vehicles.get("cars").values():
    print(car.get("model"), end=" ")

# Challenge 8
# Create "motorcycle2" with ff. parameters:
# brand = "Suzuki"
# model = "Raider"
# year = 2012
# Then add it to "vehicles"
motorcycle2 = dict(brand="Suzuki", model="Raider", year=2012)
vehicles["motorcycles"]['2'] = motorcycle2
print(vehicles)

# Challenge 9
# Access all brand of the motorcycles from "vehicles"
# 1
motor_brands = [motorcycle.get("brand") for motorcycle in vehicles.get("motorcycles").values()]
print(motor_brands)
# 2
for motorcycle in vehicles.get("motorcycles").values():
    print(motorcycle.get("brand"), end=" ")

# Challenge 10
# Change released year for Raider from 2012 to 2011 from "vehicles"
vehicles["motorcycles"]["2"]["year"] = 2013
print(vehicles)
