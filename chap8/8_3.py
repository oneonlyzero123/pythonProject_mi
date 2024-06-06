
# 练习 8.3：T 恤 编写⼀个名为 make_shirt() 的函数，它接受⼀个
# 尺码以及要印到 T 恤上的字样。这个函数应该打印⼀个句⼦，简要地
# 说明 T 恤的尺码和字样。
# 先使⽤位置实参调⽤这个函数来制作⼀件 T 恤，再使⽤关键字实参来
# 调⽤这个函数。

def make_shirt(size,words):
    print('the shirt is '+size +" and with "+words+" on it")
make_shirt('36','night')
make_shirt(size='35',words='moon')

