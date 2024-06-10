# 练习 8.10：发送消息 在为练习 8.9 编写的程序中，编写⼀个名为
# send_messages() 的函数，将每条消息都打印出来并移到⼀个名为
# sent_messages 的列表中。调⽤ send_messages() 函数，再将两
# 个列表都打印出来，确认把消息移到了正确的列表中。

words=['it is good','it is bad','it is ok']
def show_messages(words):
    for word in words:
        print(word)

def send_messages(words,send_message):
    while words:
        current_word=words.pop()
        print(current_word)
        send_message.append(current_word)

send_message=[  ]
send_messages(words,send_message)
print(words)
print(send_message)
