#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3

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
    conn, cursor = opendb()
    while input('Input exit to exit.n to conntinue:') != 'exit':
        if input('Input p to print sql:') == 'p':
            print('''建:create table 表 (列 类型(大小) primary key, 列 类型(大小), 列...) varchar类型足足
增:insert into 表 (列, 列) values (值, 值)
删:delete from 表,删表中所有值
删:delete from 表 where 列=值
删:drop table 表,删表
改:update 表 set 列=新值 (where 列=值)
查:select * from 表，或加 where 列=值''') 
        values = runsql(cursor, input('Please input SQL:'))
        print(values)

finally:
    closedb(conn, cursor)
