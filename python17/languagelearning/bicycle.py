#创建列表
bicycle = ['trek','cannodale']
print(bicycle)
print(bicycle[0])
print(bicycle[0].title())

message = "My first bicycle was a " + bicycle[0].title() + "."
print(message)

#修改列表元素
bicycle[0] = 'treknew'
print(bicycle)

#在列表末尾添加元素
bicycle.append('addone')
print(bicycle)

#在列表插入元素
bicycle.insert(1,'insertone')
print(bicycle)

#在列表删除元素
del bicycle[0]
print(bicycle)

#用pop函数删除列表末尾元素
popped_one = bicycle.pop()
print(popped_one)
print(bicycle)

#用pop()加下标可以删除列表中的任意一个元素
popped_two = bicycle.pop(0)
print(popped_two)
print(bicycle)

#用remove函数根据值删除列表中的值 且删除列表中的第一个出现的指定的元素，其他的相同的元素需要重新删除
bicycle = ['trek','cannodale']
bicycle.remove('trek')
print(bicycle)

#用sort函数对列表进行排序,永久性修改
bicycle = ['trek','cannodale']
bicycle.sort()
print(bicycle)

#用sorted函数对列表进行临时性排序,非永久性修改
bicycle = ['trek','cannodale']
print(sorted(bicycle))
print(bicycle)

#用reverse函数倒置打印列表的元素,永久性修改
bicycle.reverse()
print(bicycle)

#用len函数获取列表长度
print(len(bicycle))

#用索引-1返回最后一个列表元素,列表元素为空的时候则返回错误
print(bicycle[-1])

#用for循环循环打印名单
magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician)

#用for循环 缩进很重要,循环中的缩进循环执行 没有缩进的语句执行一次
magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician)
	print("good")
print("the end")

 







