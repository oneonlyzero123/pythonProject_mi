
from user import  User
class Privileges():

    def __init__(self,privileges=
    ["can add post", "can delete post", "can ban user","can write","can read"]):

        self.privileges =privileges
    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, position):
        super().__init__(first_name, last_name, position)
        self.privileges_0 = ["can add post","can delete post","can ban user"]
        self.privileges=Privileges()

    def show_privileges(self):
        print(self.privileges_0)