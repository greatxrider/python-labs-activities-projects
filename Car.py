class Car:
    name = ''
    model = ''
    company = ''
    date_of_manufacture = ''
    engine = ''
    isEngineOn = False 
    speed = 0
    gear = 0
    _clutch = False 

    def __init__(self,name,model,company,date_of_manufacture,engine,isEngineOn=isEngineOn,speed=speed,gear=gear,_clutch=_clutch):
        self.name = name 
        self.model = model
        self.company = company 
        self.date_of_manufacture = date_of_manufacture
        self.engine = engine 
        self.isEngineOn = isEngineOn
        self.speed = speed 
        self.gear = gear 
        self._clutch = _clutch

    def turn_engine(self):
        self.isEngine = True 
        print("The engine is ON.\n")

    def brake(self):
        self.speed -= 2
        self.change_gears(-1)
        print("Speed = {}\n".format(self.speed))
    
    def accelerate(self):
        self.speed += 2
        self.change_gears(1)
        print("Speed = {}\n".format(self.speed))
    
    def clutch(self):
        self._clutch = not(self._clutch) 
        print("Clutch = {}".format(self._clutch))

    def change_gears(self, n):
        self.clutch()
        print("Gear = {}".format(self.gear))
        self.gear = self.gear + n
        self.clutch()
        print("Gear = {}".format(self.gear)) 

    def blow_horn(self):
        print("pip pip! \n")   

if __name__ == "__main__":
    Tesla = Car(name="Tesla",model="ModelS",company="Tesla",date_of_manufacture="2018",engine='sample')
    Tesla.turn_engine()
    Tesla.accelerate()
    Tesla.blow_horn()
    Tesla.brake()