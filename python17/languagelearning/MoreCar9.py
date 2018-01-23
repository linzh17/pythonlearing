#在一个模块中存储多个类

class Car():

	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.miles = 0

	def get_car_name(self):
		print(str(self.year) + self.make + self.model + str(self.miles))

	def update_car_miles(self,new_miles):
		self.miles = new_miles

		
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
