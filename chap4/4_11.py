#4_1的代码
pizzas=['chicken pizza','beef pizza','pig pizza']
#4_11
friend_pizzas=pizzas[:]
pizzas.append("bolo pizza")
print("my favorite pizzas are:")
for value in pizzas:
    print(value)
print("my friend's favorite pizzas are:")
for value in friend_pizzas:
    print(value)