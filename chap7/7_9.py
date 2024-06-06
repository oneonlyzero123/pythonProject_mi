# 练习 7.9：五⾹烟熏⽜⾁卖完了 使⽤为练习 7.8 创建的列表
# sandwich_orders，并确保 'pastrami' 在其中⾄少出现了三次。
# 在程序开头附近添加这样的代码：先打印⼀条消息，指出熟⾷店的五
# ⾹烟熏⽜⾁（pastrami）卖完了；再使⽤⼀个 while 循环将列表
# sandwich_orders 中的 'pastrami' 都删除。确认最终的列表
# finished_sandwiches 中未包含 'pastrami'。

sandwich_orders=['beef','chicken','tomato','pastrami','pastrami','pastrami']
finished_sanwiched=[]

print('熟⾷店的五⾹烟熏⽜⾁（pastrami）卖完了')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    sandwich_done=sandwich_orders.pop()
    finished_sanwiched.append(sandwich_done)
print(finished_sanwiched)
