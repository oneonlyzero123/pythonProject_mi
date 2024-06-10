# 练习 9.13：骰⼦ 创建⼀个 Die 类，它包含⼀个名为 sides 的属性，
# 该属性的默认值为 6。编写⼀个名为 roll_die() 的⽅法，它打印位
# 于 1 和骰⼦⾯数之间的随机数。创建⼀个 6 ⾯的骰⼦并掷 10 次。
# 创建⼀个 10 ⾯的骰⼦和⼀个 20 ⾯的骰⼦，再分别掷 10 次。


from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        roll=randint(1,self.sides)
        print("你掷出了： "+str(roll))

    def roll_ten(self):
        for num in range(1,10):
            self.roll_die()

print("6面骰子")
die_6=Die()
die_6.roll_ten()


print("10面骰子")

die_10=Die()
die_10.sides=10
die_10.roll_ten()


print("20面骰子")

die_20=Die()
die_20.sides=20
die_20.roll_ten()