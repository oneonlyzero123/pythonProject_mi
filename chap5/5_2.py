#检查两个字符串相等和不相等
car_1='audi'
car_2='BMW'
print('检查两个字符串相等和不相等')
if car_1==car_2:
    print("yes")
else:
    print('no')

#使用函数lower（）
print('\n使用函数lower（）')
if car_2.lower()=='bmw':
    print("yes")
else:
    print('no')
#检查两个数字相等，不等，大于，小于，大于等于，小于等于
print('\n检查两个数字相等，不等，大于，小于，大于等于，小于等于')
print(32==21)
print(32!=21)
print(32>21)
print(32<21)
print(32>=21)
print(32<=21)

#使用关键字and和or的测试
age=26
print('\n使用关键字and和or的测试')

if 32!=age and 24<age:
    print('yes')
else:
    print('no')

if 32==age or 24<age:
    print('yes')
else:
    print('no')

#测试特定的值是否包含在列表中，

print('\n测试特定的值是否包含在列表中')
list_test=[1,2,3,4]
if 2 in list_test:
    print("it exists")

#测试特定的值是否未包含在列表中

print('\n测试特定的值是否未包含在列表中')
if 5 not in list_test:
    print("it does not exist")