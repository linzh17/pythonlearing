#创建和使用类
class Dog():

#类的初始化方法__init__()，左右都各有两个‘_’ 为约定
#形参self 不可缺少，python自动传递
#只需传递另外的形参
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over！")

#根据类创建实例
my_dog = Dog('willie',6)

print("my dog's name is " + my_dog.name.title())
print("my dog's age is " + str(my_dog.age))

