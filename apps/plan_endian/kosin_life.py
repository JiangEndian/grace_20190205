#!/usr/bin/env python3

from MyPython3 import *

def alarm(info):
    cvlc_play_mp3('/home/ed/beginring_once.wav')
    #show_UI(info)
    runsyscmd('gnome-screenshot')

task1 = {
    539:'带钥匙,收拾,打包,과자/초크>노트북실,alt1+吃',
    755:'回去吃早饭半萝卜走人',
    955:'下山上山爬一下',
    1159:'做二饭吃午饭半萝卜学习运动' ,
    1459:'下山上山/出去购物去，休息下大脑',
    1550:'回屋躺刷alt，困睡半个点，晚上特别好学',
    #1730:'吃晚饭半萝卜并洗一件衣',
    1850:'一楼聚会',
    2129:'回去洗澡睡前英语梦中学',
    }
task2 = {
    539:'带钥匙,洗淑,6点晨更,带上计划本和圣经划线',
    711:'做二饭吃早饭去图书馆',
    855:'인간론 과목',
    1159:'吃午饭+alt+15分钟的极度困眠～(30m闹钟)',
    1555:'参加读经M201',
    1730:'做二饭吃晚饭半萝卜并洗一件衣',
    2129:'回去洗澡睡前英语梦中学',
    }
task3 = {
    539:'带钥匙,洗淑,6点晨更,带上计划本和圣经划线',
    711:'吃早饭刷牙收拾带零食去图书馆',
    855:'讲道学',
    1159:'경건회',
    1255:'신약총론',
    1550:'回屋躺刷alt，困睡半个点，晚上特别好学',
    1730:'做二饭吃晚饭半萝卜并洗一件衣',
    2129:'回去洗澡睡前英语梦中学',
    }
task4 = {
    539:'带钥匙,洗淑,6点晨更,带上计划本和圣经划线',
    711:'吃早饭回去刷牙收拾带零食去图书馆',
    855:'구약총론',
    1159:'경건회',
    1255:'히브리어',
    1550:'回屋躺刷alt，困睡半个点，晚上特别好学',
    1730:'做二饭吃晚饭半萝卜并洗一件衣',
    2129:'回去洗澡睡前英语梦中学',
    }
task5 = {
    539:'带钥匙,洗淑,6点晨更,带上计划本和圣经划线',
    711:'吃早饭去图书馆',
    855:'목자의도',
    1159:'做二饭吃午饭半萝卜走走购物-蛋/당근/라면',
    1550:'回屋躺刷alt，困睡半个点，晚上特别好学',
    1730:'吃晚饭半萝卜洗个衣' ,
    2129:'回去洗澡睡前英语梦中学',
    }
task6 = {
    539:'带钥匙,收拾,打包,과자/초크>노트북실,alt1+吃',
    755:'回去做二饭吃早饭半萝卜走人',
    1059:'吃午饭半萝卜노트북실学习运动,啊，乐天',
    1455:'出去走走，休息下',
    1550:'回屋躺刷alt，困睡半个点，晚上特别好学',
    1730:'做二饭吃晚饭半萝卜并洗一件衣',
    1820:'노트북실',
    2129:'回去洗澡睡前英语梦中学',
    }
task0 = {
    539:'带钥匙,客厅早读并啃萝卜',
    639:'吃早饭刷牙打包去한울교회',
    1550:'回屋躺刷alt，困睡半个点，晚上特别好学',
    1730:'做二饭吃晚饭半萝卜并看书加新',
    2129:'洗澡睡前英语梦中学',
    }
#time:task，每饭可以配1/2,1/3萝卜
tasks = [task0, task1, task2, task3, task4, task5, task6]

#alarm(1)
#exit()

while True:
    #得到今天周几并打印今天的任务
    today_number = int(getnowtime('week'))
    task_today = tasks[today_number]
    runsyscmd()
    print('\n%d' % today_number)
    for task_time in task_today:
        print(task_time, task_today[task_time])
    print()

    #得到明天周几并打印明天的任务
    if today_number == 6:
        tomorrow_number = 0
    else:
        tomorrow_number = today_number + 1
    print('\n%d' % tomorrow_number)
    task_tomorrow = tasks[tomorrow_number]
    for task_time in task_tomorrow:
        print(task_time, task_tomorrow[task_time])
    print()
    
    #判断当前时间是否有任务并打印
    now_time = int(getnowtime('hm'))
    for time in task_today:
        if now_time>time-10 and now_time<time:
        #这样，任务的时间分钟数目须>10
            #print('now_time:%d' % now_time)
            info = str(time) + '：' + task_today[time]
            print(info)
            alarm(info)
            

    sleep_ed(180)
