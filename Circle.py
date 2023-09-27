class Circle:
    # Attributes 
    radius = 1.0 
    color = "red"

    # Methods 
    def __init__(self, radius=radius, color=color):
        self.radius = radius
        self.color = color 

    def getRadius(self):
        return self.radius 

    def getColor(self):
        return self.color 

    def getArea(self):
        return 3.14 * self.radius**2

    def display(self):
        print("Radius: ", self.radius)
        print("Color: ", self.color)
        print("Area: ", self.getArea(), "\n")


if __name__ == "__main__":
    c1 = Circle(radius=2.0, color="blue")
    c2 = Circle(radius=2.0)
    c3 = Circle()
    
    c1.display()
    c2.display()
    c3.display()