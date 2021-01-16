#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3
from newestMyPython3 import *

def opendb():#打开一个sqlite3数据库，并返回cursor
    conn = sqlite3.connect(input('Input db name:'))
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
    for book in runsql(cursor, 'select * from bible_korean_nkv'):
        bookcontent = book[1]
        bookno = book[2]
        chapterno = book[3]
        verseno = book[4]
        bookall = bookall + '\n' + '卷' + str(bookno) + ' ' + str(chapterno) + ':' + str(verseno) + ' ' + str(bookcontent)
    write2file('koreanbible.txt', bookall)
finally:
    closedb(conn, cursor)
