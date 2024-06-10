# 练习 10.10：常⻅单词 访问古登堡计划，找⼀些你想分析的图书。下
# 载这些作品的⽂本⽂件或将浏览器中的原始⽂本复制到⽂本⽂件中。
# 可以使⽤⽅法 count() 来确定特定的单词或短语在字符串中出现了多
# 少次。例如，下⾯的代码计算 'row' 在⼀个字符串中出现了多少次：
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# 请注意，通过使⽤ lower() 将字符串转换为全⼩写的，可捕捉要查找
# 的单词的各种格式，⽽不管其⼤⼩写如何。
# 编写⼀个程序，读取你在古登堡计划中获取的⽂件，并计算单词
# 'the' 在每个⽂件中分别出现了多少次。这⾥计算得到的结果并不准
# 确，因为诸如 'then' 和 'there' 等单词也被计算在内了。请尝试计
# 算 'the '（包含空格）出现的次数，看看结果相差多少。
filename='guest.txt'
with open(filename) as f_obj:
    words=f_obj.read()
    print(words)
    print(words.lower().count('the '))

