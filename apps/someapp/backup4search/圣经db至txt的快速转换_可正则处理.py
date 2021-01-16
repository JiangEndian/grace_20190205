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
    
dictbible = {1:'创世纪', 2:'出埃及记', 3:'利未记', 4:'民数记', 5:'申命记', 6:'约书亚记', 7:'士师记', 8:'路得记', 9:'撒母耳记上', 10:'撒母耳记下', 11:'列王纪上', 12:'列王纪下', 13:'历代志上', 14:'历代志下', 15:'以斯拉记', 16:'尼希米记', 17:'以斯帖记', 18:'约伯记', 19:'诗篇', 20:'箴言', 21:'传道书', 22:'雅歌', 23:'以赛亚书', 24:'耶利米书', 25:'耶利米哀歌', 26:'以西结书', 27:'但以理书', 28:'何西阿书', 29:'约珥书', 30:'阿摩司书', 31:'俄巴底亚书', 32:'约拿书', 33:'弥迦书', 34:'那鸿书', 35:'哈巴谷书', 36:'西番雅书', 37:'哈该书', 38:'撒迦利亚书', 39:'玛拉基书', 40:'马太福音', 41:'马可福音', 42:'路加福音', 43:'约翰福音', 44:'使徒行传', 45:'罗马书', 46:'哥林多前书', 47:'哥林多后书', 48:'加拉太书', 49:'以弗所书', 50:'腓立比书', 51:'歌罗西书', 52:'帖撒罗尼迦前书', 53:'帖撒罗尼迦后书', 54:'提摩太前书', 55:'提摩太后书', 56:'提多书', 57:'腓利门书', 58:'希伯来书', 59:'雅各书', 60:'彼得前书', 61:'彼得后书', 62:'约翰一书', 63:'约翰二书', 64:'约翰三书', 65:'犹大书', 66:'启示录'}


def get_num_five(one_num):
    five_num = ''
    for i in one_num:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            five_num = five_num + i
    for i in range(5-len(five_num)):
        five_num = '0' + five_num
    return five_num
   
try:
    bookall = ''
    bookall_list = []

    conn = sqlite3.connect('和合本.db')
    cursor = conn.cursor()

    connc = sqlite3.connect('Tanakh+.db')
    cursorc = connc.cursor()
    names_of_hebrew = runsql(cursorc, 'select * from Books')

    connh = sqlite3.connect('cuvs_sn.wd')
    cursorh = connh.cursor()
    #print(names_of_hebrew)
    #exit()
    #for (book, bookc) in zip(runsql(cursor, 'select * from bible_korean_nkv'), runsql(cursorc, 'select * from bible_chinese_sim')):
    for book in runsql(cursorc, 'select * from Bible'):
        bookcontent = book[4] #内容

        ####提取内容与索引####
        import re
        text = ''.join(re.split(r'<[qQ]>', bookcontent))
        hebrew_and_number = text
        mean_search = re.split(r'>.*?<', text)
        #print(mean_search) 
        mean_num_list = []
        for one_num in mean_search:
            num_five = get_num_five(one_num)
            mean_num_list.append(num_five)
        bookcontent = ''.join(re.split(r'<.*?>', text))
        ####提取内容与索引####

        bookno = book[1] #创世纪为1,这样的序号
        chapterno = book[2] #章
        verseno = book[3] #节
        bookall =  names_of_hebrew[bookno-1][1] + '(' + names_of_hebrew[bookno-1][2] + ')' + ' ' + str(chapterno) + ':' + str(verseno) + ' ' + str(bookcontent)
        bookall_list.append(bookall)
        
        kjb_title = dictbible[bookno]
        cursor.execute('select * from Bible where Book=? and Chapter=? and Verse=?', (bookno, chapterno, verseno))
        bookc = cursor.fetchall()
        if bookc:
            bookccontent = kjb_title +' ' + str(bookc[0][2]) + ':' + str(bookc[0][3]) + ' ' + bookc[0][4] 
            bookall_list.append(bookccontent)
            #bookall = bookall + '\n' + bookccontent + '\n'
        else:
            bookall_list.append('这节中文没有。。。')
            #bookall = bookall + '\n' + '这节中文没有。。。' + '\n'
        for mean_num in mean_num_list:
            mean = cursorh.execute('select * from t_dict_hebrew_sn where strong_number=?', (mean_num, )).fetchall()
            if mean:
                if mean[0][2] == None:
                    mean = '________________________________\n'  + mean[0][0] + '\n___________' + mean[0][1] + '\n' + hebrew_and_number
                elif mean[0][1] == None:
                    mean = '________________________________\n'  + mean[0][0] + '\n___________' + mean[0][2] + '\n' + hebrew_and_number
                else:
                    mean = '________________________________\n' + mean[0][2] + '\n___________\n' + mean[0][1]
                mean = mean.replace('\r', '\n')
                mean = mean.replace('\n\n', '\n')
                mean = mean.replace('\n\n', '\n')
                mean = mean.replace('\n\n', '\n')
                mean = mean.replace('\n\n', '\n')
                bookall_list.append(mean)
            else:
                print('%s没有意思解释。' % mean_num)
        bookall_list.append('\n\n\n\n')
        
        #print('\n'.join(bookall_list))
        #input()
    write2file('hebrew_chinese_dict_bible.txt', '\n'.join(bookall_list))
finally:
    closedb(conn, cursor)
    closedb(connc, cursorc)
