#一个简单的字典

alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#使用字典，访问字典中的值
alien_0 = {'color':'green'}
print(alien_0['color'])
alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print("击杀外星人你获得了" + str(new_points) + "分。")

#添加键一值对
alien_0 = {'color': 'greeb', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#先创建一个空字典
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#修改字典中的值
alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position:" + str(alien_0['x_position']))

#向右移动外星人
#根据外星人当前速度决定其移动多远
#alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment
print("New x_position: " + str(alien_0['x_position']))


alien_0['x_position'] += x_increment
print("New x_position: " + str(alien_0['x_position']))

#删除键一值对
alien_0 = {'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

#由类似对象组成的字典
favorite_labguages = {'袁鹏':'python',
                      '唐菁':'java',
                      '张凯':'C',
                      '张三':'python'}

print("袁鹏最喜欢的语言是" + favorite_labguages['袁鹏'].title())

#遍历所有的键一值对
user_0 = {
    'username':'袁鹏',
    'first':'yuan',
    'last':'peng'
}
for key,value in user_0.items():
    print("\nKey：" + key)
    print("value：" + value)

favorite_labguages = {'袁鹏':'python',
                      '唐菁':'java',
                      '张凯':'C',
                      '张三':'python'}
for name,language in favorite_labguages.items():
    print(name.title() + "'s favorite language is" + language.title())

for name in favorite_labguages.keys():
    print(name.title())

friends = ['张如辉','张凯']
for name in favorite_labguages.keys():
    print(name.title())
    if name in friends:
        print(name.title() + "我知道你最喜欢的语言" + favorite_labguages[name].title())

if '周子琦' not in favorite_labguages.keys():
    print("周子琦你最喜欢的语言是！")

#按顺序遍历字典中的所有键
favorite_labguages = {'袁鹏':'python',
                      '唐菁':'java',
                      '张凯':'C',
                      '张三':'python'}
for name in sorted(favorite_labguages.keys()):
    print(name.title() + ",我知道你最喜欢的语言是啥了！")

#遍历字典中的所有值
favorite_labguages = {'袁鹏':'python',
                      '唐菁':'java',
                      '张凯':'C',
                      '张三':'python'}

for language in favorite_labguages.values():
    print(language.title())

    #使用set剔除重复值
print("剔除重复值")
for language in set(favorite_labguages.values()):
    print(language)


#嵌套
#字典列表
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
#显示创建了多少个外星人
print("总共创建了" + str(len(aliens)) + "个")

#为前三个外星人升级
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

#再次显示前5个外星人
for alien in aliens[:5]:
    print(alien)

#为黄色外星人再次升级
for alien in aliens[0:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

#再次显示前5个外星人
for alien in aliens[:5]:
    print(alien)

#在字典中存储列表
#存储所点手抓饼的信息
shouzhuabing = {
    'size':'big',
    'kouweis':['jiangxiang','nongxiang'],
}
#讲一下所点的手抓饼
print("你点了一个" + shouzhuabing['size'])

for kouwei in shouzhuabing['kouweis']:
    print(  kouwei)
print("口味的手抓饼")

favorite_labguages = {'袁鹏':['python','C'],
                      '唐菁':['java','c++'],
                      '张凯':['C','java'],
                      '张三':['python','java']}

for name,languages in favorite_labguages.items():
    print("\n" + name.title() +"最喜欢的语言是：")
    for language in languages:
        print("\t" + language.title())

#在字典中存储字典
users = {
    '袁鹏':{
        '姓':'袁',
        '名':'鹏',
        'sex':'man'
    },
    '张凯':{
            '姓':'张',
            '名':'凯',
            'sex':'woman'
    },
    '张如辉':{
            '姓':'张',
            '名':'如辉',
            'sex':'woman'
    }
}

for username,user_info in users.items():
    print("用户名"+ username)
    full_name = user_info['姓'] + " " + user_info['名']
    sex = user_info['sex']
    print(full_name.title())
    print(sex.title())