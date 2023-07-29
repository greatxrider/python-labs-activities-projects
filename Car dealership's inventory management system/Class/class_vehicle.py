# Jeph Mari Daligdig

class Vehicle:
    color = "White"

    def __init__(self, maximum_speed, mileage):
        self.maximum_speed = maximum_speed
        self.mileage = mileage
        
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    def display_properties(self):
        print("Properties of the vehicle: ")
        print("Color: ", self.color)
        print("Maximum Speed: ", self.maximum_speed)
        print("Mileage: ", self.mileage)	
        print("Seating Capacity: ", self.seating_capacity)