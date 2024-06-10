# 练习 8.8：⽤户的专辑 在为练习 8.7 编写的程序中，编写⼀个 while
# 循环，让⽤户输⼊歌⼿名和专辑名。获取这些信息后，使⽤它们来调
# ⽤ make_album() 函数并将创建的字典打印出来。在这个 while 循
# 环中，务必提供退出途径。

def make_album(singer,songs,num=None):
    album = {'singer': singer,'songs': songs,}
    if num:
        album = {'singer': singer,'songs': songs,
                 'num': num,
                 }
    return album


while True:
    singer_in=input("歌⼿名")
    if singer_in=='quit':
        break

    songs_in=input("专辑名")
    if songs_in=="quit":
        break
    result=make_album(singer_in,songs_in)
    print(result)
