#使用while循环来处理列表和字典
#在列表之间移动元素
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nthe confirmed users")
for confirmed_user in confirmed_users:
	print(confirmed_user)

#删除包含特定值的所有列表元素，重复出现的元素，remove()只能删除一次，重复的元素需要继续删除
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)

#使用用户输入来填充字典
reponses = {}

#设置一个标志
polling_active = True

while polling_active:
	
	name = input("\nwhat is your name ")
	reponse = input("\nwhich moutain would you like to climb someday ")

	reponses[name] = reponse

	repeat = input("\nwould you like to continue yes or no ")
	if repeat == 'no':
		polling_active = False
print("end")
					