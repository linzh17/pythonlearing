#if语句
#实例
cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

requested_topping = 'mushroom'

if requested_topping != 'anchovies':
	print("Hold the anchovies")

answer = 17	
if answer != 8:
	print("flase")

#检查多个条件
#使用and,等同于C++的 &&
answer_1 = 1
answer_2 = 2
if(answer_1 == 1 and answer_2 ==2):
	print("right")

#使用or 等同于C++的 ||
answer_1 = 1
answer_2 = 3
if(answer_1 == 1 or answer_2 == 2):
	print("right")

#检查特定值是否在列表中
cars = ['audi','bmw','subaru','toyota']
if 'bmw' in cars:
	print("right")

if 'xiandai' not in cars:
	print("false")

#条件测试
car = 'subaru'
print(car == 'audi')	
print(car == 'subaru')
