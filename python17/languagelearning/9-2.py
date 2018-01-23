class Car():

	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year

	def get_car_name(self):
		print(str(self.year) + self.make + self.model)

my_car = Car('audi','a4',2017)
my_car.get_car_name()

#给属性指定默认值
class Car():
	def __init__(self,make,model,year):
		self.make =make
		self.model =model
		self.year = year
		"""属性指定默认值，初始化方法可以不提供该属性的形参"""
		self.mile = 0

	def get_car_name(self):
		print(str(self.year) + self.make +self.model + str(self.mile) )
	"""通过方法修改属性的默认值"""
	def update_mile(self,new_mile):
		self.mile = new_mile	


my_car = Car('audi','a4',2017)
my_car.get_car_name()

#修改属性的值
#直接修改属性的值
my_new_car = Car('audi','a4',2017)
my_new_car.get_car_name()
my_new_car.mile = 32
my_new_car.get_car_name()

#通过方法修改属性的值
my_new_car = Car('bmw','x5',2018)
my_new_car.get_car_name()
"""修改属性的值"""
my_new_car.update_mile(55)
my_new_car.get_car_name()

#通过方法对属性的值进行递增




