# from Car import Car,ElectricCar
#
# my_beetle = Car('Volkswagen','beetle',2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla','roadster',2016)
# print(my_tesla.get_descriptive_name())

#导入整个模块
# import Car
#
# my_beetle = Car.Car('Volkswagen','beetle',2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = Car.ElectricCar('tesla','roadster',2016)
# print(my_tesla.get_descriptive_name())
#在一个模块中导入另一个模块

from Car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswage','beetle','2016')
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())