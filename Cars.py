class Cars:
    name = ''
    model = ''
    company = ''
    date_of_manufacture =  ''
    engine =  ''
    isEngineon = False
    speed = 0
    gear = 0
    clutch = False

    def __init__(self, name, model, company, date_of_manufacture, engine, isEngineon, speed, gear, clutcher):
        self.name = name 
        self.model = model
        self.company = company
        self.date_of_manufacture = date_of_manufacture
        self.engine = engine
        self.isEngineon = isEngineon
        self.speed = speed 
        self.gear = gear
        self.clutch = clutcher
        
    def turn_engine(self):
        self.isEngineon = True
        self.display()
        print("")
        print("")
    
    def change_gears(self,n):
        self.clutchers()
        self.gear = self.gear + n
        print("gear:", self.gear)

    def brake(self):
        self.speed = self.speed - 2
        self.change_gears(-1)
        print("speed:", self.speed)
        
    def accelerate(self):
        self.speed = self.speed + 2
        self.change_gears(1)
        print("speed:", self.speed)

    def clutchers(self):
        
        if self.speed <= 0:
            self.clutch = False
            print("clutch:", self.clutch)
        elif self.speed >= 0:
            self.clutch = True
            print("clutch:", self.clutch)
        else:
            self.clutch = True
            print("clutch:", self.clutch)

    def blow_horn(self):
        print("pip pip")

    def display(self):
        print("name:", self.name)
        print("model:", self.model)
        print("company:", self.company)
        print("dateofmanufacture:", self.date_of_manufacture)
        print("engine:", self.engine)
        print("isEngineon:", self.isEngineon)
        print("speed:", self.speed)
        print("gear:", self.gear)
        print("clutch:", self.clutch)

if __name__ == "__main__":
    carry = Cars(name = "Mazda",model = "CX-9",company = "Mazda Motors Corporation",date_of_manufacture = "2019",engine = "Skyactiv-G engine", isEngineon = False, speed = 0, gear = 0, clutcher = False)
    carry.turn_engine()
    carry.accelerate()
    carry.brake()
    carry.blow_horn()
