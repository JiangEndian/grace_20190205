#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

mps = 3300000*365*24*60*60 #一mps的3.3million光年到千米
print('mps=', mps)

def getV(r=0):
    return 4/3*3.14*r**3

r0 = 100*mps #设置初始半径
s0 = getV(r0) #得到初始空间体积
T0 = 10000*365*24*3600 #设置时间为10万年，不然看不到变化
print('T0=', T0)

t = np.arange(0, 1000, 1) #一维列表，从0到999的间隔1的1000份

def getX(r=0):
    return r / mps * 75

def getR1(r=0, t=1): #得到新一轮半径
    x = getX(r)
    #return r + x*t
    #return r + x*t*3600*24*3650 #每次十年的
    #return r + x*t*3600*24*36500 #每次百年的，共10000年
    #return r + x*t*3600*24*365000 #每次千年的，共100000年
    return r + x*t*3600*24*36500 #每次百年的，共100000年

listR = [] #半径的变化列表
listS = [] #空间的变化列表
listT = [] #剩余时间的变化列表

for i in t:
    r1 = getR1(r0)
    listR.append(r1)

    S = getV(r1)
    listS.append(S)

    TThis = S/300000**2
    TRemain = T0 - TThis
    listT.append(TRemain)

    r0=r1

plt.plot(t, listR)
plt.show()
plt.plot(t, listS)
plt.show()
plt.plot(t, listT)
plt.show()

