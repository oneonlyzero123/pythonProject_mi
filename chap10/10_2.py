
# 练习 10.2：C 语⾔学习笔记 可使⽤ replace() ⽅法将字符串中的特
# 定单词替换为另⼀个单词。下⾯是⼀个简单的⽰例，演⽰了如何将句
# ⼦中的 'dog' 替换为 'cat'：
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# 读取你刚创建的⽂件 learning_python.txt 中的每⼀⾏，将其中的 Python
# 都替换为另⼀门语⾔的名称，如 C。将修改后的各⾏都打印到屏幕
# 上。
filename='learning_python.txt'
with open(filename, 'r', encoding='gbk', errors='ignore') as file:
    lines=file.readlines()

for line in lines:
    line=line.replace('python','c语言')
    print(line.rstrip())
