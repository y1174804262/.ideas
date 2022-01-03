import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("你叫啥")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("这次我将记住你的名字"+ username +"等你回来的时候")
    else:
            print("欢迎回来，" + username)

greet_user()