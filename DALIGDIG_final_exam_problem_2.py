# Parent Class
class Vehicle():
    wheels = None

    def __init__(self, wheels):
        self.wheels = wheels

    def display(self):
        print("\nThe vehicle has {} wheels.".format(self.wheels))

    def accelerate(self):
        print("It is now accelerating...")

# Child Class
class Car(Vehicle):
    brand = ''

    def __init__(self, brand, wheels):
        self.brand = brand
        Vehicle.__init__(self, wheels)

    def display(self):
        super().display()
        print("brand is {}.".format(self.brand))

# Child Class
class Motorcycle(Vehicle):
    brand = ''

    def __init__(self, brand, wheels):
        self.brand = brand
        Vehicle.__init__(self, wheels)

    def display(self):
        super().display()
        print("Brand is {}.".format(self.brand))

# Child of Car Class
class Estate(Car):
    model = ''
    gears = 0

    def __init__(self, model, gears, brand,  wheels):
        self.model = model
        self.gears = gears
        Car.__init__(self, brand, wheels)

    def display(self):
        super().display()
        print(" {} has {} gears.".format(self.model , self.gears))

# Child of Motorcycle Class 
class Scooter(Motorcycle):
    model = None
    gears = None
    
    def __init__(self, model, gears, brand, wheels):
        self.model = model
        self.gears = gears
        Motorcycle.__init__(self, brand, wheels)

    def display(self):
        super().display()
        print(" {} has {} gear.".format(self.model , self.gears))


if __name__ == "__main__":
    e = Estate(model="S", gears=5, wheels=4, brand="Tesla")
    e.display() # overrides
    e.accelerate()

    s = Scooter(model="Mio", gears=1, wheels=2, brand="Yamaha")
    s.display() # overrides
    s.accelerate()