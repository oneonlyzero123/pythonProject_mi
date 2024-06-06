# 练习 7.6：三种出路 以不同的⽅式完成练习 7.4 或练习 7.5，在程序中
# 采取如下做法。
# 在 while 循环中使⽤条件测试来结束循环。
# 使⽤变量 active 来控制循环结束的时机。
# 使⽤ break 语句在⽤户输⼊ 'quit' 时退出循环。


# 在 while 循环中使⽤条件测试来结束循环。
age = input("how old are you?")
while age!='quit':

    if int(age) < 3:
        print("for free")
    elif 3 <= int(age) < 12:
        print("you need to pay 10 dollars every ticket.")
    elif int(age) >= 12:
        print("you need to pay 15 dollars every ticket.")
    age = input("how old are you?")

# 使⽤变量 active 来控制循环结束的时机。
active=1
while active==1:
    age = input("how old are you?")
    if age=='quit':
        active=0
    if age!='quit':
        if int(age) <3:
            print("for free")
        elif 3<=int(age)<12:
            print("you need to pay 10 dollars every ticket.")
        elif int(age)>=12:
            print("you need to pay 15 dollars every ticket.")






# 使⽤ break 语句在⽤户输⼊ 'quit' 时退出循环。
age=0
while True:
    age = input("how old are you?")
    if age=='quit':
        break
    if age!='quit':
          if int(age) <3:
              print("for free")
          elif 3<=int(age)<12:
            print("you need to pay 10 dollars every ticket.")
          elif int(age)>=12:
            print("you need to pay 15 dollars every ticket.")
