#函数传递列表
def greet_users(names):
	for name in names:
		msg = "hello " + name.title() + "!"
		print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

#在函数修改列表
unprinted_designs = ['iphone case','robot pendant','dodecahedron']	
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()

	print("printing model: " + current_design)
	completed_models.append(current_design)
print("\nthe following models have been printed: ")
for completed_model in completed_models:
	print(completed_model)

#禁止函数修改列表
#可以使用[:]创建列表的副本，上面例子的用法则会使原来的列表为空

