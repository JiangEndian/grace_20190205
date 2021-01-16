#!/usr/bin/env python3

import numpy as np

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

X = np.array([[0,0,1],  #4-3
            [0,1,1],
            [1,0,1],
            [1,1,1]])

y = np.array([[0],  #4-1
            [1],
            [1],
            [0]])

np.random.seed(1)

#随机初始化权重
syn0 = 2*np.random.random((3,4)) - 1 #第一层权值3个到4个
syn1 = 2*np.random.random((4,1)) - 1 #第二层权值4个到1个

for j in range(60000):

    # Feed forward through layers 0, 1, and 2
    l0 = X  #网络第1层，输入层
    l1 = nonlin(np.dot(l0,syn0))  #网络第2层，隐藏层
    l2 = nonlin(np.dot(l1,syn1))  #假定为最后一层

    print(l1, '\n', l2)
    input()

    # how much did we miss the target value?
    l2_error = y - l2  #神经网络预测时，'丢失'的数据

    if (j% 10000) == 0:  #每一万次训练，打印一次丢失的绝对值
        print("Error:" + str(np.mean(np.abs(l2_error))))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2,deriv=True) #置信度加权后的误差

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)  
    #l2_delta经syn1加权后的结果，从而能够得到中间层/隐藏层的误差

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1,deriv=True)
    #置信度加权后的l1层的误差

    syn1 += l1.T.dot(l2_delta) #用这个更新量来更新第2层权重
    syn0 += l0.T.dot(l1_delta) #用这个更新量来更新第1层权重

print(l2)
