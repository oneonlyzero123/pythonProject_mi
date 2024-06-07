# 练习 9.7：管理员 管理员是⼀种特殊的⽤户。编写⼀个名为 Admin
# 的类，让它继承你为练习 9.3 或练习 9.5 完成编写的 User 类。添加⼀
# 个名为 privileges 的属性，⽤来存储⼀个由字符串（如 "can add
# post"、"can delete post"、"can ban user" 等）组成的列
# 表。编写⼀个名为 show_privileges() 的⽅法，显⽰管理员的权
# 限。创建⼀个 Admin 实例，并调⽤这个⽅法。
class User():
    def __init__(self,first_name,last_name,position):
        self.first_name=first_name
        self.last_name=last_name
        self.position=position

    def describe_user(self):
        message="name: "+self.first_name+" "+ self.last_name
        message+="\nposition: "+self.position
        print(message)

    def greet_user(self):
        print("hi ! "+self.first_name+" "+self.last_name+" ,how are you?")

class Admin(User):
    def __init__(self, first_name, last_name, position):
        super().__init__(first_name, last_name, position)
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self):
        print(self.privileges)

Admin= Admin('jim','tom','beijing')

Admin.show_privileges()