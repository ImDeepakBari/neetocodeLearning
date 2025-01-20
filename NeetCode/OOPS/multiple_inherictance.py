"""
Create a car class and inherit it from power and mileage class.

Here, Car class is child class and it is inheritaing properties of Two parent class i.e Power class and Mileage class.
"""


class Power:

    def get_power(self):
        return "Power of car engine"


class Mileage:

    def get_mileage(self):
        return 'this is mileage of car'


class Car(Power, Mileage):
    pass


new_car = Car()
print(new_car.get_mileage())
print(new_car.get_power())
