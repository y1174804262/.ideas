# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)
#     print(contents.rstrip())

# file_name = 'pi_digits.txt'
#
# with open(file_name) as file_object:
#     lines = file_object.readlines()
#
# for line in lines:
#         print(line.rstrip())

file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

bithday = input("请输入你的生日，yymmdd：")

if bithday in pi_string:
    print("小数点的前100W位含你的生日")
else:
    print("小数点的前100W位不含你的生日")