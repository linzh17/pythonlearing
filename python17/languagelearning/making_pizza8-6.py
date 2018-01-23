#导入模块
import pizza8
pizza8.make_pizza(16,'pepperoni','cheese')

#导入特定的函数
#格式如下 from ** import **
#可以同时导入多个函数

from pizza8 import make_pizza,text

make_pizza(16,'pepperoni','cheese')
text()

#使用as给函数指定别名
from pizza8 import make_pizza as mp
mp(16,'pepperoni','cheese')

#使用as给模块指定别名
import pizza8 as p
p.make_pizza(16,'pepperoni','cheese')

#导入模块中的所有函数
#使用* 号可以让pyhton导入模块中的所有函数
#导入他人的大型模块时，容易出现模块中的函数和项目中的函数名称冲突的问题
from pizza8 import *
make_pizza(16,'pepperoni','cheese')

