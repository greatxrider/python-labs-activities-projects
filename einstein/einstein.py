#Jeph Mari Daligdig - Einstein
#Problem set 0

def convert(userInput):
    mass = int(userInput)
    c = 300000000
    E = mass*(c**2)
    return E

userInput = input("Please enter any value of mass m: ")
print(convert(userInput))