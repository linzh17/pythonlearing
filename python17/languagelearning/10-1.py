#打开并读取整个文件
#关键字with 在不需要访问文件时 自动关闭文件
with open('pi_digits.txt') as file_object:
	"""read()在读取到文件尾时会返回一个空字符串"""
	contents = file_object.read()
	print(contents)
	"""使用rstrip()删除多出来的空行"""
	print(contents.rstrip())

#逐行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		"""文件末尾默认有一个换行符"""
		"""print语句也会默认加一个换行符"""
		#print(line)
		"""使用rstrip()消除空字符串"""
		print(line.rstrip())

#创建一个包含文件各行内容的列表

filename = 'pi_digits.txt'

with open(filename) as file_object:
	"""使用readlines()从文件中读取每一行，并将其存储在一个列表中"""
	lines = file_object.readlines()

for line in lines:
	print(line)
for line in lines:
	print(line.rstrip())

#使用文件内容

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(pi_string)	

#圆周率是否包含生日例子
birthday = "141592"
if birthday in pi_string:
	print("right")
else:
	print("wrong")





