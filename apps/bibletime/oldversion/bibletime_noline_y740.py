#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *
from newestMyPython3 import *

#字体设置
global ft
ft = getfont(fontsize=100)
ft = getfont('Times',fontsize=100)
fto = getfont(fontsize=150)

#canvas的长和宽设定
global cx
cx = 7000
global cy
cy = 740
#纵屏截图，拼图，分割。。。

#Y轴的步子
global sy
sy = 25

#开始位置及时间AA,BC的设定
global bx
bx = 0
global by
by = sy 
global bAA
bAA = 1
global bBC
bBC = 3969

#画面X轴和Y轴的缩放系数
global kx
kx = 2
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
    cvst.create_rectangle(bx*kx, by*ky, (bx+age)*kx, (by+nsy)*ky, fill=color, outline=color)
    cvst.pack()

    #显示这些信息，个别调整一些X的位置，以便文字显示不重叠
    if True:
        cvst.create_text((bx+age/2)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    #if who in ['亚伯兰', '亚伯兰99', '以撒']:
    #    cvst.create_text((bx+age/2-200)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['雅各', '约瑟', '以色列在埃及']:
        cvst.create_text((bx+age/2-260)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['摩西', '旷野', '约书亚81?']:
        cvst.create_text((bx+age/2-130)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['27年元老死？']:
        cvst.create_text((bx+age/2-130)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['士师记？', '100年撒母耳？']:
        cvst.create_text((bx+age/2-180)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['扫罗40', '大卫']:
        cvst.create_text((bx+age/2-60)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['尼希米']:
        cvst.create_text((bx+age/2+200)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['希腊']:
        cvst.create_text((bx+age/2+150)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['托勒密王朝', '塞硫西王朝', '马喀比革命', '哈斯摩尼王朝']:
        cvst.create_text((bx+age/2+200)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['罗马', '以东人希律', '耶稣']:
        cvst.create_text((bx+age/2+50)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['巡抚', '耶路撒冷沦陷', '动乱与镇压']:
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

#1,2为主线，4为他强国，3为耶稣在世
color1 = '#ffff00'
color2 = '#00ffff'
color3 = '#00ff00'
color4 = '#ff00ff'
color5 = '#FFFFFF'#白色不显示

#对单词进行块分割
def asciicount(text):
    nums = 0
    for num in range(10):
        nums += text.count(str(num))
    for symbol in '{' '}' '[' ']' '<' '>' '/' '*' '-' '=' 'B' 'C' 'A' 'D' ' ' '.':
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
        if len(text) - asciicount(text)*1/2 >= charnums:
            #print(len(text), text)
            if word != strlist[-1]:
                alltext += text + '\n'
            else:
                alltext += text
            text = ''
    alltext += text
    return alltext

#import data4bibletime
#cr(cvs, '事件', 交任, 持续, 'color', '大事记')
rundata(cr, cvs)
bibletime.mainloop()
