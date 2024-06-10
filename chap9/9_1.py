# 练习 9.1：餐馆 创建⼀个名为 Restaurant 的类，为其
# __init__() ⽅法设置两个属性：restaurant_name 和
# cuisine_type。创建⼀个名为 describe_restaurant() 的⽅法
# 和⼀个名为 open_restaurant() 的⽅法，其中前者打印前述两项信
# 息，⽽后者打印⼀条消息，指出餐馆正在营业。
# 根据这个类创建⼀个名为 restaurant 的实例，分别打印其两个属
# 性，再调⽤前述两个⽅法。
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):

        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def decribe_restaurant(self):
        print("name:"+self.restaurant_name)
        print("cuisine_type:"+self.cuisine_type)


    def open_restaurant(self):
        print("the restaurant is open")

restaurant=Restaurant("domind","pizza")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.decribe_restaurant()
restaurant.open_restaurant()