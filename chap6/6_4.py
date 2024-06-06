dictionary={'print': '打印',
    'Title':' 首字母大写',
    'Lower':'将字符串全部小写',
    'Sort':'对字符串进行首字母从小到大排序',
    'Reverse':'反转列表顺序',
            }
for key ,value in dictionary.items():
    print(key+':'+value)
dictionary['items']='将字典中的键和值一一放在列表里'
dictionary['.key']='将字典中的键一一放在列表里'
dictionary['.value']='将字典中的值一一放在列表里'
dictionary['set']='集合'
dictionary['==']='判断是否相等'
for key ,value in dictionary.items():
    print(key+':'+value)