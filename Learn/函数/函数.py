#函数
#定义函数

def greet_uesr():
    #显示简单的问候语
    print("你好！")

greet_uesr()

#向函数传递信息
def greet_user(username):
    print(username + "你好")
greet_user('袁鹏')

#传递实参
#位置实参
def describe_friend(friend_sex,friend_name):
    """显示朋友信息"""
    print(friend_name + "是我的朋友，他是" + friend_sex )

describe_friend('男','张凯')
#多次调用函数
describe_friend('女','张如辉')

#位置实参的顺序很重要，区分函数！跟C想，你能相通，懒得举例

#关键字实参
def describe_friend(friend_sex,friend_name):
    """显示朋友信息"""
    print(friend_name + "是我的朋友，他是" + friend_sex )

describe_friend(friend_name='周子琦',friend_sex='男')

#默认值，默认值也是可以改的！
def describe_friend(friend_name,friend_sex = '男'):
    print(friend_name + "是我的好朋友，他是" + friend_sex)

describe_friend(friend_name='张凯')

#等效的函数调用
describe_friend(friend_name='张凯',friend_sex='女')

#返回值
#返回简单值
def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name

computer = get_formatted_name('袁','鹏')
print(computer)

#让实参变成可选的
def get_formatted_name(first_name,middle_name,last_name):
    full_name = first_name + middle_name + last_name
    return full_name

print(get_formatted_name('袁','','鹏'))
print(get_formatted_name('张','如','辉'))

#返回字典
def build_person(first_name,last_name):
    #返回一个字典，其中包含有关一个人的信息
    person = {'first':first_name,'last':last_name}
    return person
computer = build_person('张','凯')
print(computer)

#结合使用函数和while循环
'''
def get_formatted_name(first_name,last_name):
    #返回整洁姓名
    full_name = first_name + last_name
    return full_name

while True:
    print("请输入你的名字,如果想退出请输入‘q’")
    f_name = input("请输入您的姓")
    if f_name == 'q':
        break
    l_name = input("请输入您的名")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)

    print(formatted_name + "您好！")
'''
#传递列表
def greet_users(names):
    '''向每位同学问好'''
    for name in names:
        print(name + "您好！好好学习！")

usernames = ['张凯','袁鹏','崔满亮']
greet_users(usernames)

#在函数中修改列表

unprinted_designs = ['张凯','袁鹏','崔满亮','张悦']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()

    print("打印" + current_design)
    completed_models.append(current_design)

print("下面的名字打印完了：")
for completed_model in completed_models:
    print(completed_model)



def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("打印" + current_design)
        completed_models.append(current_design)

def show_completed_modles(compled_models):
    print("下面的名字打印完了：!!!")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['张凯','袁鹏','崔满亮','张悦']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_completed_modles(completed_models)
show_completed_modles(unprinted_designs)
#禁止函数修改列表,只需要在传递参数的时候在参数后边加上[:]如上面

#传递任意数量的参数
def make_shouzhuabing(*peiliaos):
    print("下面说要加什么\n加",end="")
    for peiliao in peiliaos:
        print("-" + peiliao,end="")

make_shouzhuabing("烤肠")
make_shouzhuabing("烤肠",'生菜','鸡柳')

#结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    '''概述要制作的pizza'''
    print("\n Making a " + str(size) +"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza(16,"pepperoni")
make_pizza(12,'mushrooms','green peppers','extra cheese')

#使用任意数量的关键实参
def build_profile(first,last,**user_info):
    '''创建一个字典，其中包含我们知道的有关用户的一切'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('袁','鹏',locationg ='河南',school = 'DLOU' )
print(user_profile)

