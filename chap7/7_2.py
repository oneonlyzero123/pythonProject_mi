#练习 7.2：餐馆订位 编写⼀个程序，询问⽤户有多少⼈⽤餐。如果超
#过 8 个⼈，就打印⼀条消息，指出没有空桌；否则指出有空桌。

info=input("how many people will go there?")
info=int (info)
if info>8:
    print("no free table")
else:
    print("table still free ")