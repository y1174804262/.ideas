def count_words(filename):

    try:
        with open(filename) as file_object:
            contens = file_object.read()
    except FileNotFoundError:
       pass
    else:
        words = contens.split()
        num_words = len(words)
        print(filename + "文件有" + str(num_words) + "个词")

filenames = ['alice.txt','little_women.txt','moby_dick.txt','siddhartha.txt']
for filename in filenames:
    count_words(filename)