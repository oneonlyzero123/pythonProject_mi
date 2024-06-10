
# 练习 10.12：记住喜欢的数 将你在完成练习 10.11 时编写的两个程序
# 合⽽为⼀。如果存储了⽤户喜欢的数，就向⽤户显⽰它，否则提⽰⽤
# 户输⼊⾃⼰喜欢的数并将其存储在⽂件中。运⾏这个程序两次，看看
# 它是否像预期的那样⼯作。

import json
filename='num_favorite.json'
try:
    with open(filename) as f_obj:
        number_favorite = json.load(f_obj)
except FileNotFoundError:
    num_favorite = input("请输入你最喜欢的数")
    with open(filename, 'w') as f_obj:
        json.dump(num_favorite, f_obj)
        print("我之后会记得你最喜欢的数 "+num_favorite+ " ")
else:
    print("I know your favorite number! It's " + number_favorite)
