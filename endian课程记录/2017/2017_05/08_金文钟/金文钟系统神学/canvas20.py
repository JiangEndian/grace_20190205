#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *

#canvas的长和宽设定
global cx
cx = 1200
global cy
cy = 700

#Y轴的步子
global sy
sy = 40

#开始位置及时间AA,BC的设定
global bx
bx = 10
global by
by = sy
global bAA
bAA = 5986
global bBC
bBC = -2016 

#画面X轴和Y轴的缩放系数
global kx
kx = 20
global ky
ky = 1

#canvase开始画画,没有明确纪年的，推算的时间的。如族长时代们～
def cr(cvst, who, whenson, age, color, other='空白'):
    global cy
    global bx
    global by
    global bAA
    global bBC
    global kx
    global ky
    def bAD(after=0):#通过BC计算AD
        global bBC
        return 1-(bBC-after)
    if by > 600:#如果y轴画过600了，重新回到sy*1.5开始画
        by = sy * 1.5
    #画矩形，开始位置，长宽，填充,然后在末处画一条纵线
    cvst.create_rectangle(bx*kx, by*ky, (bx+age)*kx, (by+sy)*ky, fill=color)
    cvst.pack()
    cvst.create_line((bx+age)*kx, 0, (bx+age)*kx, cy, fill=color)

    #AD1年为AA3970年，那么，BC1年，为AA3969年（AA:AfterAdam)
    if True:
        msgt1 = '计划:%s  持续:%d年' % (who, age)
    else:
        msgt1 = 'AA%d-AA%d年  事件:%s  交任:%d年  持续:%d年' % (bAA,bAA+age, who, whenson, age)
    if bBC > bAD() and bBC > bAD(age):#生死都在公元前
        msgt2 = 'BC%d-BC%d年  大事记:%s' % (bBC,bBC-age, other)
    elif bBC < bAD():#生于公元后
        msgt2 = 'AD%d-AD%d年  事记:%s' % (bAD(),bAD(age), other)
    else:#生于公元前，但死于公元后
        msgt2 = 'BC%d-AD%d年  大事记:%s' % (bBC,bAD(age), other)
    msgt = msgt1 + '\n' + msgt2
    #显示这些信息
    cvst.create_text((bx+age/2)*kx, (by+sy/2)*ky, text=msgt, fill='black')

    #开始位置和时间前进喽
    bx += whenson
    by += sy
    bAA += whenson
    bBC -= whenson

bibletime = tk.Tk()
bibletime.title('BibleTime...')
#一个Y轴滚动条
scrollbary = Scrollbar(bibletime)
scrollbary.set(0.5,1)
scrollbary.pack(side=RIGHT)
#一个X轴滚动条
scrollbarx = Scrollbar(bibletime, orient=HORIZONTAL)
scrollbarx.set(0.5,1)
scrollbarx.pack()
#把这个东西设置好同时绑定到滚动条上
#cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)#加上set后，win不好使
cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=scrollbarx, yscrollcommand=scrollbary)#不加set,mint好使...
cvs.pack()
#对滚动条进行配置，滚动时触发什么
scrollbarx.config(command=cvs.xview)
scrollbary.config(command=cvs.yview)

color1 = 'pink'
color2 = 'yellow'
color3 = '#00FF00'#闪绿色
color4 = '#00FFFF'#青色

#cr(cvs, '事件', 交任, 持续, 'color', '大事记')
cr(cvs, '圣经40遍', 2, 2, color1, '把圣经读40遍')
cr(cvs, '系统神学', 3, 3, color4, '学习系统神学')

#插入不影响：插入的交付为0，例如：
#cr(cvs, '插入不影响', 0, *, color...
#或者上条记录交付=新交付+插入交付，例如：cr(cvs, '上条', 40, *, color...
#cr(cvs, '上条', 19/20/21, *, color...
#cr(cvs, '插入', 21/20/19, *, color...
#总原则就是：交付总数不能变，原来总多少，后来也总多少。。。

bibletime.mainloop()
