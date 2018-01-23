#传递任意数量的实参，不定位置实参
#* 星号创建 一个空的元组，将收到的值封装在元组中
def make_pizza(*toppings):
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')

#结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
	print("making a " + str(size) + " inch pizza with following toppings")
	for topping in toppings:
		print(topping)

make_pizza(12,'peppeoni','cheese','green')

#使用任意数量的关键字实参
# ** 两个星号创建一个空的字典 ，将收到的键-值对封装到字典中 不定关键字实参
def build_profile(first,last,**user_info):
	profile = {}
	profile['first_name'] = first 
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
user_profield = build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profield)		


