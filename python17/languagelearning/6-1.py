#简单的字典
alien_0 = {'colors': 'green','points': 5}

print(alien_0['colors'])
print(alien_0['points'])

#添加字典的键-值对
alien_0 = {'colors': 'green','points': 5}
alien_0['x_points'] = 0
alien_0['y_points'] = 25

print(alien_0)

#修改字典中的值
alien_0['colors'] = 'yellow'
print(alien_0)

#删除键-值对,用del 删除元素
alien_0 = {'colors': 'green','points': 5}

del alien_0['points']
print(alien_0)

#遍历字典
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

#itmes()返回一个键-值对列表	
for key ,value in user_0.items():
	print("\nKey " + key)
	print("Value " + value)

#遍历字典中的所有键,keys()返回字典的键——值对的键列表
favorite_lauguage = {
	'jen': 'python',
	'sarah': 'c',
	'echward': 'ruby',
	'phil': 'python'
	}
friends = ['jen','sarah']
for name in favorite_lauguage.keys():
	if name in friends:
		print(name.title()+" is my friend")
	else:
		print(name.title())	
#省略keys()方法，得到相同结果
for name in favorite_lauguage:
	print(name.title())

#按顺序遍历字典中的键
favorite_lauguage = {
	'jen': 'python',
	'sarah': 'c',
	'echward': 'ruby',
	'phil': 'python'
	}

for name in sorted(favorite_lauguage.keys()):
	print(name)

#遍历字典中的值,用values()返回字典中值列表
favorite_lauguage = {
	'jen': 'python',
	'sarah': 'c',
	'echward': 'ruby',
	'phil': 'python'
	}

for lauguage in favorite_lauguage.values():
	print(lauguage.title())

#用set()提取字典中的值，并且不重复取值
for lauguage in set(favorite_lauguage.values()):
	print(lauguage)
		
