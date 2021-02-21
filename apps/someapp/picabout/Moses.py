#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *
from newestMyPython3 import *

#字体设置
global ft
ft = getfont(fontsize=120)
#ft = getfont('Times', 100)

#canvas的长和宽设定
global cx
cx = 7000
global cy
cy = 1000

#Y轴的步子
global sy
sy = 40

#开始位置及时间AA,BC的设定
global bx
bx = 2
global by
by = sy
global bAA
bAA = 1
global bBC
bBC = 3969

#画面X轴和Y轴的缩放系数
global kx
kx = 10
global ky
ky = 5

global upnorth
upnorth = True


#对单词进行块分割,第一个是计算占用半块的非汉字数
def asciicount(text):
    nums = 0 
    for num in range(10):
        nums += text.count(str(num))
    for symbol in '{' '}' '[' ']' '<' '>' '/' '*' '-' '=' 'B' 'C' 'A' 'D' ' ':
        nums += text.count(symbol)
        #    print(nums)
    return nums                 
#asciicount('江飞0123456789 {} [] ')
def strdef(strlist, charnums=33):
    text = ''
    alltext = ''
    spacenum = 0 
    for word in strlist:
        text += word + ' ' 
        if len(text) - asciicount(text)/2 >= charnums:
            #print(len(text), text)
            alltext += text + '\n'
            text = ''
    alltext += text
    return alltext
                                                                                                            
#canvase开始画画,没有明确纪年的，推算的时间的。如族长时代们～
def cr(cvst, who, whenson, age, color, other=''):
    global ft
    global cy
    global bx
    global by
    global bAA
    global bBC
    global kx
    global ky
    global upnorth

    msgt = who + '\n' + other
    #计算新的高度nsy
    nsy = (msgt.count('\n')+1) * sy / 2 

    cvst.create_rectangle(bx*kx, by*ky, (bx+age)*kx, (by+nsy)*ky, fill=color, outline=color)
    #显示这些信息
    cvst.create_text((bx+age/2)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    cvst.pack()
    #开始位置和时间前进喽
    bx += whenson
    by += nsy
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
color5 = '#FFFFFF'#白色不显示

#cr(cvs, '事件', 交任, 持续, 'color', '大事记')

#北国诸王
temp = '出生 成长'.split()
cr(cvs, '埃及40年', 40, 40, color1, strdef(temp, 33))

temp = '旷野 放羊'.split()
cr(cvs, '旷野40年', 40, 40, color2, strdef(temp, 33))

temp = '旷野 放以色列'.split()
cr(cvs, '旷野40年', 40, 40, color1, strdef(temp, 33))

bibletime.mainloop()
