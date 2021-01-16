#!/usr/bin/env python3

from MyPython3 import *
import random

input('神爱感受器（无层次）（感受/确认——神爱）')

def new_eye(body):
    eye = input('请输入一个眼睛：')
    body.append(eye)
    dump2file('eyes4love.list', body)

def load_eyes():
    return loadffile('eyes4love.list')

all_eyes = load_eyes()

random.shuffle(all_eyes)
body = all_eyes.copy()

for eye in all_eyes:
    runsyscmd()
    print()
    print(eye)
    CMD = input()
    if CMD == 'ADD':
        new_eye(all_eyes)
        input()
    elif CMD == 'EDIT':
        i = all_eyes.index(eye)
        all_eyes[i] = input('输入修改后的：')
        print('修改前:%s\n修改后:%s' % (body[i], all_eyes[i]))
        input('确认？')
        dump2file('eyes4love.list', all_eyes)
    elif CMD == 'DEL':
        i = body.index(eye)
        print(body[i])
        input('确认？')
        body.pop(i)
        dump2file('eyes4love.list', body)
