# 练习 10.5：访客簿 编写⼀个 while 循环，提⽰⽤户输⼊其名字。收
# 集⽤户输⼊的所有名字，将其写⼊ guest_book.txt，并确保这个⽂件中
# 的每条记录都独占⼀⾏。
filename='guest_book.txt'
while True:
    name = input("请输入您的名字。输入quit退出")
    if name=='quit':
        break
    else:
        with open(filename, 'a') as file:
            file.write(name + "\n")
        with open(filename, 'r') as file:
            print(file.read())


