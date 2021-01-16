#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *

#canvas的长和宽设定
global cx
cx = 1400
global cy
cy = 800

#Y轴的步子
global sy
sy = 40

#开始位置及时间AA,BC的设定
global bx
bx = 10
global by
by = 300
global bAA
bAA = 5986
global bBC
bBC = -2016 

#画面X轴和Y轴的缩放系数
global kx
kx = 0.9
global ky
ky = 0.9

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

#canvas, 显示信息， 长，高，颜色， 下次画的原点位移x，y
def cr(cvst, who, x, y, color, x_move=0, y_move=0):
    global cy
    global bx
    global by
    global bAA
    global bBC
    global kx
    global ky
    cvst.create_rectangle(bx*kx, by*ky, (bx+x)*kx, (by+y)*ky, fill=color)
    cvst.create_text((bx+x/2)*kx, (by+y/2)*ky, text=who, fill='black')
    #cvst.pack()
    bx += x_move
    by += y_move
    #print(bx, by)

#cr(cvs, '测试1', 20, 20, color1,20,20)
#cr(cvs, '测试2', 20, 20, color2)
cr(cvs, '但', 100, 250, color1, 100, 0)
cr(cvs, '亚设', 100, 250, color2, 100, 0)
cr(cvs, '拿弗他利', 100, 250, color1, 100, 0)
cr(cvs, '玛拿西', 100, 250, color2, 100, 0)
cr(cvs, '以法莲', 100, 250, color1, 100, 0)
cr(cvs, '流便', 100, 250, color2, 100, 0)
cr(cvs, '犹大', 100, 250, color1, 100, 0)
cr(cvs, '祭司', 100, 250, color2, 100, 0)
cr(cvs, '利未', 100, 250, color1, 100, 0)
cr(cvs, '俗用', 50, 250, color2, -200, -100)
cr(cvs, '王', 250, 100, color1, 0, 350)
cr(cvs, '王', 250, 100, color2, 250, -250)
cr(cvs, '便雅闵', 100, 250, color1, 100, 0)
cr(cvs, '西缅', 100, 250, color2, 100, 0)
cr(cvs, '以萨迦', 100, 250, color1, 100, 0)
cr(cvs, '西布伦', 100, 250, color2, 100, 0)
cr(cvs, '迦得', 100, 250, color1, 100, 0)

bibletime.mainloop()
