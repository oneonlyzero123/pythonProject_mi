# 练习 9.15：彩票分析 可以使⽤⼀个循环来理解中前述彩票⼤奖有多
# #难。为此，创建⼀个名为 my_ticket 的列表或元组，再编写⼀个循
#  环，不断地随机选择数或字⺟，直到中⼤奖为⽌。请打印⼀条消息，
#  报告执⾏多少次循环才中了⼤奖。


from random import choice
i=0
ticket=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d']
ticket_good=[]
for num in range(1,5):
    ticket_good.append(choice(ticket))

print("只要彩票上是这 4 个数或字⺟:")
print(ticket_good)

my_ticket=[]
while True:
    for num in range(1,5):
        my_ticket.append (choice(ticket))
    if my_ticket==ticket_good:
        print("中大奖！")
        print("循环了"+str(i)+"次中奖")
        break
    else:
        print(my_ticket)
        i+=1
        print("没中奖！")
        my_ticket=[]