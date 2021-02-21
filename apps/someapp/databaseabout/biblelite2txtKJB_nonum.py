#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3
from newestMyPython3 import *

def opendb():#打开一个sqlite3数据库，并返回cursor
    conn = sqlite3.connect('bibles.sqlite')
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
    bookpyeon = ''
    conn, cursor = opendb()
    for book in runsql(cursor, 'select * from bible'):
        bookcontent = book[4]
        chapterno = book[2]
        verseno = book[3]
        if bookpyeon != str(book[1]):
            bookpyeon = str(book[1])
            bookall = bookall + '\n' + bookpyeon
        bookall = bookall + '\n' + str(bookcontent)
    write2file('KJBkoreanbible_nonum.txt', bookall)
finally:
    closedb(conn, cursor)
