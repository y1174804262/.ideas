#示例1
cars = ['biyadi','dazhong','hongqi','wuling']

for car in cars:
    if car == 'wuling':
        print(car.upper())
    else:
        print(car.title())

#检验python
car = 'auto'
if car == 'AUTO':
    print("python不区分大小写")
else:
    print("python区分大小写")

#检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("hello the anchovies")
    #检查两个数字是否相等
age = 20;
if age != 40:
    print("你不是40岁")
#检查多个条件，用and，&&
age = 20
if age != 30 and age != 10:
    print("你不是10岁也不是30岁")

#检查多个条件，使用or，||
age = 15
if age == 18 or age == 12:
    print("并是处在12岁或者18岁")

#检查特定值是否包含在列表中
requested_toppings = ['mushrooms','onions','pineapple']
if 'mushrooms' in requested_toppings:
    print("mushrooms在列表里面")

#布尔表达式
game_active = True
can_edit = False

#简单的if语句
age = 18
if age <= 20:
    print("你还年轻")
    print("你一定要努力")

#if-else 语句
age = 20
if age <= 18:
    print("你还小")
    print("你要好好学习")
else:
    print("你不小了")
    print("你更要努力")

#if-elif-else 结构

age = 12

if age <= 4:
    print("四岁以下都免费")
elif age < 18:
    print("4-18岁5美元")
else:
    print("18岁以上10美元")

#使用多个elif代码块
age  = 12
if age < 4 :
    price = 0
elif age < 12:
    price = 5
elif age < 18:
    price = 10
else:
    price = 70
print(price)

#else 可以省略
age  = 12
if age < 4 :
    price = 0
elif age < 12:
    price = 5
elif age < 18:
    price = 10

print(price)

#测试多个条件，在多种条件都为真的话只返回第一个
ages = [11,12,15]
if 11 in ages:
    print("11在")
elif 12 in ages:
    print("12也在")
elif 15 in ages:
    print("15也在")

#使用if语句处理列表
#检查特殊元素
requested_toppings = ['mushrooms','green papers','extra cheese']
for requested_topping in requested_toppings:
    print("Adding" + requested_topping)

for requested_topping in requested_toppings:
    if requested_topping == 'green papers':
        print("green papers,没了")
    else:
        print("add\t"+requested_topping)
print("haole!")

#确定列表不是空的
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("add" + requested_topping)
    print("做好了")
else:
    print("你想吃啥！")

#使用多个列表
available_toppings = ['mushrooms','olives','green papers','paperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("添加" + requested_topping)
    else:
        print(requested_topping+"这里没有这个")