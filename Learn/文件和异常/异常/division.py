#使用try-except代码块
try:
    print(4/0)
except ZeroDivisionError:
    print("除数不能为0")

print("给两个数就能做除法")
print("输入q退出程序")

while True:
    first_number = input("第一个数")
    if first_number == 'q':
        break;
    second_number = input("第二个数")
    if second_number == 'q':
        break;
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("除数不能为0")
    else:
        print(answer)