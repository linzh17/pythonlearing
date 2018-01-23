#将函数存储在模块中
#模块是扩展名为.py的文件

#模块名不可以含有 ‘-’
def make_pizza(size,*toppings):
	print("making a " + str(size) + " inch pizza with fllowing toppings")
	for topping in toppings:
		print(topping)

def text():
	print("hello")
	
