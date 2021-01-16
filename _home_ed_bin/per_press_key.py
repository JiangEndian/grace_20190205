#!/usr/bin/env python3


import virtkey #模拟按键的。。。
####sudo apt install python3-virtkey####
import time


vk = virtkey.virtkey()
def press_key(KEY, v=vk):
    v.press_unicode(ord(KEY))
    v.release_unicode(ord(KEY))
    time.sleep(0.1)


key = input('输入要按的按键:')
repeat_times = int(input('输入间隔时间(3s后开始%s）:' % key))
time.sleep(3)

while True:
    press_key(key)
    time.sleep(repeat_times)


