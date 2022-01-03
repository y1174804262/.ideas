print("hello Python world!");

message = "Hello Python world!"
print(message)

message = "Hello Python is the best language"
print(message)
mesage = "Hello Python is the best language"
print(mesage)

name = "ada lovelace"
print(name.title())  #title方法将字符串上的首字母大写
print(name.upper())  #Upper方法将字符串上所有的字母都大写
print(name.lower())  #lower方法将字符串上所有的字母都小写

#字符串拼接
first_name = "yuan"
last_name = "peng"
full_name = first_name + " " + last_name
print(full_name)
message = "Hello," + full_name.title() + "!"
print(message)

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#删除空白
favorite_language = 'Python '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = ' Python '
print(favorite_language.rstrip()) #前空格
print(favorite_language.lstrip()) #后空格
print(favorite_language.strip())  #前后空格都删

#字符串输出错误
message = "I come's from Dlou"
print(message)
#message = 'I come's from Dlou引号必须对应！

#所有小数都叫浮点数
print(0.2 + 0.1)
print(3 * 0.1)

#引入str（）
# age = 20
# message = "Hello" + age + "th;"
# print(message) 这不是错了么
age = 20
message = "hello" + str(age) + "th"
print(message)

print(3/2)
print(3.0/2)
print(3.0/2.0)
print(3/2.0)



