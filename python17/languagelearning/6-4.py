#嵌套
#字典列表，将字典嵌套在列表中
alien_0 = {'color': 'green','point': 5}
alien_1 = {'color': 'yellow','point': 10}
alien_2 = {'color': 'red','point': 15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)
	for key,value in alien.items():
		print(key)
		print(value)


#列表字典，将列表嵌套在字典中
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms','extra cheese'],
	}

print(pizza)
print(pizza['toppings'])
print(pizza['toppings'][0])

for topping in pizza['toppings']:
	print(topping)

#在字典中存储字典
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},	
	}
for username,user_info in users.items():
	print("\nUsername: "+username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\nFullname: "+full_name)
	print("\nLocation: "+location)
