#继承
#子类的__init__()
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def get_car_name(self):
		print(str(self.year) + self.model + self.make)

#子类继承
class ElectricCar(Car):
	def __init__(self,make,model,year):
		""" super()调用父类的__init__()方法"""
		super().__init__(make,model,year)

my_tesla = ElectricCar('tesla','model s',2018)
my_tesla.get_car_name()

#给子类定义 属性和方法

class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def get_car_name(self):
		print(str(self.year) + self.model + self.make)

class ElectricCar(Car):
	def __init__(self,make,model,year):
		""" super()调用父类的__init__()方法"""
		super().__init__(make,model,year)
		self.battery_size = 70

	def get_car_battery(self):
		print(self.battery_size)

my_tesla = ElectricCar('tesla','model s',2017)
my_tesla.get_car_name()
my_tesla.get_car_battery()

#重写父类的方法
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def get_car_name(self):
		print(str(self.year) + self.model + self.make)

class ElectricCar(Car):
	def __init__(self,make,model,year):
		""" super()调用父类的__init__()方法"""
		super().__init__(make,model,year)
		self.battery_size = 70
		"""对父类方法重写"""
	def get_car_name(self):
		print(str(self.year) + self.model + self.make + str(self.battery_size))

my_tesla = ElectricCar('tesla','model s',2017)
my_tesla.get_car_name()


#将实例用作属性
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def get_car_name(self):
		print(str(self.year) + self.model + self.make)

class Battery():
	def __init__(self,battery_size = 70):
		self.battery_size = battery_size
	def get_battery_size(self):
		return self.battery_size

class ElectricCar(Car):
	def __init__(self,make,model,year):
		""" super()调用父类的__init__()方法"""
		super().__init__(make,model,year)
		""""Battery实例用作属性"""
		self.battery = Battery()

	def get_car_battery(self):
		print(self.battery.get_battery_size())

my_tesla = ElectricCar('tesla','model s',2017)
my_tesla.get_car_name()
my_tesla.get_car_battery()
