# 练习 7.10：梦想中的度假胜地 编写⼀个程序，调查⽤户梦想中的度
# 假胜地。使⽤类似于“If you could visit one place in the world, where
# would you go?”的提⽰，并编写⼀个打印调查结果的代码块

result={}

active=1
while active:
    name = input("what is your name")
    pro = "If you could visit one place in the world,"
    pro += 'where would you go?'
    place = input(pro)
    result[name]=place
    problem=input("do you have something else to say?(yes/no)")
    if problem=='no':
        active=0

for name,pro in result.items():
    print('name: '+name)
    print("place: "+place)