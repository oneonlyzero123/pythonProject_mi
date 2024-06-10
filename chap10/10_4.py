# 练习 10.4：访客 编写⼀个程序，提⽰⽤户输⼊其名字。在⽤户做出
# 响应后，将其名字写⼊⽂件 guest.txt。
filename='guest.txt'
with open(filename,'w') as file:
    name=input("请输入您的名字。")
    file.write(name)
with open(filename) as file:
    print(file.read())

