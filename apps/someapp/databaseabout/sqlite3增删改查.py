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
    if input('Input showtable to showtable') == 'showtable':
        while True:
            sql = 'select * from %s' % input('Input table name:')
            print(runsql(cursor, sql))
    while input('Input exit to exit.n to conntinue:') != 'exit':
        if input('Input p to print sql:') == 'p':
            print('''
建:create table 表 (列 类型(大小) primary key, 列 类型(大小), 列...) varchar类型足足
    integer primary key可自动增长。integer类型可不设大小.
增:insert into 表 (列1, 列2) values (值, 值)
删:delete from 表,删表中所有值
	delete from 表 where 列=值     cursor.execute('***where 列1=? and 列2=?', ('值1', '值2'))cursor执行带参sql
	drop table 表,删表
改:update 表 set 列1=新值1, 列2=新值2 (where 列=值)
查:select 列 from 表 [where 列=值] [where 列 in ('val1', 'val2', 'val3')] [where 列 between val1 and val2]
	select *为整行。查到结果为[]，一行一个()
	select name from syscolumns where id=object_id('TableName')''') 
        values = runsql(cursor, input('Please input SQL:'))
        print(values)

finally:
    closedb(conn, cursor)
