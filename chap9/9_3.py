# 练习 9.3：⽤户 创建⼀个名为 User 的类，其中包含属性
# first_name 和 last_name，还有⽤户简介中通常会有的其他⼏个
# 属性。在类 User 中定义⼀个名为 describe_user() 的⽅法，⽤于
# 打印⽤户信息摘要。再定义⼀个名为 greet_user() 的⽅法，⽤于向
# ⽤户发出个性化的问候。
# 创建多个表⽰不同⽤户的实例，并对每个实例调⽤上述两个⽅法

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

user_jim=User('jim','willson','newyork')
user_jim.describe_user()
user_jim.greet_user()
user_tom=User('tom','shell','london')
user_tom.describe_user()
user_tom.greet_user()