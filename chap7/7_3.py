#练习 7.3：10 的整数倍 让⽤户输⼊⼀个数，并指出这个数是否是 10
#的整数倍
prom="please input a figure,then i will tell you if it is 10的整数倍"
number=int(input(prom))
if number %10==0:
    print("yes,it is!")
else:
    print("no, it is not!")
