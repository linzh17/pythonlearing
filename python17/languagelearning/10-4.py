#存储数据
#使用json.dump()和json.load()
#函数json.dump()接受两个实参，要存储的数据以及可用于存储数据的文件对象
"""使用json.dump()存储数据"""
"""先导入json模块"""
import json

numbers = [2,3,4,7,11,13]

filename = 'numbers.json'
"""以写入的模式打开文件"""
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)

#将json.load()将这个列表读取到内存中
import json

filename = 'numbers.json'
"""文件以读取方式打开"""
with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)

#保存和读取用户的生成的数据
"""import json

username = input("what is your name? ")

filename = 'username.json'
with open(filename,'w') as f_obj:
	json.dump(username,f_obj)
	print("we'll remember you come back, " + username + "!")

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("welcome back, " + username +"!" )"""
		
#重构
#将代码划分为一系列完成具体工作的函数

import json
def greet_users():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
			username = input("what's your name")
			with open(filename,'w') as f_obj:
				json.dump(f_obj)
				print("we'll remberyour name " + username)
	else:
		print("welcome come back " + username)

greet_users()								