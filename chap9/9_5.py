# 练习 9.5：尝试登录次数 在为练习 9.3 编写的 User 类中，添加⼀个
# 名为 login_attempts 的属性。编写⼀个名为
# increment_login_attempts() 的⽅法，⽤来将属性
# login_attempts 的值加 1。再编写⼀个名为
# reset_login_attempts() 的⽅法，⽤来将属性
# login_attempts 的值重置为 0。
# 根据 User 类创建⼀个实例，再调⽤
# increment_login_attempts() ⽅法多次。打印属性
# login_attempts 的值，确认它正确地递增了。然后，调⽤⽅法
# reset_login_attempts()，并再次打印属性 login_attempts
# 的值，确认它被重置为 0

class User():
    def __init__(self,first_name,last_name,position,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.position=position
        self.login_attempts=login_attempts

    def describe_user(self):
        message="name: "+self.first_name+" "+ self.last_name
        message+="\nposition: "+self.position
        print(message)

    def greet_user(self):
        print("hi ! "+self.first_name+" "+self.last_name+" ,how are you?")

    def increment_login_attempts(self):
        self.login_attempts+=1


    def reset_login_attempts(self):
        self.login_attempts =0

user_jim=User('jim','willson','newyork',0)
user_jim.increment_login_attempts()
print(user_jim.login_attempts)
user_jim.increment_login_attempts()
print(user_jim.login_attempts)
user_jim.increment_login_attempts()
print(user_jim.login_attempts)
user_jim.increment_login_attempts()
print(user_jim.login_attempts)
user_jim.increment_login_attempts()
print(user_jim.login_attempts)
user_jim.reset_login_attempts()
print(user_jim.login_attempts)

