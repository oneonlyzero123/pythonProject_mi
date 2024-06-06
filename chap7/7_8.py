# 练习 7.8：熟⾷店 创建⼀个名为 sandwich_orders 的列表，其中
# 包含各种三明治的名字，再创建⼀个名为 finished_sandwiches
# 的空列表。遍历列表 sandwich_orders，对于其中的每种三明治，
# 都打印⼀条消息，如“I made your tuna sandwich.”，并将其移到列表
# finished_sandwiches 中。当所有三明治都制作好后，打印⼀条消
# 息，将这些三明治列出来。
sandwich_orders=['beef','chicken','tomato']
finished_sanwiched=[]
while sandwich_orders:
    sandwich_done=sandwich_orders.pop()
    print("i made your " + sandwich_done + " sanwich")
    finished_sanwiched.append(sandwich_done)

print(finished_sanwiched)