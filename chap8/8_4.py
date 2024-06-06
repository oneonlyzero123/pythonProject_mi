# 练习 8.4：⼤号 T 恤 修改 make_shirt() 函数，使其在默认情况下
# 制作⼀件印有
# “I love Python”字样的⼤号 T 恤。调⽤这个函数分别制作⼀件印有默认
# 字样的⼤号 T 恤，⼀件印有默认字样的中号 T 恤，以及⼀件印有其他
# 字样的 T 恤（尺码⽆关紧要）。

def make_shirt(size='large',words='i love Python'):
    print('the shirt is '+size +" and with "+words+" on it")
make_shirt()
make_shirt(size='medium')
make_shirt(words="water")