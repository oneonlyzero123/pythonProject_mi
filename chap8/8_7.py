# 练习 8.7：专辑 编写⼀个名为 make_album() 的函数，它创建⼀个
# 描述⾳乐专辑的字典。这个函数应接受歌⼿名和专辑名，并返回⼀个
# 包含这两项信息的字典。使⽤这个函数创建三个表⽰不同专辑的字
# 典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给 make_album() 函数添加⼀个默认值为 None 的可选形参，以便存
# 储专辑包含的歌曲数。如果调⽤这个函数时指定了歌曲数，就将这个
# 值添加到表⽰专辑的字典中。调⽤这个函数，并⾄少在⼀次调⽤中指
# 定专辑包含的歌曲数。

def make_album(singer,songs,num=None):
    album = {'singer': singer,'songs': songs,}
    if num:
        album = {'singer': singer,'songs': songs,
                 'num': num,
                 }
    return album
result=make_album("adel",'there is ',3)
print(result)
result=make_album("zhou",'qingtian ',9)
print(result)
result=make_album("jj",'love ',7)
print(result)
