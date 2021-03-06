#!/usr/bin/env python3


import virtkey #模拟按键的。。。
####sudo apt install python3-virtkey####
import time


vk = virtkey.virtkey()
def press_key(KEY, v=vk):
    v.press_unicode(ord(KEY))
    v.release_unicode(ord(KEY))
    time.sleep(0.01)


repeat_keys = input('输入要重复的按键:')
repeat_times = input('输入要重复%s的次数(3s后开始):' % repeat_keys)
time.sleep(3)

for i in range(int(repeat_times)):
    for key_one in repeat_keys:
        press_key(key_one)


