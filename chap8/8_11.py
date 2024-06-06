# 练习 8.11：消息归档 修改为练习 8.10 编写的程序，在调⽤函数
# send_messages() 时，向它传递消息列表的副本。调⽤
# send_messages() 函数后，将两个列表都打印出来，确认原始列表
# 保留了所有的消息。
words=['it is good','it is bad','it is ok']
def show_messages(words):
    for word in words:
        print(word)

def send_messages(words,send_messages):
    while words:
        current_word=words.pop()
        print(current_word)
        send_messages.append(current_word)



send_message=[]
send_messages(words[:],send_message)
print(words)
print(send_message)