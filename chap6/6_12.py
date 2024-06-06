#练习 6.12：扩展 本章的⽰例⾜够复杂，能以很多⽅式进⾏扩展。请
#对本章的⼀个⽰例进⾏扩展：添加键和值，调整程序要解决的问题，
#或改进输出的格式。

favorite={'tom':[7,8],
    'jack':[3,13],
    'rose':[12,65],
    'lucy':[14,31],
    'jenny':[77,7],
    'jerry':[23,32]
    }# --coding:utf-8--
for name ,nums in favorite.items():
    print(f"{name}'s favorite number is ")
    for num in nums:
        print(num)