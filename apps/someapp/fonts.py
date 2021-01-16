#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from tkinter import *

root = Tk()

for ft in ('Times', 'Helvetica', 'Courier', 'Symbol', 'Arial', '浪漫雅圆', ('Microsoft YaHei')):  
    Label(root, text='hello %s font\n你好 %s 字体' % (ft, ft), font=('-*-%s-*-*-*--*-240-*') % (ft)).grid()  
#X Font Descriptor格式：-*-family-weight-slant-*--*-size-*-*-*-*-charset  

root.mainloop()
