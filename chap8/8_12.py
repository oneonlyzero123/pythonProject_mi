# 练习 8.12：三明治 编写⼀个函数，它接受顾客要在三明治中添加的
# ⼀系列⾷材。这个函数只有⼀个形参（它收集函数调⽤中提供的所有
# ⾷材），并打印⼀条消息，对顾客点的三明治进⾏概述。调⽤这个函
# 数三次，每次都提供不同数量的实参。
def sandwiches(*toppings):
    print("your sandwich is with all following :")
    for top in toppings:

        print(top)
sandwiches(1,2,3)
