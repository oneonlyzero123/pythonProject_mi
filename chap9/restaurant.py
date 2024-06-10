class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):

        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def decribe_restaurant(self):
        print("name:"+self.restaurant_name)
        print("cuisine_type:"+self.cuisine_type)


    def open_restaurant(self):
        print("the restaurant is open")
