class Cat:
    Mood=0
    Hungry=0
    Energy=0

    def __init__(self, Mood=Mood, Hungry=Hungry, Energy=Energy):
        self.Mood = Mood
        self.Hungry = Hungry
        self.Energy = Energy
    
    def sleep(self):
        self.Energy = self.Energy + 1
        self.Hungry = self.Hungry + 1
        self.display()

    def play(self):
        self.Mood = self.Mood + 1
        self.Energy = self.Energy - 1
        self.meow()
        self.display()

    def feed(self):
        self.Hungry = self.Hungry + 1 
        self.Mood = self.Mood + 1
        self.meow()
        self.display()

    def meow(self):
        print("meeeeow")

    def display(self):
        print("Mood:", self.Mood)
        print("Hungry:", self.Hungry)
        print("Energy:", self.Energy)
        print("Mood:", self.Mood)

if __name__ == "__main__":
    catty = Cat(Mood=0, Hungry=0, Energy=0)
    catty.feed()







