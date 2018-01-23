#导入类
#导入单个类
"""一个用于表示汽车的类"""
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
			
