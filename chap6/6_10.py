#练习 6.10：喜欢的数 2 修改为练习 6.2 编写的程序，让每个⼈都可以
#有多个喜欢的数字，然后将每个⼈的名字及其喜欢的数打印出来。
favorite={'tom':[7,8],
    'jack':[3,13],
    'rose':[12,65],
    'lucy':[14,31],
    'jenny':[77,7],
    }# --coding:utf-8--
for name ,nums in favorite.items():
    print(f"{name}'s favorite number is ")
    for num in nums:
        print(num)