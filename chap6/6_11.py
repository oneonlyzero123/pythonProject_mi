#练习 6.11：城市 创建⼀个名为 cities 的字典，将三个城市名⽤作
#键。对于每座城市，都创建⼀个字典，并在其中包含该城市所属的国
#家、⼈⼝约数以及⼀个有关该城市的事实。表⽰每座城市的字典都应
#包含 country、population 和 fact 等键。将每座城市的名字以及
#相关信息都打印出来。

cities={'beijing':
            {'country':'China',
            'population':'100 minlion',
             'fact':'the capital of China',},
        'Washington':
            {'country':'USA',
            'population':'100 minlion',
             'fact':'the capital of USA',},
        'shanghai':
            {'country':'China',
            'population':'100 minlion',
             'fact':'very properrous',}
        }
for city,info in cities.items():
    print(city+": ")
    country=info['country']
    population=info['population']
    fact=info['fact']
    print("from "+country+" "+"with "+ population+" "+",it is "+fact)
