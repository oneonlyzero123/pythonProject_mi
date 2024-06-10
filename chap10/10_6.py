# 练习 10.6：加法运算 在提⽰⽤户提供数值输⼊时，常出现的⼀个问
# 题是，⽤户提供的是⽂本⽽不是数。在这种情况下，当你尝试将输⼊
# 转换为整数时，将引发 ValueError 异常。编写⼀个程序，提⽰⽤户
# 输⼊两个数，再将它们相加并打印结果。在⽤户输⼊的任意⼀个值不
# 是数时都捕获 ValueError 异常，并打印⼀条友好的错误消息。对你
# 编写的程序进⾏测试：先输⼊两个数，再输⼊⼀些⽂本⽽不是数。


num_1=input("请输入第一个数")
num_2=input("请输入第二个数")
try:
    num_1=int(num_1)
    num_2=int(num_2)
    print(num_1+num_2)
except ValueError:
    print("你输入的不是数，请输入整数")



def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
        msg=filename+" doed not exist."
        print(msg)
    else:
        words=contents.split()
        num_words=len(words)
        print(filename+" has about "+str(num_words)+" words")

filename='guest_book.txt'
count_words(filename)