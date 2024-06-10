# 练习 10.14：验证⽤户 最后⼀个 remember_me.py 版本假设⽤户要么
# 已输⼊其⽤户名，要么是⾸次运⾏该程序。我们应修改这个程序，以
# 防当前⽤户并⾮上次运⾏该程序的⽤户。
# 为此，在 greet_user() 中打印欢迎⽤户回来的消息之前，询问他⽤
# 户名是否是对的。如果不对，就调⽤ get_new_username() 让⽤户
# 输⼊正确的⽤户名
import json
def get_stored_username():
    filename='username.json'
    try:
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return  username


def get_new_username():
    username=input("name")
    filename='username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    username=get_stored_username()
    if username:
        answer=input(username+" 这个名字是对的吗？Y/N")
        if answer=='Y':
            print("welcome back, " + username + " !")
        elif answer=='N':
            username = get_new_username()
            print("we will remember you when you come back, " + username + " !")
    else:
        username=get_new_username()
        print("we will remember you when you come back, "+username+" !")

greet_user()