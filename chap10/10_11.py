# 练习 10.11：喜欢的数 编写⼀个程序，提⽰⽤户输⼊⾃⼰喜欢的数，
# 并使⽤ json.dumps() 将这个数存储在⽂件中。再编写⼀个程序，从
# ⽂件中读取这个值，并打印如下消息。
# I know your favorite number! It's _____.
num_favorite=input("请输入你最喜欢的数")
import json
filename='num_favorite.json'
with open(filename,'w') as f_obj:
    json.dump(num_favorite,f_obj)

with open(filename) as f_obj:
    number_favorite=json.load(f_obj)
    print("I know your favorite number! It's " + number_favorite)




