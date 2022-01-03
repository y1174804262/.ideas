#函数input（）工作原理
# message = input("tell me something, and i will repat it back to you: ")
# print(message)


'''
#编写清晰的程序
message = input("请输入OSI参考模型的七层：")
print("OSI的七层参考模型从上到下为" + message)

prompt = "我想了解TCP/IP参考模型："
prompt += "\n请告诉我答案"

question = input(prompt)
print("TCP\IP的四层参考模型为：" + question)

#使用int（）来获取数值输入
number = input("请告诉我我们学的模型是多少层： ")
number = int(number)
if number == 5:
    print("你的回答是正确的！")
print(number)

#求模运算符
print(4%3)
number = input("请输入OSI参考模型有几层： ")
number = int(number)

if number % 2 == 0:
    print("他有偶数层为：" + str(number))
else:
    print("他有奇数层为：" + str(number))

#while循环简介
#使用while循环

i = 1
print("请输入OSI参考模型（有高层到底层）： ")
while i <= 7:
    input("第" + str(i) + "层为： ")
    i += 1

#让用户选择何时退出

prompt = "\n 请输入OSI参考模型（有高层到底层）： "
prompt += "\n输入网络层退出"
message = ''
while message != '网络层':
    message = input(prompt)
    if message != '网络层':
        print(message)

#使用标志
prompt = "请输入互联网的三级结构："
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False

#使用break退出循环
prompt = "请输入互联网的三级结构："

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)


#在循环中使用continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    else:
        print(i)


#使用while循环来处理列表和字典

#创建一个待验证用户列表
#和一个用于存储已验证用户的空列表

unconfirmed_users = ['张凯','袁鹏','张如辉']
confirmed_users = []

#验证每个用户，直到没有未验证用户为止
#将每个经过验证的列表都移到已验证用户列表中

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("验证用户：" + current_user.title())
    confirmed_users.append(current_user)

#显示所有已验证的用户
print("以下用户通过验证：")
for confirmed_user in confirmed_users:
    print(confirmed_user)

#删除包含所有特定值的所有列表元素
friends = ['张凯','张如辉','周子琦','张凯','张辰','张如辉']
print(friends)
while '张凯' in friends:
    friends.remove('张凯')
print(friends)

#使用用户输入来填充字典
responses = {}

#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    #提示输入者，输入被调查者的名字和回答
    name = input("\n你叫啥？")
    response = input("你喜欢大海大？")

    #将答卷存储在字典中
    responses[name] = response

    #看看是否还有人要参与调查
    repeat = input("你还想让别的人回答这个问题？（yes/no）")
    if repeat == 'no':
        polling_active = False

#调查结束，显示结果
print("显示调查结果\n")
for name,response in responses.items():
    print(name + response + "大海大")
'''
