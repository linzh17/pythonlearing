#创建数值列表
#range()可以生成一系列数字，从第一个参数数值开始生成，
#直到第二个参数数值停止（不包括第二个参数数值）
for value in range(1,5):
	print(value)

#使用list()将range()的结果直接转化为列表
numbers = list(range(1,6))
print(numbers)

#range() 第三个参数可以指定步长
even_numbers = list(range(2,11,2))
print(even_numbers)

#将十个整数的平方加入到一个列表中
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)

#列表解析,同上面一个结果，语句更加简洁
suqares = [value**2 for value in range(1,11)]
print(squares)

#使用列表的一部分
#切片,始于第一个索引，终于第二个（不包括）
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[1:2])
print(players[:3]) #始于列表头
print(players[2:]) #终于列表尾

#负数索引返回距离列表尾相应距离的的元素
print(players[-3:])
print(players[-4:-2])

#遍历列表切片
for player in players[:3]:
	print(player.title())

#复制列表 创建包含一整个列表的切片
my_food = ['pizza','falafel','carrot cake']
friend_food = my_food[:]
print(friend_food)

#两个列表是独立的，相互不受影响
my_food.append('ice cream')
friend_food.append('hotdog')
print(my_food)
print(friend_food)

#另外一种情况
#直接赋值，类似于将一个列表的引用赋给另外一个，指向同一个列表
my_food = ['pizza','falafel','carrot cake']
friend_food = my_food
my_food.append('ice cream')
print(my_food)
print(friend_food)
friend_food.append('hotdog')
print(my_food)


 









