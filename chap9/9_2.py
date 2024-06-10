# 练习 9.2：三家餐馆 根据为练习 9.1 编写的类创建三个实例，并对每
# 个实例调⽤ describe_restaurant() ⽅法。
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):

        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def decribe_restaurant(self):
        print("name:"+self.restaurant_name)
        print("cuisine_type:"+self.cuisine_type)


    def open_restaurant(self):
        print("the restaurant is open")

restaurant_1=Restaurant("domind","pizza")
restaurant_1.decribe_restaurant()
restaurant_2=Restaurant("maidanglao","fried chicken")
restaurant_2.decribe_restaurant()
restaurant_3=Restaurant("kendeji","potato")
restaurant_3.decribe_restaurant()