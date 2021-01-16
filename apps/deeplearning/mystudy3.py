#!/usr/bin/env python3

import numpy as np
def mysigmodfun(x,deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

X = np.array([ [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])  #4-3

y = np.array([ [0],
                [0],
                [0],
                [1] ])  #4-1

np.random.seed(1)

syn0 = 2 * np.random.random((3,4)) -1
syn1 = 2 * np.random.random((4,1)) -1

for i in range(60000):
    l0 = X  #4-3
    l1 = mysigmodfun(np.dot(l0, syn0))  #4-3 3-4=4-4
    l2 = mysigmodfun(np.dot(l1, syn1))  #4-4 4-1=4-1

    l2_error = y - l2  #4-1

    l2_delta = l2_error * mysigmodfun(l2, True)  #4-4 4-1=4-1

    l1_error = l2_delta.dot(syn1.T)  #4-1 1-4=4-4
    
    l1_delta = l1_error * mysigmodfun(l1, True)  #4-4 4-4=4-4


    syn0 += l0.T.dot(l1_delta)  #3-4 4-4=3-4
    syn1 += l1.T.dot(l2_delta)  #4-4 4-1=4-1

    #print(l2)
    #input()

print(l2)
def funtest(x):
    l1 = mysigmodfun(np.dot(x, syn0))
    print(mysigmodfun(np.dot(l1, syn1)))
    
funtest([1,1,1])

while True:
    x = [int(input('请输入0/1:\n')),int(input()),int(input())]
    funtest(x)
