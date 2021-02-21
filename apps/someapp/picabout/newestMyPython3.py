#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'Endian personal Python3 module'

from datetime import datetime,timedelta #使用date相关
from tkinter import *                   #使用GUI
import tkinter.messagebox as messagebox #使用GUI
import os
import pickle       #使用pickle持久化对象
import sqlite3      #使用sqlite3要导入的
import numpy as np
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
    conn = sqlite3.connect(input('Please input dbfile:'))
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

#获取字体
def getfont(fontdescriptor=('Microsoft YaHei'), fontsize=240):
    return '-*-%s-*-*-*--*-%d-*' % (fontdescriptor, fontsize)
   
#运行系统命令
def runsyscmd(cmd):
    output = os.popen(cmd)
    print(output.read())
    output.close()

#返回圣经卷数与卷名dict
def getbiblename():
	return {1:'创世记', 2:'出埃及记', 3:'利未记', 4:'民数记', 5:'申命记', 6:'约书亚记', 7:'士师记', 8:'路得记', 9:'撒母耳记上', 10:'撒母耳记下', 11:'列王纪上', 12:'列王纪下', 13:'历代志上', 14:'历代志下', 15:'以斯拉记', 16:'尼希米记', 17:'以斯帖记', 18:'约伯记', 19:'诗篇', 20:'箴言', 21:'传道书', 22:'雅歌', 23:'以赛亚书', 24:'耶利米书', 25:'耶利米哀歌', 26:'以西结书', 27:'但以理书', 28:'何西阿书', 29:'约珥书', 30:'阿摩司书', 31:'俄巴底亚书', 32:'约拿书', 33:'弥迦书', 34:'那鸿书', 35:'哈巴谷书', 36:'西番雅书', 37:'哈该书', 38:'撒迦利亚书', 39:'玛拉基书', 40:'马太福音', 41:'马可福音', 42:'路加福音', 43:'约翰福音', 44:'使徒行传', 45:'罗马书', 46:'哥林多前书', 47:'哥林多后书', 48:'加拉太书', 49:'以弗所书', 50:'腓立比书', 51:'歌罗西书', 52:'帖撒罗尼迦前书', 53:'帖撒罗尼迦后书', 54:'提摩太前书', 55:'提摩太后书', 56:'提多书', 57:'腓利门书', 58:'希伯来书', 59:'雅各书', 60:'彼得前书', 61:'彼得后书', 62:'约翰一书', 63:'约翰二书', 64:'约翰三书', 65:'犹大书', 66:'启示录'}
	
#sigmod方法,神经网络相关
def ed_sigmod(x):
    return 1 / (1 + np.exp(-x))
def ed_deriv(x):
    return x * (1 - x)
#生成wij连接权重(随机)
def ed_createwij(xi,xj):
    return 2*np.random.random((xi,xj)) - 1
#步骤为1输入矩阵乘权重再sigmod得到输出（或下层输入），2标准减输出得到误差，3加权(*)输出的导数值，得到误差加权导数值，4用输入转和它矩阵乘得到权值更新量，5更新
#多层的中间层错误由后一层的误差加权导数值矩阵乘二者的连接权重转，其他同样

if __name__ == '__main__':
    pass
    #测试命令行方法
    X = np.array([ [0,0,1],
                    [0,1,1],
                    [1,0,1],
                    [1,1,1],
                    [0,1,0],
                    [1,1,0],
                    [0,0,0],
                    [1,0,0] ])
    y = np.array([ [0,1,1,1,0,0,0,0] ]).T  #或再和最后与
    
    syn01 = ed_createwij(3,4)  #w01
    syn12 = ed_createwij(4,1)  #w12

    for i in range(10000):
        l0 = X  #输入
        l1 = ed_sigmod(np.dot(l0,syn01))  #l0*syn01再sigmod得到l1
        l2 = ed_sigmod(np.dot(l1,syn12))  #l1*syn12再sigmod得到l2

        l2_error = y - l2                 #y-l2得到l2的误差
        l2_delta = l2_error*ed_deriv(l2)  #l2的误差乘l2的导数得到误差加权导数值

        l1_error = l2_delta.dot(syn12.T)  #l2的误差加权导数值矩阵乘syn12.T得到l1的误差
        l1_delta = l1_error*ed_deriv(l1)  #l1的误差乘l1的导数得到误差加权导数值

        syn01 += l0.T.dot(l1_delta)       #l0.T矩阵乘l1的误差加权导数值得到syn01的更新量
        syn12 += l1.T.dot(l2_delta)       #l1.T矩阵乘l2的误差加权导数值得到syn12的更新量
    print(l2)
    #测试GUI方法
