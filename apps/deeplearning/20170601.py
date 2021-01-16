#!/usr/bin/env python3

import numpy as np
def sigmodf(x):
    return 1 / (1 + np.exp(-x))
def daof(x):
    return x * (1 - x)

X = np.array([ [0,0,1],
                [0,1,1],
                [1,1,0],
                [1,0,0],
                [0,1,0] ])  #5-3

y = np.array([ [0],
                [1],
                [1],
                [0],
                [0] ])  #5-1

np.random.seed(1)

#中间层可随意(本次4为最好)
syn0 = 2 * np.random.random((3,4)) -1  #3-4
syn1 = 2 * np.random.random((4,1)) -1  #4-1

for i in range(10000):
    l0 = X  #5-3
    l1 = sigmodf(np.dot(l0, syn0))  #5-4
    l2 = sigmodf(np.dot(l1, syn1))  #5-1

    l2_error = y - l2  #5-1
    l2_delta = l2_error * daof(l2)  #5-1

    l1_error = l2_delta.dot(syn1.T)  #5-4
    l1_delta = l1_error * daof(l1)  #5-4

    syn1 += l1.T.dot(l2_delta)  #4-1
    syn0 += l0.T.dot(l1_delta)  #3-4
print(l2)

#底下这个代码就是失败的代码，没有可读性，逻辑也混乱。。。
while True:
    print(sigmodf(np.dot(sigmodf(np.dot([int(input('Input num:')),int(input('Input num:')),int(input('Input num:'))],syn0)),syn1)))
