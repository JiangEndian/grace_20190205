#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3
from newestMyPython3 import *

def opendb():#打开一个sqlite3数据库，并返回cursor
    #conn = sqlite3.connect(input('Input db name:'))
    conn = sqlite3.connect('ko.db')
    return conn, conn.cursor()

def runsql(cursor, sql):#接收一个cursor，并用此执行语句，返回values
    cursor.execute(sql)
    values = cursor.fetchall()
    return values

def closedb(conn, cursor):#关闭数据库
    cursor.close()
    conn.commit()
    conn.close()
   
try:
    bookall = ''
    conn, cursor = opendb()
    for classify in runsql(cursor, 'select * from classify'):
        #print(classify)
        #bookall += classify[3] + '\n' + classify[2] + '\n\n'
        bookall += str(classify[0]) + '=' +classify[3] + '=' + classify[2] + '\n'
        #print(classify[0], classify[2], classify[3])
        #input()
        for record in runsql(cursor, 'select * from records where cid=%s' % classify[0]):
            #print(record)
            bookall += str(record[0]) + '=' + record[3] + '=' + record[2] + '\n'
            #bookall += record[3] + '\n' + record[2] + '\n\n'
            #print(record[0], record[2], record[3])
            #input()
    write2file('koreanlite4bash.txt', bookall)
finally:
    closedb(conn, cursor)
