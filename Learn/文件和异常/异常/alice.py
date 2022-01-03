#处理FileNotFoundError
file_name = 'alice.txt'

try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(file_name + "文件不存在")
else:
    words = contents.split()
    num_words = len(words)
    print(file_name + "里有" + str(num_words) + "个单词")