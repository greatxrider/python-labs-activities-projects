#Jeph Mari Daligdig
# Car dealership's inventory management system

from Class.class_vehicle import Vehicle

#Vehicle 1 with 200 kph and 1000 mileage

vehicle_1 = Vehicle(200, 1000)
vehicle_1.assign_seating_capacity(5)
vehicle_1.display_properties()

#Vehicle 2 with 180 kph and 7500 mileage

vehicle_2 = Vehicle(180, 7500)
vehicle_2.assign_seating_capacity(4)
vehicle_2.display_properties()