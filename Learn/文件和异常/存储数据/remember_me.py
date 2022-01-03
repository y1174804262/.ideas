import json

username = input("请输入你的名字")

filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("我将记住你当你返回的时候， " + username)