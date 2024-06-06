# 练习 7.4：⽐萨配料 编写⼀个循环，提⽰⽤户输⼊⼀系列⽐萨配料，
# 并在⽤户输⼊ 'quit' 时结束循环。每当⽤户输⼊⼀种配料后，都打
# 印⼀条消息，指出要在⽐萨中添加这种配料。

toppings = []

while True:
    topping = input("what do you want to add on your pizza?")

    print('we will add the '+topping+" on your pizza!")
    if topping == 'quit':
        print("all toppings you want to add:")
        print(toppings)
        break
    toppings.append(topping)
