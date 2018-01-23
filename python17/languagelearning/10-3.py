#异常
#处理ZeroDivisionError 异常
#使用try_except 代码块
try:
	print(5/0)
except ZeroDivisionError:
	print("you can't do this")

#使用异常可以使程序避免奔溃
#else代码块
f_num = 5
s_num = 0 
try:
	answer = f_num/s_num
except ZeroDivisionError:
	print("you can't do that")	
else:
	print(answer)

#FileNotFoundError异常
#文件不存在产生的异常
filename = 'alioe.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except:
	message = ("sorry ,i can't find that")
	print(message)	

#出现异常时使用pass语句
#程序会执行except的语句 但程序不会出现trackback
filename = 'alioe.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except:
	pass
