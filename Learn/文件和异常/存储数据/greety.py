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
def get_new_username():
    username = input("你叫啥")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("欢迎回来" + username)
    else:
        username = get_new_username()
        print(username + "我们还记得你")

greet_user()