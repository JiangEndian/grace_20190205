#!/usr/bin/env python3

#导入线性代数工具库
import numpy as np

#一个sigmod函数,也可输入参数来返回层数
def mysigmodfun(x, deriv=False):
    if(deriv==True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

#输入集,一个矩阵，每次三个，共5组，神经元非常傻，只能一刀，分一个特征。。。不懂。。。无关的为1
X = np.array([ [1,1,1],
                [0,1,1],
                [0,1,1],
                [1,1,1],
                [1,1,1] ])

#输出集，一个矩阵，省空间，用反转（）
#一个神经元只能砍一刀，只能或0,或1，没有第三种了，只能一刀
y = np.array([[0,1,1,0,0]]).T

#设定随机序列种子，这样，依然平均分布，但每次生成的随机数序列都一样，便于观察，好习惯
np.random.seed(1)

#第一层权值，突触0,连接l0层与l1层,3-1
syn0 = 2 * np.random.random((3,1)) - 1

#开始训练
for i in range(10000):
    #前置训练，根据输入和权重，试着输出
    l0 = X  #5-3
    l1 = mysigmodfun(np.dot(l0, syn0))  #5-3 * 3-1 = 5-1

    #用标准结果y减去试着输出的结果l1，得到误差大小
    l1_error = y - l1  #5-1

    #误差项加权导数值(误差项 l1的导数值，设置为True即为求导)
    l1_delta = l1_error * mysigmodfun(l1, True)  #逐元素乘，同长度5-1

    #更新权重,权值更新量为输入值×误差项加权导数值
    syn0 += np.dot(l0.T, l1_delta)  #3-5 * 5-1 = 3-1

    #测试输出
    print(l1, '\n', '误差和其加权导数值:\n', l1_error, '\n\n', l1_delta, '\n', '更新后权重:\n', syn0)
    #print(l1)
    input()

print(l1)
