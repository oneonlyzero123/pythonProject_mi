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