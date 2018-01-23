#写入文件
#写入空文件
filename = 'programing.txt'

"""调用open()需要另一个参数 'w' 告诉python要写入打开的文件"""
"""'w'以写入模式打开文件 如果文件存在，则清空文件"""
"""'r'读取模式"""
"""'a'附加模式"""
"""'r+'模式 可以读取和写入"""
"""没有模式实参的情况 默认为只读模式"""
with open (filename,'w') as file_object:
	file_object.write("i love python. ")

#写入多行
filename = 'programing.txt'

with open(filename,'w') as file_object:
	file_object.write("i love python")
	file_object.write("i love creating python")
	file_object.write("\ni love python")
	file_object.write("\ni love python work ")

#附加到文件
#要给文件添加内容
#可以使用'a'附加模式 添加内容
#从而不会清空文件
filename = 'programing.txt'

with open(filename,'a') as file_object:
	file_object.write("\ni also love c++")
	file_object.write("\ni don't like like java")
