#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3


def opendb():#打开一个sqlite3数据库，并返回cursor
    conn = sqlite3.connect(input('Input clear db name:'))
    return conn, conn.cursor()

def closedb(conn, cursor):#关闭数据库
    cursor.close()
    conn.commit()
    conn.close()

try:
    conn, cursor = opendb()
    tables = input('Input tables to clear:').split()
    for table in tables:
        cursor.execute('delete from %s' % table)
        print(cursor.execute('select * from %s' % table).fetchall())
finally:
    closedb(conn, cursor)
