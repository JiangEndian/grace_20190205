#!/usr/bin/env python3

import tkinter as tk 
from MyPython3 import *

localFiles = ['/home/ed/temp4submit', 
            '/home/ed/syncFiles2RemoteFiles.py']

remoteLocation = 'ed@47.244.31.34:/home/ed/grace_20190205/apps/statics/files/'

scpCmds = []
for localFile in localFiles:
    scpCmds.append(f'scp {localFile} {remoteLocation}')
print(scpCmds)

def syncAll():
    for scpCmd in scpCmds:
        print(scpCmd)
        print(runsyscmd(scpCmd))

def openUrlSubmit(url='http://47.244.31.34:3927/submitToGithub'):
    runsyscmd(f'google-chrome {url}')

window = tk.Tk()
window.title(f'同步至{remoteLocation}')
window.geometry('600x400')

#tk.的组件：BitmapImage, Button, Canvas, Checkbutton, Entry, Frame, Label, 
#LabelFrame, Listbox, Menu, Menubutton, Message, OptionMenu, PanedWindow, 
#PhotoImage, Radiobutton, Scale, Scrollbar, Spinbox, Text, Toplevel窗口

tk.Label(window, text='').pack()

#for scpCmd in scpCmds:
for localFile in localFiles:
    #tk.Label(window, text=scpCmd).pack()
    tk.Label(window, text=localFile).pack()

tk.Label(window, text='').pack()

tk.Button(window, text='sync', width=20, height=2, command=syncAll).pack()
tk.Label(window, text='').pack()
tk.Button(window, text='submit', width=20, height=2, command=openUrlSubmit).pack()

window.mainloop()

