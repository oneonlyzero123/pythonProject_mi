# 练习 7.5：电影票 有家电影院根据观众的年龄收取不同的票价：不到
# 3 岁的观众免费；3（含）〜12 岁的观众收费 10 美元；年满 12 岁的观
# 众收费 15 美元。请编写⼀个循环，在其中询问⽤户的年龄，并指出其
# 票价。

age=input("how old are you?")
while True:
    age = int(input("how old are you?"))
    if age <3:
        print("for free")
    elif 3<=age<12:
        print("you need to pay 10 dollars every ticket.")
    else:
        print("you need to pay 15 dollars every ticket.")
