#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'Endian personal Python3 module'

from datetime import datetime,timedelta #使用date相关
from tkinter import *                   #使用GUI
import tkinter.messagebox as messagebox #使用GUI
import os
import pickle       #使用pickle持久化对象
import sqlite3      #使用sqlite3要导入的

# 获取当前时间的年月日或秒数
def getnowtime( a='ymd' ):
    now = datetime.now()
    today = now.strftime('%Y%m%d')
    alls = now.timestamp()
    if a == 'ymd':
        return today
    else:
        return alls

# 获取几天后的年月日
def getdaystime( day ):
    now = datetime.now()
    now = now + timedelta(days=day)
    return now.strftime('%Y%m%d')

# 居中放置窗口，窗口，宽，高
def setwcenter(root, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)  
    root.geometry(size)
#test = Tk()

###一个窗口类，包含的组件们～tab为tab，不是空格，这个类。不如Tk()来的方便简单。。。###
class Myframe(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createwidgets()
	def createwidgets(self):
		#显示文本的
		self.helloLabel = Label(self, text='Hello,world')
		self.helloLabel.pack()
		#一个按钮的
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()
		#一个输入的框框
		self.nameInput = Entry(self)
		self.nameInput.pack()
		#一个按钮
		self.alertButton = Button(self, text='Hello', command=self.hello)
		self.alertButton.pack()
		#一个单选框，一个复选框
		self.radiobutton = Radiobutton(self, command=self.printhello)
		self.radiobutton.pack()
		self.checkbutton = Checkbutton(self, command=self.printhello)
		self.checkbutton.pack()
		
	def hello(self):
		name = self.nameInput.get() or 'World'
		messagebox.showinfo('EndianMessage', 'Hello, %s' % name)
		
	def printhello(self):
		messagebox.showinfo('TT', 'HelloHello')
		#messagebox.showinfo('EndianMessage', 'Hello, World.')
#####################################################

#文件直接读取，写入(text)
def write2file(fname, stext):
    with open(fname, 'w') as f:
        f.write(stext)
def readffile(fname):
    with open(fname, 'r') as f:
        return f.read()

#建立及删除文件夹,针对当前目录下
def newdir(dirname):
    os.mkdir(os.path.join(os.path.abspath('.'), dirname))
def deldir(dirname):
    os.rmdir(os.path.join(os.path.abspath('.'), dirname))

#pickle来进行对象序列化（持久化对象)
def dump2file(fname, obj):
    with open(fname, 'wb') as f:
        pickle.dump(obj, f)
def loadffile(fname):
    with open(fname, 'rb') as f:
        return pickle.load(f)

#打开一个sqlite3数据库，并返回连接conn和游标cursor
def opendb():
    conn = sqlite3.connect(input('Input db name:'))
    return conn, conn.cursor()
#接收一个cursor，并用此执行sql语句，返回values...
def runsql(cursor, sql):
    cursor.execute(sql)
    return cursor.fetchall()
#关闭连接和游标
def closedb(conn, cursor):
    cursor.close()
    conn.commit()
    conn.close()

#--------------------------时间相关的方法------------------------------------------------------
#getnowtime('ymd')--得到yyyymmdd或1344151512, getdaystime(day)--得到几天后的yyyymmdd

#--------------------------GUI相关的方法-------------------------------------------------------
#setwcenter(root,width,height)--使root窗口居中, Myframe()--类。。。

#--------------------------文本与对象和文件互相转化的方法--------------------------------------
#write2file(fname,stext), readffile(fname)--从文件读取文本, newdir(dirname), deldir(dirname).
#dump2file(fname,obj)--把obj持久化到文件, loadffile(fname)--从文件读取到obj

#--------------------------数据库操作的相关方法------------------------------------------------
#opendb()--得到conn和cursor, runsql(cursor, sql)--得到values, closedb(conn,cursor)

if __name__ == '__main__':
    pass
    #测试命令行方法(已测试的，就删除掉了)(保留的，都是测试过的.)
    #测试GUI方法
