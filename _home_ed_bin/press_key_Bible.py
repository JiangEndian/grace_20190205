#!/usr/bin/env python3


import virtkey #模拟按键的。。。
####sudo apt install python3-virtkey####
import time
from MyPython3 import *

vk = virtkey.virtkey()
def press_key(KEY, v=vk):
    v.press_unicode(ord(KEY))
    v.release_unicode(ord(KEY))
    time.sleep(0.3)


key_list1 = 'gkdtkd rlQjgkfk ' #항상 기뻐하라 
key_list2 = 'tnlwl akfrh rlehgkfk ' #쉬지 말고 기도하라
key_list3 = 'qjatkdp rkatkgkfk ' #범사에 감사하라 
key_list4 = 'eptkffhslrkwjstj 5:16-18 '

key_list = [key_list1, key_list2, key_list3, key_list4]

while True:
    for key_ in key_list:
        for key in key_:
            press_key(key)
        vk.press_keysym(65293)
        vk.release_keysym(65293)
        time.sleep(0.5)
        vk.press_keysym(65293)
        vk.release_keysym(65293)
        time.sleep(0.5)
        vk.press_keysym(65293)
        vk.release_keysym(65293)
        time.sleep(0.5)
    time.sleep(2.5)
    runsyscmd()
    time.sleep(2)

