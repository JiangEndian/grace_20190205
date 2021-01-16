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
   
conn = sqlite3.connect('bible_chinese_sim.sqlite')
cursor = conn.cursor()
dictbible = {1:'创世记', 2:'出埃及记', 3:'利未记', 4:'民数记', 5:'申命记', 6:'约书亚记', 7:'士师记', 8:'路得记', 9:'撒母耳记上', 10:'撒母耳记下', 11:'列王纪上', 12:'列王纪下', 13:'历代志上', 14:'历代志下', 15:'以斯拉记', 16:'尼希米记', 17:'以斯帖记', 18:'约伯记', 19:'诗篇', 20:'箴言', 21:'传道书', 22:'雅歌', 23:'以赛亚书', 24:'耶利米书', 25:'耶利米哀歌', 26:'以西结书', 27:'但以理书', 28:'何西阿书', 29:'约珥书', 30:'阿摩司书', 31:'俄巴底亚书', 32:'约拿书', 33:'弥迦书', 34:'那鸿书', 35:'哈巴谷书', 36:'西番雅书', 37:'哈该书', 38:'撒迦利亚书', 39:'玛拉基书', 40:'马太福音', 41:'马可福音', 42:'路加福音', 43:'约翰福音', 44:'使徒行传', 45:'罗马书', 46:'哥林多前书', 47:'哥林多后书', 48:'加拉太书', 49:'以弗所书', 50:'腓立比书', 51:'歌罗西书', 52:'帖撒罗尼迦前书', 53:'帖撒罗尼迦后书', 54:'提摩太前书', 55:'提摩太后书', 56:'提多书', 57:'腓利门书', 58:'希伯来书', 59:'雅各书', 60:'彼得前书', 61:'彼得后书', 62:'约翰一书', 63:'约翰二书', 64:'约翰三书', 65:'犹大书', 66:'启示录'}

bd = {} #反转上字典的KV。。。
for k, v in dictbible.items():
    bd[v] = k
#print(bd)

#while False:
if True:
    try:
#        one = input('请输入卷数:')
        one = input('请输入卷名/卷数：')
        if len(one) > 2:    #如果长度大于2,是卷名，用其为K查找V的数
            one = bd[one]
        else:               #输入的是卷数，则，直接int即可，其实这个可以不要也行，但，我就是笨。。。不优化。。。
            one = int(one)

        book_no = int(one)  #再次int与上一个重复了。。
        two = input('请输入章数:')
        chapter_no = int(two)
    except:
        print(one)
        print(two)
        book_no = 19
        chapter_no = 23
    
    bookall = '卷' + str(book_no) + dictbible[book_no]
    books = cursor.execute('select * from bible_chinese_sim where c4book_no=? and c5chapter_no=?', (book_no, chapter_no))

    for book in books:
        bookcontent = book[1]
        bookno = book[2]
        chapterno = book[3]
        verseno = book[4]
        bookall = bookall + '\n' + str(chapterno) + ':' + str(verseno) + ' ' + str(bookcontent)
    #print(bookall)
    write2file('cnbtemp', bookall)

closedb(conn, cursor)
