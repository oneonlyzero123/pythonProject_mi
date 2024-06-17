import matplotlib.pyplot as plt
import numpy as np
list=[]#list为一个中间列表，用来承接信息和制作字典
dic={}#初始化字典
frame_list=[]
#记录A，B的帧数
frame_a=[]
frame_b=[]

#此列表记录每帧的总耗时
frame_time_list=[]


#初始化A,B的起始时间
time_a_start=0
time_a_end=0
time_b_start=0
time_b_end=0

key_number=0#记录有多少帧数
key_AB_number=0#记录有AB进程的帧数
i=0#用来计数，确保只运行一次



with (open('trace_111.log','r') as file):
    lines=file.readlines()
    for line in lines:
        line_1=line[76:]
        line_1=line_1.rstrip("\n")
        line_1=line_1.split("|")
        del line_1[1]
        del line_1[1]#除去不用的信息，只留下需要的信息：A,B的起始时间和帧数。

        list.append(line_1)
        for i in list:
            dic[i[0]]=[]
        for i in list:
            dic[i[0]].append(i[1])#将原始数据化成字典，帧数frame为key，value是该帧数下，A,B的进程时间

for key,value in dic.items():#key为frame，value为各进程时间，但是此时仍未分开
    for i in range(0,len(value)):
        value[i] = value[i].rsplit(":", 1)#将value中各进程A,B开始/结束与其时间分开
        dict1 = dict([(value[i][0], int(value[i][1]))])#将进程A/B开始/结束作为新字典的key,将时间作为value
        value[i]=dict1#将列表中对应的元素变为字典

    dic[key]=value#把新的value和key联系起来
    #要取出帧号数
    frame_id=key.split(":")
    try:
        frame_id = int(frame_id[-1])
        frame_list.append(frame_id)
    except ValueError:
        pass

    for diction in value:
        for key_process,value_di in diction.items():

            # 记录每个进程的耗时

            if key_process=='ProcessA:start':
                time_a_start=value_di

                if i==0:
                    time_start=value_di
                    i+=1#保证只记录第一个A：start的时间

            if key_process=='ProcessA:end':
                time_a_end=value_di
                # 从时间开始，到时间结束，步长随意。
                a = np.arange(time_a_start-90706,time_a_end-90706,1)
                p1 = frame_id+a*0
                plt.plot(a,p1,label="$P1$",color="y",linewidth=2)


            if key_process=='ProcessB:start':
                time_b_start=value_di

            if key_process=='ProcessB:end':
                time_b_end=value_di
                b = np.arange(time_a_start - 90706, time_a_end - 90706, 1)
                p1 = frame_id + b * 0
                plt.plot(b, p1, label="$P1$", color="r", linewidth=2)





plt.xlabel('time stamp')
plt.ylabel('frame_id')
plt.show()
