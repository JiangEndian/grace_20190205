#!/usr/bin/env python3

import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = plt.axes(projection='3d')
#ax = fig.add_subplot(111, projection='3d')

#x = np.arange(0,10,1)
#y = np.arange(0,10,1)

#ax1.plot3D(x, y, z) #绘制3d线
#X, Y = np.meshgrid(x, y) #绘制3D面 #把y的每个值对应上所有的x，组成二维，10×10个点
#print(X, Y)

#z = np.array(range(100)).reshape((10,10))
#Z = z
#ax1.plot_surface(X, Y, Z)
#ax1.plot_surface(Y, X, Z)
#plt.show()

a = np.array(range(10*20*30*40)).reshape((10,20,30,40))

def gene3d(l):
    #print(a[l])
    return a[l]

a3 = gene3d(2)

def gene2d(k):
    #print(a3[k])
    return a3[k]
x = np.arange(0, 10, 1) 
y = np.arange(0, 10, 1)
z = np.arange(0, 10, 1)
v = np.arange(0, 10, 1)

XY = np.meshgrid(x, y) #200个X，因为10个点，在y轴上移动20下，Y也有200个
XZ = np.meshgrid(x, z)
XV = np.meshgrid(x, v)
YZ = np.meshgrid(y, z)
YV = np.meshgrid(y, v)
ZV = np.meshgrid(z, v)

def faceXY(face, high):
    xd = len(face[0])
    yd = len(face[0][0])
    Z = np.array(range(xd*yd)).reshape((xd, yd))
    for i in range(xd):
        for j in range(yd):
            Z[i,j] = high
    ax1.plot_surface(face[0], face[1], Z)
def faceXZ(face, high):
    xd = len(face[0])
    zd = len(face[0][0])
    Y = np.array(range(xd*zd)).reshape((xd, zd))
    for i in range(xd):
        for j in range(zd):
            Y[i,j] = high
    ax1.plot_surface(face[0], Y, face[1])
def faceYZ(face, high):
    yd = len(face[0])
    zd = len(face[0][0])
    X = np.array(range(yd*zd)).reshape((yd, zd))
    for i in range(yd):
        for j in range(zd):
            X[i,j] = high
    ax1.plot_surface(X, face[0], face[1])


faceXY(XY, 0)
faceXY(XY, 9)
faceXZ(XZ, 0)
faceXZ(XZ, 9)
faceYZ(YZ, 0)
faceYZ(YZ, 9)
#ax1.plot_surface(XY[0], XY[1], Z)


plt.show()
#print(a[4]) #这样直接第1个三维体，共7个三维体
