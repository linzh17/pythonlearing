#if语句
#简单的if语句,缩进的作用与循环中的类似
age = 19
if age >= 18:
	print("right")
	print(age)

#if-else 语句
age = 17
if age >= 18:
	print("old")
	print(age)
else:
	print("young")
	print(age)

#if-elif-else语句
age = 30

if age < 4:
	print("too young")
elif age < 18:
	print("young")
elif age < 45:
	print("adult")	
else:
	print("old")

#if-elif结构可以省略else语句块


#用if语句处理列表
#检查特殊元素
request_toppings = ['mushroom','green peppers','extra cheese']

for request_topping in request_toppings:
	if request_topping == 'green peppers':
		print("sorry,nothing")
	else:
		print("Adding"+request_topping)
print ("making your pizza")

#确定列表不是空的
request_toppings = []

if request_toppings:
	for request_topping in request_toppings:
		print(request_topping)
else:
	print("empty\n")

#使用多个列表
available_toppings = ['mushroom','olives','green peppers','pepperoni',
						'pineapple','extra cheese']
requested_toppings = ['mushroom','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding "+requested_topping)
	else:
		print("Sorry,no " + requested_topping )

print("\nfinished making your pizza")
