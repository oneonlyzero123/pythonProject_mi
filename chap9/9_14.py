# 练习 9.14：彩票 创建⼀个列表或元素，其中包含 10 个数和 5 个字
# ⺟。从这个列表或元组中随机选择 4 个数或字⺟，并打印⼀条消息，
# 指出只要彩票上是这 4 个数或字⺟，就中⼤奖了。
from random import choice
ticket=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d']
ticket_good=[]
for num in range(1,5):
    ticket_good.append(choice(ticket))

print("只要彩票上是这 4 个数或字⺟:")
print(ticket_good)



