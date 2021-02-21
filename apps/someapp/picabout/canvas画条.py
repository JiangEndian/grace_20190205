#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *
from newestMyPython3 import *

#Font set
global ft
ft = getfont(fontsize=130)

#canvas的长和宽设定
global cx
cx = 1400
global cy
cy = 800

#Y轴的步子
global sy
sy = 40

#开始位置设定
global bx
bx = 50
global by
by = 50

#画面X轴和Y轴的缩放系数
global kx
kx = 1
global ky
ky = 1

bibletime = tk.Tk()
bibletime.title('Canvas画条')
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

#画标尺定位用的
cvs.create_line(2,5,1366,5,fill='black')#上线
for ix in [i*100 for i in range(14)]:
    cvs.create_line(ix,2,ix,10,fill='black')#上线标尺
    cvs.create_text(ix,20,text=str(ix),font=ft,fill='black')
cvs.create_line(1350,1,1350,800,fill='black')#右线
for iy in [i*50 for i in range(20)]:
    cvs.create_line(1350,iy,1340,iy,fill='black')
    cvs.create_text(1330,iy,text=str(iy),font=ft,fill='black')

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
    cvst.create_text((bx+x/2)*kx, (by+y/2)*ky, text=who, font=ft, fill='black')
    #cvst.pack()
    bx += x_move
    by += y_move
    #print(bx, by)

cr(cvs, '测试1', 200, 20, color1,200,20)
cr(cvs, '测试2', 20, 20, color2)

bibletime.mainloop()
