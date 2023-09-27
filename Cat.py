class Cat:
    # Attributes 
    mood = 0 
    hungry = 0 
    energy = 0

    # Methods
    def __init__(self, mood=mood, hungry=hungry, energy=energy):
        self.mood = mood 
        self.hungry = hungry 
        self.energy = energy
    
    def meow(self):
        print("meow!")
    
    def sleep(self):
        self.energy += 1
        self.hungry += 1
        self.display() 

    def play(self):
        self.mood += 1
        self.energy -= 1
        self.meow()
        self.display()

    def feed(self):
        self.hungry -= 1
        self.mood += 1
        self.meow()
        self.display()


    def display(self):
        print("Mood: ", self.mood)
        print("Energy: ", self.energy)
        print("Hungry: ", self.hungry)
        print() # enter new space

if __name__ == "__main__":
    Garfield = Cat()
    Garfield.sleep()
    Garfield.feed()
    Garfield.play()