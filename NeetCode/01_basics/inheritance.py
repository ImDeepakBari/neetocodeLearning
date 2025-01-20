"""
Create an electric car class that inherites form car class and has an additional attribute battery_size.
"""
from class_basic import Car


class ElectricCar(Car):

    def __init__(self, model, brand, battery_size):
        super().__init__(model, brand)
        self.battery = battery_size


my_tesla = ElectricCar("Tesla", "Model Z", "87kWH")
print(my_tesla.model)
