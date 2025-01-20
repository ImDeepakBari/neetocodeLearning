"""
Modify the car class to encapsulate the brand attribute , making it private and provide a getter method for it.
"""

from class_basic import Car

mynew_car = Car("Tata", "Creta")
print(mynew_car.model)

print("Accessing private attributes: ", mynew_car.get_car_color())