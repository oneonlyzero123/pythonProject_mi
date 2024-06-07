#
# 练习 9.6：冰激凌⼩店 冰激凌⼩店是⼀种特殊的餐馆。编写⼀个名为
# IceCreamStand 的类，让它继承你为练习 9.1 或练习 9.4 编写的
# Restaurant 类。这两个版本的 Restaurant 类都可以，挑选你更喜
# 欢的那个即可。添加⼀个名为 flavors 的属性，⽤于存储⼀个由各种
# ⼝味的冰激凌组成的列表。编写⼀个显⽰这些冰激凌⼝味的⽅法。创
# 建⼀个 IceCreamStand 实例，并调⽤这个⽅法。

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):

        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def decribe_restaurant(self):
        print("name:"+self.restaurant_name)
        print("cuisine_type:"+self.cuisine_type)
    def open_restaurant(self):
        print("the restaurant is open")
class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=["甘草","草莓","抹茶"]

    def describe_flavors(self):
        print(self.flavors)

IceCreamStand= IceCreamStand('domind','pizza')
IceCreamStand.describe_flavors()





