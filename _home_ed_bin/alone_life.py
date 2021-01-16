#!/usr/bin/env python3

from newestMyPython3 import *

#改为两个番茄钟
def a_lesson(class_time=50):
    cvlc_play_mp3('~/beginring.mp3', 1, '-', '=')
    show_UI('准备上课')
    print('上课：%s' % getnowtime('hm'))
    time.sleep(class_time*60/2)

    show_UI('准备休息')
    print('休息：%s' % getnowtime('hm'))
    cvlc_play_mp3('~/endring_once.wav', 1, '-', '=')
    time.sleep(5*60)

    cvlc_play_mp3('~/beginring_once.wav', 1, '-', '=')
    show_UI('准备开始')
    print('开始：%s' % getnowtime('hm'))
    time.sleep(class_time*60/2)

    show_UI('准备下课')
    print('下课：%s' % getnowtime('hm'))
    cvlc_play_mp3('~/endring.mp3', 1, '-', '=')

start_time_list = ['0600', #清晨
    '0750', '0855', '1000', '1105', #上午
    '1420', '1525', '1630', #下午
    '1810', '1915', '2020', '2125'] #晚上
#print(getnowtime('hm'))

while True:
    for wait_time in start_time_list:
        if getnowtime('hm') == wait_time:
            if wait_time == '0600':
                runsyscmd()
            a_lesson()
    time.sleep(1)

