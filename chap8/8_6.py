# 练习 8.6：城市名 编写⼀个名为 city_country() 的函数，它接受
# 城市的名称及其所属的国家。这个函数应返回⼀个格式类似于下⾯的
# 字符串：
# "Santiago, Chile"
# ⾄少使⽤三个城市⾄国家对调⽤这个函数，并打印它返回的值。
def city_country(city,country):
    city_country=city+", "+country
    return city_country
result=city_country('Beijing','China')
print(result)
result=city_country('Shanghai','China')
print(result)
result=city_country('NewYork','USA')
print(result)

