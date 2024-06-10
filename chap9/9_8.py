# 练习 9.8：权限 编写⼀个名为 Privileges 的类，它只有⼀个属性
# privileges，其中存储了练习 9.7 所述的字符串列表。将⽅法
# show_privileges() 移到这个类中。在 Admin 类中，将⼀个
# Privileges 实例⽤作其属性。创建⼀个 Admin 实例，并使⽤⽅法
# show_privileges() 来显⽰权限。

class Privileges():

    def __init__(self,privileges=
    ["can add post", "can delete post", "can ban user","can write","can read"]):

        self.privileges =privileges
    def show_privileges(self):
        print(self.privileges)

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
        self.privileges_0 = ["can add post","can delete post","can ban user"]
        self.privileges=Privileges()

    def show_privileges(self):
        print(self.privileges_0)



Admin= Admin('jim','tom','beijing')
Admin.privileges.show_privileges()
