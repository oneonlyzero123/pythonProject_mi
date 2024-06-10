# 练习 9.9：电池升级 在本节最后⼀个 electric_car.py 版本中，给
# Battery 类添加⼀个名为 upgrade_battery() 的⽅法。这个⽅法
# 检查电池容量，如果电池容量不是 65，就设置为 65。创建⼀辆电池容
# 量为默认值的电动汽⻋，调⽤⽅法 get_range()，然后对电池进⾏升
# 级，并再次调⽤ get_range()。你将看到这辆汽⻋的续航⾥程增加
# 了
#
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometer(self):
        print(str(self.odometer_reading))

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage

        else:
            print("no!")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles


class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print(str(self.battery_size))

    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270

        message=str(range)
        print(message)

    def upgrade_battery(self):
        if self.battery_size!=85:
            self.battery_size=85



class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla=ElectricCar('tesla','model s',2016)
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()








