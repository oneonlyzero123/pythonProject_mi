# 练习 10.7：加法计算器 将为练习 10.6 编写的代码放在⼀个 while 循
# 环中，让⽤户在犯错（输⼊的是⽂本⽽不是数）后能够继续输⼊数。

while True:
    num_1 = input("请输入第一个数")
    num_2 = input("请输入第二个数")
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        print(num_1 + num_2)
    except ValueError:
        print("你输入的不是数，请输入整数")
