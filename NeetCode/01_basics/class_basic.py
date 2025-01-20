"""
Create a Car class with attribute like brand and model. Then create an instance of this class.

"""


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__color = "black"

    def get_car_color(self):
        return self.__color + " car color!"


my_car = Car("Toyota", "Corolla")
print(my_car.model)
print(my_car.brand)

my_car_new = Car('Tata', "Safari")
print(my_car_new.model)
print(my_car_new.brand)

print(my_car.get_car_color())
