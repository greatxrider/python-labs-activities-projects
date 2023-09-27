# Parent1 Class
class Vehicle():
    wheels = None 

    def __init__(self, wheels):
        self.wheels = wheels

    def display(self):
        print("The vehicle has {} wheels.".format(self.wheels))

# Parent2 Class
class Asset(Vehicle):
    price = None 
    def __init__(self, price, wheels):
        self.price = price 
        Vehicle.__init__(self,wheels)

    def display(self):
        print("The asset is worth {} pesos.".format(self.price))

# Child Class
class Car(Asset):
    brand = None 
    def __init__(self, brand, price, wheels):
        self.brand = brand 
        Asset.__init__(self, price, wheels)

    def display(self):
        super().display()
        print("Brand is {}.".format(self.brand))

# Child of Car Class
class Estate(Car):
    model = ''
    gears = 0

    def __init__(self, model,gears, wheels,brand, price,):
        self.model = model
        self.gears = gears
        Car.__init__(self, brand, price, wheels)

    def display(self):
        super().display()
        print("{} has {} gears.".format(self.model, self.gears))


if __name__ == "__main__":
    e = Estate("S",5,4,"Tesla",3000000)
    e.display()

