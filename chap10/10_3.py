
# 练习 10.3：简化代码 本节前⾯的程序 file_reader.py 中使⽤了⼀个临
# 时变量 lines，来说明 splitlines() 的⼯作原理。可省略这个临
# 时变量，直接遍历 splitlines() 返回的列表：
# for line in contents.splitlines():
# 对于本节的每个程序，都删除其中的临时变量，让代码更简洁。
from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text()
for line in contents.splitlines():
    print (line)
