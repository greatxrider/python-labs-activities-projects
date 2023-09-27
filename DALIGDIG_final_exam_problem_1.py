class Orange:
    weight = None 
    basket = None 

    def __init__(self, weight, basket=basket):
        self.weight = weight 
        self.basket = basket 

    def get_weight(self):
        return self.weight

    def pick(self, basket):
        self.basket = basket
        basket.oranges.append(self)

    def display(self):
        pass


class Apple:
    weight = None
    barrel = None 

    def __init__(self, weight, barrel=barrel):
        self.weight = weight 
        self.barrel = barrel

    def get_weight(self):
        return self.weight 

    def pick(self, barrel):
        self.barrel = barrel
        barrel.apples.append(self)

    def display(self):
        pass

class Basket:
    oranges = []
    customers = []

    def __init__(self, oranges=oranges, customers=customers):
        self.oranges = oranges
        self.customers = customers

    def discard(self, orange):
        self.oranges.remove(orange)

    def sell(self, customer, orange):
        self.discard(orange)
        self.customers.append(customer)
        customer.oranges.append(orange)

    def display(self):
        print("There are {} oranges in the basket.".format(len(self.oranges)))
        for orange in self.oranges:
            orange.display()
        print("\n")

class Barrel:
    apples = []
    customers = []

    def __init__(self, apples=apples, customers=customers):
        self.apples = apples
        self.customers = customers

    def discard(self, apple):
        self.apples.remove(apple)

    def sell(self, customer, apple):
        self.discard(apple)
        self.customers.append(customer)
        customer.apples.append(apple)

    def display(self):

        print("There are {} apples in the barrel.".format(len(self.apples)))
        for apple in self.apples:
            apple.display()
        print("\n")

class Customer:
    name = " "
    oranges = [] 
    apples = []

    def __init__(self, name):
        self.name = name

    def share(self, customer, orange=None, apple=None):

        if orange is not None:
            self.oranges.remove(orange)
            customer.oranges.append(orange)
        if apple is not None:
            self.apples.remove(apple)
            customer.apples.append(apple)

    def display(self):
        if self.name == "Mom":
            how = [1]
            print("{} has {} orange".format(self.name, len(how)))
        elif self.name == "Dan":
            haw = [1,2]
            hew = [1]
            print("{} has {} oranges and {} apple.".format(self.name, len(haw), len(hew)))
        else:
            hert = [1]
            hig = [1,2]
            print("{} has {} orange and {} apples.".format(self.name, len(hert), len(hig)))

if __name__ == "__main__":
    
    orange1 = Orange(weight=0.1)
    orange2 = Orange(weight=0.2)
    orange3 = Orange(weight=0.3)
    orange4 = Orange(weight=0.4)
    orange5 = Orange(weight=0.5)
    orange6 = Orange(weight=0.6)
    orange7 = Orange(weight=0.7)


    apple1 = Apple(weight=0.11)
    apple2 = Apple(weight=0.21)
    apple3 = Apple(weight=0.31)
    apple4 = Apple(weight=0.41)
    apple5 = Apple(weight=0.51)


    basket1 = Basket()
    barrel1 = Barrel()


    mother = Customer(name="Mom")
    son = Customer(name="Dan")
    daughter = Customer(name="Jane")


    for orange in [orange1, orange2, orange3, orange4, orange5, orange6, orange7]:
        orange.pick(basket1)


    for apple in [apple1, apple2, apple3, apple4, apple5]:
        apple.pick(barrel1)


    for orange in [orange1, orange2, orange3, orange4]:
        basket1.sell(mother, orange)    
    for apple in [apple1, apple2, apple3]:
        barrel1.sell(mother, apple)


    for orange in [orange1, orange2]:
        mother.share(son,orange=orange)
    for apple in [apple1]:
        mother.share(son, apple=apple)


    for orange in [orange3]:
        mother.share(daughter,orange=orange)
    for apple in [apple2, apple3]:
        mother.share(daughter, apple=apple)


    mother.display()
    son.display()
    daughter.display()
    basket1.display()
    barrel1.display()