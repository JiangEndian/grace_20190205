#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *
from newestMyPython3 import *

#字体设置
global ft
ft = getfont(fontsize=120)
#ft = getfont('Times', 110)

#canvas的长和宽设定
global cx
cx = 7000
global cy
cy = 1750
#纵屏截图，拼图，分割。。。

#Y轴的步子
global sy
sy = 34

#开始位置及时间AA,BC的设定
global bx
bx = 0 - 3900 
global by
by = sy 
global bAA
bAA = 1
global bBC
bBC = 3969

#画面X轴和Y轴的缩放系数
global kx
kx = 1
global ky
ky = 1

#canvase开始画画,没有明确纪年的，推算的时间的。如族长时代们～
def cr(cvst, who, whenson, age, color, other='空白'):
    global ft
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
    if bAA == 1:#刚开始时画标尺
        cvst.create_line(1,(sy/2)*ky,cx*kx,(sy/2)*ky,fill='black')#上线
        cvst.create_line(1,(cy-sy/2)*ky,cx*kx,(cy-sy/2)*ky,fill='black')#下线
        for ix in [i*100 for i in range(int(cx/100))]:
            cvst.create_line(ix*kx,(sy/2)*ky,ix*kx,sy*0.7*ky,fill='black')#上线标尺
            cvst.create_text(ix*kx,sy*0.95*ky,text='AA' + str(ix),font=ft,fill='black')
            if ix<3970:
                cvst.create_text(ix*kx,sy*ky+sy/4,text='BC'+str(3970-ix),font=ft,fill='black')
            elif ix>3970:
                cvst.create_text(ix*kx,sy*ky+sy/4,text='AD'+str(ix-3969),font=ft,fill='black')
            cvst.create_line(ix*kx,(cy-sy/2)*ky,ix*kx,(cy-sy*0.7)*ky,fill='black')#下线标尺
            cvst.create_text(ix*kx,(cy-sy*0.9)*ky,text='AA' + str(ix),font=ft,fill='black')
            if ix<3970:
                cvst.create_text(ix*kx,(cy-sy)*ky-sy/4,text='BC'+str(3970-ix),font=ft,fill='black')
            elif ix>3970:
                cvst.create_text(ix*kx,(cy-sy)*ky-sy/4,text='AD'+str(ix-3969),font=ft,fill='black')
        by = sy/2 + by#画完标尺，下移图画

    #AD1年为AA3970年，那么，BC1年，为AA3969年（AA:AfterAdam)
    if whenson == 0:
        msgt1 = 'AA%d-AA%d年  事件:%s  持续:%d年' % (bAA,bAA+age, who, age)
    else:
        msgt1 = 'AA%d-AA%d年  事件:%s  交任:%d年  持续:%d年' % (bAA,bAA+age, who, whenson, age)
    if bBC > bAD() and (bBC-age) > bAD(age):#生死都在公元前
        if len(other) < 16:
            msgt2 = 'BC%d-BC%d年 %s' % (bBC,bBC-age, other)
        else:
            msgt2 = 'BC%d-BC%d年\n%s' % (bBC,bBC-age, other)
    elif bBC < bAD():#生于公元后
        if len(other) < 16:
            msgt2 = 'AD%d-AD%d年 %s' % (bAD(),bAD(age), other)
        else:
            msgt2 = 'AD%d-AD%d年\n%s' % (bAD(),bAD(age), other)
    else:#生于公元前，但死于公元后
        if len(other) < 16:
            msgt2 = 'BC%d-AD%d年 %s' % (bBC,bAD(age), other)
        else:
            msgt2 = 'BC%d-AD%d年\n%s' % (bBC,bAD(age), other)
    msgt = msgt1 + '  ' + msgt2

    #满足条件，隐藏一些条的文字
    if age == 480 or age == 430:
        msgt = ''

    #计算新的高度nsy
    nsy = (msgt.count('\n')+1) * sy / 2 

    if by + nsy > cy - sy*1.5:#如果y轴画过了，重新回到sy*1.5开始画
        by = sy * 1.5
    #画矩形，开始位置，长宽，填充,然后在末处画一条纵线/纵线提前画了
    #cvst.create_line((bx+age)*kx, 0, (bx+age)*kx, cy, fill=color)
    cvst.create_rectangle(bx*kx, by*ky, (bx+age)*kx, (by+nsy)*ky, fill=color)
    cvst.pack()

    #显示这些信息，个别调整一些X的位置，以便文字显示不重叠
    if bAA < 1058:#这个到挪亚时
        cvst.create_text((bx+300)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif bAA < 2444:#这个调到摩西时
        cvst.create_text((bx+age/2-250)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif bAA < 2595:#这个调到约书亚死长老在时
        cvst.create_text((bx+age/2-150)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif bAA < 2929:#这个调到扫罗时
        cvst.create_text((bx+age/2-145)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif bAA < 2960:#大卫时
        cvst.create_text((bx+age/2-40)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif bAA < 3513:#到以斯拉
        cvst.create_text((bx+age/2)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif bAA < 4105:#到动乱与镇压
        cvst.create_text((bx+age/2+200)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    else:
        cvst.create_text((bx+age/2)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')

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

color1 = '#FFFFaa'
color2 = 'yellow'
color3 = '#00FF00'#闪绿色
color4 = '#00FFFF'#青色
color5 = '#FFFFFF'#白色不显示

#对单词进行块分割
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
            if word != strlist[-1]:
                alltext += text + '\n'
            else:
                alltext += text
            text = ''
    alltext += text
    return alltext

#import data4bibletime
rundata(cr, cvs)
bibletime.mainloop()
