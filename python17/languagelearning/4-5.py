#元组
#定义元组
#类似列表，但使用圆括号而不是方括号
dimesions = (200,50)
print(dimesions[0])
print(dimesions[1])

#修改元组元素的值,不允许,可用于一组值在程序周期都不发生变化
#dimesions[0] = 250 TypeError: 'tuple' object does not support item assignment

#循环遍历元组的值
for dimesion in dimesions:
	print(dimesion)

#修改元素变量
#不可以修改元素的值，可以修改存储元组变量
print(dimesions)
dimesions = (400,100)
print(dimesions)



