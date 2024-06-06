# 练习 8.13：⽤户简介 复制前⾯的程序 user_profile.py，在其中调⽤
# build_profile() 来创建有关你的简介。在调⽤这个函数时，指定
# 你的名和姓，以及三个⽤来描述你的键值对。
def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key ,value in user_info.items():
        profile[key]=value
    return profile

user_profile=build_profile('wan','zero',location='wuhan',school='hust',age=21)
print(user_profile)