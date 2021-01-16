#!/usr/bin/env python3

from MyPython3 import *

KEY = input('按哪个键：')
times = int(input('按几次=号:')) + 1

sleep_ed(3)

def press_n_eq(times):
    for i in range(times):
        #print('一次了%s' % times)
        press_key('=')

for i in range(times):
    #print(i)
    for j in range(1,10):
        #print(j)
        press_key(KEY)
        press_n_eq(i)
        press_key(str(j))
        press_key(' ')
    #press_key('=')
