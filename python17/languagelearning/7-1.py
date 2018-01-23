#函数input()的工作原理,参数为用于输入的提示信息，不能在sublime text中实现输入，只能终端运行
message = input("Tell me something,and i will repeat it back to you: ")
print (message)

name = input("please enter your name: ")
print("hello," + name + "!")

#提示超过一行的情况
prompt = "if you tell us who you are, we can personalize the message you see. "
prompt += "\nwhat is your first name"

name = input(prompt)
print("\nhello," + name + "!")

#使用函数input(),python会将用户输入解读为字符串
#使用int()可以将输入的数字的字符串转化数值
age = input("how old are you ")
age = int(age)
if age >= 18:
	print("adult")
	

