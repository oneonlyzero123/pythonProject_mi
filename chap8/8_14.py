# 练习 8.14：汽⻋ 编写⼀个函数，将⼀辆汽⻋的信息存储在字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。在
# 调⽤这个函数时，提供必不可少的信息，以及两个名值对，如颜⾊和
# 选装配件。这个函数必须能够像下⾯这样调⽤：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息

def make_car(maker,kind,**info):
    profile={}
    profile['maker']=maker
    profile['kind']=kind
    for key,value in info.items():
        profile[key]=value
    return profile
make_car_own=make_car('subaru', 'outback', color='blue', tow_package=True)
print(make_car_own)
