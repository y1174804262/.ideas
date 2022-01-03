from pizza import make_pizza

make_pizza(16,'pepperoni')
make_pizza(18,'mushrooms','green peppers','extra cheese')

#使用as给函数指定别名
from pizza import make_pizza as mp

mp(16,'a')
mp(18,'b','c')

#使用as给模块指定别名
import pizza as p

p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers')

#导入模块中的所有函数
from pizza import *

make_pizza(14,'q')
make_pizza(13,'e','r')