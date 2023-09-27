class Orange:
    weight = None
    basket = None

    def __init__(self, weight, basket):
        self.weight = weight
        self.basket = basket

    def get_weight(self):
        return self.weight
    
    def pick(self, basket):
        self.basket = basket
        basket.oranges.append(self)

    def display(self):

        if self.weight==1:
            print("Orange1 is {} kg.".format(self.get_weight()))
        if self.weight==2:
            print("Orange2 is {} kg.".format(self.get_weight()))
        if self.weight==3:
            print("Orange3 is {} kg.".format(self.get_weight()))
        if self.weight==4:
            print("Orange4 is {} kg.".format(self.get_weight()))
        if self.weight==5:
            print("Orange5 is {} kg.".format(self.get_weight()))
        if self.weight==6:
            print("Orange6 is {} kg.".format(self.get_weight()))
        if self.weight==7:
            print("Orange7 is {} kg.".format(self.get_weight()))


class Apple:
    weight = None
    barrel = None

    def __init__(self, weight, barrel):
        self.weight = weight
        self.barrel = barrel
    
    def get_weight(self):
        return self.weight

    def pick(self, barrel):
        self.barrel = barrel
        barrel.apples.append(self)

    def display(self):
        if self.weight==1:
            print("Apple1 is {} kg.".format(self.get_weight()))
        if self.weight==2:
            print("Apple2 is {} kg.".format(self.get_weight()))
        if self.weight==3:
            print("Apple3 is {} kg.".format(self.get_weight()))
        if self.weight==4:
            print("Apple4 is {} kg.".format(self.get_weight()))
        if self.weight==5:
            print("Apple5 is {} kg.".format(self.get_weight()))

class Barrel:
    apples = []
    customers = []

    def __init__(self, apples=apples):
        self.apples = apples
    
    def discard(self, apple):
        self.apples.remove(apple)
        
    def sell(self, customer, apple):
        self.customers.append(customer)
        customer.apples.append(apple)
        self.discard(apple)

    def display(self):
        print("There are {} apples in the barrel. ".format(len(self.apples)))
        for apples in self.apples:
            apples.display()
        print("")
        print("")

class Basket:
    oranges = []
    customers = []

    def __init__(self, oranges=oranges):
        self.oranges = oranges
    
    def discard(self, orange):
        self.oranges.remove(orange)

    def sell(self, customer, orange):
        self.customers.append(customer)
        customer.oranges.append(orange)
        self.discard(orange)

    def display(self):
        print("There are {} oranges in the basket. ".format(len(self.oranges)))
        for orange in self.oranges:
            orange.display()
        print("")
        print("")

class Customer1:
    name = ""
    oranges = []
    apples = []
    customers = []

    def __init__(self, name, oranges=oranges, apples=apples):
        self.oranges = oranges
        self.apples = apples
        self.name = name

    def display(self):
        if len(self.apples)==0:
            print("{} has {} oranges ".format(self.name, len(self.oranges)))
        elif len(self.apples)>0:
            print("{} has {} oranges".format(self.name, len(self.oranges)),"and {} apples. ".format(len(self.apples)))
        for orange in self.oranges:
            orange.display()
        for apple in self.apples:
            apple.display()
        print("")
        print("")

    def discard_Orange(self, orange):
        self.oranges.remove(orange)
        
    def discard_Apple(self, apple):
        self.apples.remove(apple)

    def share(self, customer,apple=None, orange=None):
        if orange is not None:
            self.customers.append(customer)
            customer.oranges.append(orange)
            self.discard_Orange(orange)
        if apple is not None:
            self.customers.append(customer)
            customer.apples.append(apple)
            self.discard_Apple(apple)

class Customer2:
    name = ""
    oranges = []
    apples = []
    customers = []

    def __init__(self, name, oranges=oranges, apples=apples):
        self.oranges = oranges
        self.apples = apples
        self.name = name
    
    def display(self):
        if len(self.apples)==0:
            print("{} has {} oranges ".format(self.name, len(self.oranges)))
        elif len(self.apples)>0:
            print("{} has {} oranges".format(self.name, len(self.oranges)),"and {} apples. ".format(len(self.apples)))
        for orange in self.oranges:
            orange.display()
        for apple in self.apples:
            apple.display()
        print("")
        print("")

    def discard_Orange(self, orange):
        self.oranges.remove(orange)

    def discard_Apple(self, apple):
        self.apples.remove(apple)

    def share(self, customer,apple=None, orange=None):
        if orange is not None:
            self.customers.append(customer)
            customer.oranges.append(orange)
            self.discard_Orange(orange)
        if apple is not None:
            self.customers.append(customer)
            customer.apples.append(apple)
            self.discard_Apple(apple)

class Customer3:
    name = ""
    oranges = []
    apples = []
    customers = []

    def __init__(self, name, oranges=oranges, apples=apples):
        self.oranges = oranges
        self.apples = apples
        self.name = name
    
    def display(self):
        if len(self.apples)==0:
            print("{} has {} oranges ".format(self.name, len(self.oranges)))
        elif len(self.apples)>0:
            print("{} has {} oranges".format(self.name, len(self.oranges)),"and {} apples. ".format(len(self.apples)))
        for orange in self.oranges:
            orange.display()
        for apple in self.apples:
            apple.display()
        print("")
        print("")

    def discard_Orange(self, orange):
        self.oranges.remove(orange)

    def discard_Apple(self, apple):
        self.apples.remove(apple)

    def share(self, customer,apple=None, orange=None):
        if orange is not None:
            self.customers.append(customer)
            customer.oranges.append(orange)
            self.discard_Orange(orange)
        if apple is not None:
            self.customers.append(customer)
            customer.apples.append(apple)
            self.discard_Apple(apple)


if __name__ == "__main__":

    basket = Basket()
    orange1 = Orange(1,basket)
    orange2 = Orange(2,basket)
    orange3 = Orange(3,basket)
    orange4 = Orange(4,basket)
    orange5 = Orange(5,basket)
    orange6 = Orange(6,basket)
    orange7 = Orange(7,basket)
    for orange in [orange1, orange2, orange3, orange4, orange5, orange6, orange7]:
        orange.pick(basket)
    basket.display()

    barrel = Barrel()
    apple1 = Apple(1, barrel)
    apple2 = Apple(2, barrel)
    apple3 = Apple(3, barrel)
    apple4 = Apple(4, barrel)
    apple5 = Apple(5, barrel)
    for apple in [apple1,apple2,apple3,apple4,apple5]:
        apple.pick(barrel)
    barrel.display()

    customer1 = Customer1("Jeph")
    customer2 = Customer2("Leonidas")
    customer3 = Customer3("Goku")


    for orange in [orange1, orange2, orange3, orange4]:
        basket.sell(customer1, orange)
    for apple in [apple1, apple2, apple3, apple4]:
        barrel.sell(customer1, apple)
    customer1.display()

    for orange in [orange1, orange2]:
        customer1.share(customer2, orange=orange)
    for apple in [apple1]:
        customer1.share(customer2, apple=apple)
    customer2.display()

    for orange in [orange3]:
        customer1.share(customer3, orange=orange)
    for apple in [apple2, apple3]:
        customer1.share(customer3, apple=apple)
    customer3.display()

    basket.display()
    barrel.display()
    customer1.display()



    


    


    