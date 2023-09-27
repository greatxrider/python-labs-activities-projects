class Vehicle():
    wheels = None
    def __init__(self, wheels):
        self.wheels = wheels

    def accelerate(self):
        print("{} is now Accelerating....".format(self.brand))
        
    def display(self):
        if self.wheels == 4:
            print("This Car has {} wheels.".format(self.wheels))
        elif self.wheels ==2:
            print("This Motorcycle has {} wheels.".format(self.wheels))

class Car(Vehicle):
    brand = ""
    def __init__(self, brand, wheels):
        self.brand = brand
        Vehicle.__init__(self, wheels)

    def display(self):
        super().display()
        print("The Brand is {}.".format(self.brand))

class Estate(Car):
    model =  None
    gears = None
    def __init__(self, model, gears, brand,  wheels):
        self.model = model
        self.gears = gears
        Car.__init__(self, brand, wheels)

    def display(self):
        super().display()
        print("The Model is {} and it has {} gears.".format(self.model , self.gears))

class Motorcycle(Vehicle):
    brand = ""
    def __init__(self, brand, wheels):
        self.brand = brand
        Vehicle.__init__(self, wheels)
    def display(self):
        super().display()
        print("The Brand is {}.".format(self.brand))

class Scooter(Motorcycle):
    model = None
    gears = None
    def __init__(self, model, gears, brand, wheels):
        self.model = model
        self.gears = gears
        Motorcycle.__init__(self, brand, wheels)

    def display(self):
        super().display()
        print("The Model is {} and it has {} gears.".format(self.model, self.gears))

if __name__ == "__main__":
    car = Estate(model = "S", gears = 5, brand = "Kariton F540" , wheels = 4)
    car.display()
    car.accelerate()
    print("")
    print("")

    motorcycle = Scooter(model = "Mio", gears = 5, brand = "Sikad S1450" , wheels = 2)
    motorcycle.display()
    motorcycle.accelerate()
    

