#导入含有多个类的模块
from MoreCar9 import ElectricCar

my_tesla = ElectricCar('tesla','model s',2017)
my_tesla.get_car_name()
my_tesla.get_car_battery()

#从一个模块中导入多个类
from MoreCar9 import Car,ElectricCar

my_car = Car('bmw','x5',2017)
my_car.get_car_name()
my_tesla = ElectricCar('tesla','model s',2018)
my_tesla.get_car_name()
my_tesla.get_car_battery()

#导入一整个模块
import MoreCar9
my_car = MoreCar9.Car('bmw','x5',2015)
my_car.get_car_name()
my_tesla =  MoreCar9.ElectricCar('tesla','model s',2018)
my_tesla.get_car_name()

#导入模块中的所有类
from MoreCar9 import *
my_car = Car('bmw','x5',2018)
my_car.get_car_name()
my_tesla = ElectricCar('tesla','model s',2018)
my_tesla.get_car_name()

#还可以在另外一个模块中导入另一个模块