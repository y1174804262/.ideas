file_name = 'programming.txt'

with open(file_name,'w') as file_object:

    file_object.write("I love programming\n")
    file_object.write("I love programming by Python\n")

#附加到文件
with open(file_name,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love make webs\n")