#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *
import time
import threading

global text4show

def fun_tk():
    root=Tk()
    root.title('test')
    global text4show
    text4show = StringVar()
    text = text4show
    text.set('江飞강비.134971598719857198571984571980561985719056ㅛ1985619856198759817598175ㅐ샤1901759812365915719'+'\n'+'SSS')
    root.geometry('1000x610')
    root.resizable(width=True, height=True)
    l = Label(root, textvariable=text, wraplength=900, justify='left', anchor='nw', bg="white", font=("Arial", 32), width=1000, height=610)
    l.pack()
    mainloop()

t = threading.Thread(target=fun_tk)
t.start()

def print2UI(*text_list):
    all_text = ''
    for one_text in text_list:
        all_text += one_text
        all_text += '\n'
    global text4show
    text4show.set(all_text)
    
time.sleep(2)
print2UI('1', '2', '3')
