# 练习 8.9：消息 创建⼀个列表，其中包含⼀系列简短的⽂本消息。将
# 这个列表传递给⼀个名为 show_messages() 的函数，这个函数会打
# 印列表中的每条⽂本消息。

words=['it is good','it is bad','it is ok']
def show_messages(words):
    for word in words:
        print(word)

show_messages(words)
