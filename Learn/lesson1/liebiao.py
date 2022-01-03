#列表其实对应的就是数组吧
bicycles = ['trek','cannodale','redline','specialized']
print(bicycles)
print(bicycles[0].title())
#索引从0开始
print(bicycles[1])
print(bicycles[3])
#索引-1可以返回列表中的倒数第一个元素，-2为第二个，这很好用
print(bicycles[-1])
message = "My first bicycle was a" + bicycles[0].title() + "."
print(message)
#修改、添加、删除元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#插入元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#删除元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
del motorcycles[1]
print(motorcycles)
    #pop方法删除元素,类似于栈中的弹出
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop();
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("我的最后一辆摩托车是" +last_owned)

#pop方法后边可以跟参数，可以弹出任何一个元素，需要注意弹出的元素弹出后原列表就没了
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print("我的第一辆摩托车是" +first_owned)

#根据值删除元素用remove（）方法
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)

#sort()方法对列表进行永久排序
cars = ['bmw','auti','toyota','subaru']
cars.sort()
print(cars)
#使用sort方法加入传递参数 reverse = True就可降序排序
cars.sort(reverse = True)
print(cars)

#sorted()方法可进行临时排序
cars = ['bmw','auti','toyota','subaru']
print("这是排序前的顺序" )
print(cars)
print("这是排序后的顺序" )
print(sorted(cars))
print(cars)

#倒叙输出reverse()方法,反转是永久的，如果想要返回只需再次反转就行了
cars = ['bmw','auti','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#确定列表的长度
cars = ['bmw','auti','toyota','subaru']
print(len(cars))

#避免索引错误，索引是从0开始的，令索引为-1则可定位到最后一个元素

#操作列表（列表进阶）
#遍历列表
magicians = ["alic","david","corolina"]
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + "的演出太精彩了！")
    print("我期待" + magician.title() + "的下次表演.\n")
#for循环结束后执行操作
print("这个for循环用着很精彩")
#对于for循环不要忘记缩进！和“：”

#创建数值列表

#使用函数range（）,该函数是从某个数开始数，并在达到终值后停止，因此在到了结束时自动跳出
#类似于别的语言中的终止，当达到某个条件后直接终止不再运行，反正能想通的
for value in range(1,5):
    print(value)

#使用range（）创建数字列表
numbers = list(range(1,6))
print(numbers)
#range（）指定步长
even_numbers = list(range(2,11,2))
print(even_numbers)
#两个*表示乘方
squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)

print(squares)
#简化
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#对数字列表执行简单的统计计算
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析
squares = [value ** 2 for value in range(1,11)]
print(squares)

#使用列表的一部分
#切片
players = ['langping','liuxiang','yaoming','malong','liuguoliang']
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

#遍历切片
for player in players[:3]:
    print(player.title())

#复制列表[:]这个很重要！！！
my_food = ['mantou','huimian','yangtang','shaobing','kaochuan']
friend_foods = my_food[:]

my_food.append('cake')
friend_foods.append('ice cream')

print(my_food)
print(friend_foods)

#元组
#定义元组,元组中的数据不能修改！
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250

#遍历元组中的所有值
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)








