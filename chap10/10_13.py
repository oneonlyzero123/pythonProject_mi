# 练习 10.13：⽤户字典 ⽰例 remember_me.py 只存储了⼀项信息——
# ⽤户名。请扩展该⽰例，让⽤户同时提供另外两项信息，再将收集到
# 的所有信息存储到⼀个字典中。使⽤ json.dumps() 将这个字典写⼊
# ⽂件，并使⽤ json.loads() 从⽂件中读取它。打印⼀条摘要消息，
# 指出程序记住了有关⽤户的哪些信息。
import json
filename='imformation.json'
username=input("what is your name")
userage=input("how old are you")
userposition=input("where are you")
user_infor={"username":username,
               "userage":userage,
               "userposition":userposition,
               }
with open(filename, 'w') as f_obj:
    user_info=json.dumps(user_infor)
    print(user_info)

print("loads::")
with open(filename) as f_obj:
    userinfo=json.loads(user_info)

    print(userinfo)

