# 练习 10.8：猫和狗 创建⽂件 cats.txt 和 dogs.txt，在第⼀个⽂件中⾄少
# 存储三只猫的名字，在第⼆个⽂件中⾄少存储三条狗的名字。编写⼀
# 个程序，尝试读取这些⽂件，并将其内容打印到屏幕上。将这些代码
# 放在⼀个 try-except 代码块中，以便在⽂件不存在时捕获
# FileNotFoundError 异常，并显⽰⼀条友好的消息。将任意⼀个⽂
# 件移到另⼀个地⽅，并确认 except 代码块中的代码将正确地执⾏。
filename='cats.txt'
# with open('cats.txt','w') as file:
#     file.write('tom ')
#     file.write('jenny ')
#     file.write('rose ')
try:
    with open(filename) as file:
        print(file.read())

except FileNotFoundError:
    print("文件 "+filename+"不存在，请确保文件存在！")


filename = 'dogs.txt'
try:
    with open(filename) as file:
        print(file.read())
except FileNotFoundError:
    print("文件 "+filename+"不存在，请确保文件存在！")


# with open('dogs.txt','w') as file:
#     file.write('Dom ')
#     file.write('Renny ')
#     file.write('Wose ')

