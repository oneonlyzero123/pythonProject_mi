import json
list=[]#list为一个中间列表，用来承接信息和制作字典
dic={}#初始化字典
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

for key,value in dic.items():#key为frame，value为各进程时间，但是此时仍未分开
    for i in range(0,len(value)):
        value[i] = value[i].rsplit(":", 1)#将value中各进程A,B开始/结束与其时间分开
        dict1 = dict([(value[i][0], int(value[i][1]))])#将进程A/B开始/结束作为新字典的key,将时间作为value
        value[i]=dict1#将列表中对应的元素变为字典

    dic[key]=value#把新的value和key联系起来

    for diction in value:
        for key,value_di in diction.items():

            # 记录每个进程的耗时

            if key=='ProcessA:start':
                time_a_start=value_di

                if i==0:
                    time_start=value_di
                    i+=1#保证只记录第一个A：start的时间

            if key=='ProcessA:end':
                time_a_end=value_di
                t_1 = time_a_end - time_a_start
                frame_a.append(t_1)

            if key=='ProcessB:start':
                time_b_start=value_di

            if key=='ProcessB:end':
                time_b_end=value_di
                t_2 = time_b_end - time_b_start
                frame_b.append(t_2)

        # print(diction)
    if len(value) == 4:#如果该frame同时有进程A,B,那么对应的value的长度是4

        key_number+=1
        key_AB_number+=1

        for diction_AB in value:
            for key_AB, value_AB in diction_AB.items():
                if key_AB == 'ProcessA:start':  # 记录每个进程的耗时
                    frame_start = value_AB
                if key_AB == 'ProcessB:end':
                    frame_end = value_AB
                    frame_time = frame_end - frame_start
                    frame_time_list.append(frame_time)



time_all=time_b_end-time_start#最后迭代出来的time_b_end是最后的processB


#现在要删掉frame中的0值，其实应该有更加简洁优美的方式做到以上，然而get函数一直报错，只能如此
while 0 in frame_a:
    frame_a.remove(0)
while 0 in frame_b:
    frame_b.remove(0)
#
# print(frame_a)
# print(frame_b)


#a的平均值
average_1=sum(frame_a)/len(frame_a)
# print(average_1)
frame_a.sort()#对frame_a进行从小到大排列
# print(frame_a)
#排列在第0.99*len的就是p_99值
process_A_p_99=int(len(frame_a)*0.99)

process_A_p_90=int(len(frame_a)*0.90)


#b的平均值
average_2=sum(frame_b)/len(frame_b)
print(key_AB_number)
frame_b.sort()
process_B_p_99=int(len(frame_b)*0.99)
process_B_p_90=int(len(frame_b)*0.90)
#

# 系统平均吞吐量
average_system_time=time_all/key_number


#平均每帧耗时，仅仅计算同时有A,B的帧

average_frame_time=sum(frame_time_list)/key_AB_number


result_dict={"ProcessA的平均耗时":average_1,
             "ProcessB的平均耗时":average_2,
             "ProcessA的P99耗时":frame_a[process_A_p_99],
             "ProcessB的P99耗时":frame_b[process_B_p_99],
             "ProcessA的P90耗时":frame_a[process_A_p_90],
             "ProcessB的P90耗时":frame_b[process_B_p_90],
             "系统平均吞吐量":average_system_time,
             "平均每帧耗时":average_frame_time

             }
json_str = json.dumps(result_dict,ensure_ascii=False)
with open('result.json', 'w',encoding='utf-8') as json_file:
    json_file.write(json_str)

