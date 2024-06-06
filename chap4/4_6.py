for num in range(1,21):
    print(num)
for num in range(1,10):
    print(num)
list_1=range(1,1000001)
print(min(list_1))
print(max(list_1))
print(sum(list_1))
for num in range(1,21,2):
    print(num)
list_for3=range(3,31,3)
for num in list_for3:
    print(num)
list_lifang=[]
for value in range(1,11):
    lifang=value**3
    list_lifang.append(lifang)
for value in list_lifang:
    print(value)
list_lifang=[value**3 for value in range(1,11)]
print(list_lifang)