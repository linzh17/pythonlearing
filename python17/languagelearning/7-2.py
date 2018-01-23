#while循环
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

#让用户选择何时退出
prompt  = "\ntell me something, and i will repeat it back to you :"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)

	if message !='quit':
		print(message)

#使用标志来解决运行条件较多的循环

#使用break退出 循环
prompt = "\nplease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' when you are finished. "

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(city.title())

#使用continue
current_number = 0
while current_number <10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)
		

