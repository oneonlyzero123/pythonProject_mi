
# 练习 10.9：静默的猫和狗 修改你在练习 10.8 中编写的 except 代码
# 块，让程序在⽂件不存在时静默失败。
filename='cats.txt'
# with open('cats.txt','w') as file:
#     file.write('tom ')
#     file.write('jenny ')
#     file.write('rose ')
try:
    with open(filename) as file:
        print(file.read())

except FileNotFoundError:
    pass


filename = 'dogs.txt'
try:
    with open(filename) as file:
        print(file.read())
except FileNotFoundError:
    pass