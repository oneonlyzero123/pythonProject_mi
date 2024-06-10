

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



