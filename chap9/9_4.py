# 练习 9.4：就餐⼈数 在为练习 9.1 编写的程序中，添加⼀个名为
# number_served 的属性，并将其默认值设置为 0。根据这个类创建⼀
# 个名为 restaurant 的实例。打印有多少⼈在这家餐馆就餐过，然后
# 修改这个值并再次打印。
# 添加⼀个名为 set_number_served() 的⽅法，⽤来设置就餐⼈
# 数。调⽤这个⽅法并向它传递新的就餐⼈数，然后再次打印这个值。
# 添加⼀个名为 increment_number_served() 的⽅法，⽤来让就餐
# ⼈数递增。调⽤这个⽅法并向它传递⼀个这样的值：你认为这家餐馆
# 每天可能接待的就餐⼈数。
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):

        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def decribe_restaurant(self):
        print("name:"+self.restaurant_name)
        print("cuisine_type:"+self.cuisine_type)


    def open_restaurant(self):
        print("the restaurant is open")

    def restaurant(self):
        print(str(self.number_served)+" people had dinner in the restaurant")

    def set_number_served(self,number):
        self.number_served=number

    def increment_number_served(self,increment_number):
        self.number_served+=increment_number



Pizza=Restaurant('domind','pizza')
Pizza.restaurant()


Pizza.number_served=23
Pizza.restaurant()

Pizza.set_number_served(41)
Pizza.restaurant()

Pizza.increment_number_served(100)
Pizza.restaurant()

