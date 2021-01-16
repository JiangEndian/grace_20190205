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

dictbibleE = {1:'Genesis', 2:'Exodus', 3:'Leviticus', 4:'Numbers', 5:'Deuteronomy', 6:'Joshua', 7:'Judges', 8:'Ruth', 9:'Samuel 1', 10:'Samuel 2', 11:'Kings 1', 12:'Kings 2', 13:'Chronicles 1', 14:'Chronicles 2', 15:'Ezra', 16:'Nehemiah', 17:'Esther', 18:'Job', 19:'Psalms', 20:'Proverbs', 21:'Ecclesiastes', 22:'Song of Songs', 23:'Isaiah', 24:'Jeremiah', 25:'Lamentations', 26:'Ezekiel', 27:'Daniel', 28:'Hosea', 29:'Joel', 30:'Amos', 31:'Obadiah', 32:'Jonah', 33:'Micah', 34:'Nahum', 35:'Habakkuk', 36:'Zephaniah', 37:'Haggai', 38:'Zechariah', 39:'Malachi', 40:'Matthew', 41:'Mark', 42:'Luke', 43:'John', 44:'Acts', 45:'Romans', 46:'Corinthians 1', 47:'Corinthians 2', 48:'Galatians', 49:'Ephesians', 50:'Philippians', 51:'Colossians', 52:'Thessalonians 1', 53:'Thessalonians 2', 54:'Timothy 1', 55:'Timothy 2', 56:'Titus', 57:'Philemon', 58:'Hebrews', 59:'James', 60:'Peter 1', 61:'Peter 2', 62:'John 1', 63:'John 2', 64:'John 3', 65:'Jude', 66:'Revelation'}

dictbibleK = {1:"창세기", 2:"출애굽기", 3:"레위기", 4:"민수기", 5:"신명기", 6:"여호수아", 7:"사사기", 8:"룻기", 9:"사무엘상", 10:"사무엘하", 11:"열왕기상", 12:"열왕기하", 13:"역대상", 14:"역대하", 15:"에스라", 16:"느헤미야", 17:"에스더", 18:"욥기", 19:"시편", 20:"잠언", 21:"전도서", 22:"아가", 23:"이사야", 24:"예레미아", 25:"예레미야 애가", 26:"에스겔", 27:"다니엘", 28:"호세아", 29:"요엘", 30:"아모스", 31:"오바댜", 32:"요나", 33:"미가", 34:"나훔", 35:"하박국", 36:"스바냐", 37:"학개", 38:"스가랴", 39:"말라기", 40:"마태복음", 41:"마가복음", 42:"누가복음", 43:"요한복음", 44:"사도행전", 45:"로마서", 46:"고린도전서", 47:"고린도후서", 48:"갈라디아서", 49:"에베소서", 50:"빌립보서", 51:"골로새서", 52:"데살로니가전서", 53:"데살로니가후서", 54:"디모데전서", 55:"디모데후서", 56:"디도서", 57:"빌레몬서", 58:"히브리서", 59:"야고보서", 60:"베드로전서", 61:"베드로후서", 62:"요한1서", 63:"요한2서", 64:"요한3서", 65:"유다서", 66:"요한계시록"}


try:
    bookall = ''
    bookall_list = []

    connh = sqlite3.connect('bible_hebrew.sqlite')
    cursorh = connh.cursor()

    connc = sqlite3.connect('和合本.db')
    cursorc = connc.cursor()
    
    connk = sqlite3.connect('bibles.sqlite')
    cursork = connk.cursor()

    conne = sqlite3.connect('web.db')
    cursore = conne.cursor()

    conng = sqlite3.connect('bible_greek.sqlite')
    cursorg = conng.cursor()
#################################中文开始##################
    for book in runsql(cursorc, 'select * from Bible'):
        bookcontent = book[4] #内容
        bookno = book[1] #创世纪为1,这样的序号
        chapterno = book[2] #章
        verseno = book[3] #节
        bookall =  dictbible[bookno] + ' ' + str(chapterno) + '-' + str(verseno) + ' ' + str(bookcontent)
        bookall_list.append(bookall)
        #################################中文开始##################

        #################################韩文继续##################
        book_k = cursork.execute('select * from bible where pyeon=? and jang=? and jeol=?', (dictbibleK[bookno], chapterno, verseno)).fetchall()
        if book_k:
            bookall =  dictbibleK[bookno] + ' ' + str(book_k[0][2]) + '-' + str(book_k[0][3]) + ' ' + str(book_k[0][4])
        else:
            bookall = '这节韩语没有'
        bookall_list.append(bookall)
        #################################韩文继续##################

        #################################英文继续##################
        book_e = cursore.execute('select * from Bible where Book=? and Chapter=? and Verse=?', (bookno, chapterno, verseno)).fetchall()
        if book_e:
            bookall =  dictbibleE[bookno] + ' ' + str(book_e[0][1]) + '-' + str(book_e[0][2]) + ' ' + str(book_e[0][3])
        else:
            bookall = '这节英语没有'
        bookall_list.append(bookall)
        #################################英文继续##################

        #################################希伯来文继续##################
        book_h = cursorh.execute('select * from bible_hebrew where c4book_no=? and c5chapter_no=? and c6verse_no=?', (bookno, chapterno, verseno)).fetchall()
        if book_h:
            bookall = str(book_h[0][2]) + ' ' + str(book_h[0][3]) + '-' + str(book_h[0][4]) + ' ' + str(book_h[0][1])
        else:
            bookall = '这节希伯来文没有'
        bookall_list.append(bookall)
        #################################希伯来文继续##################
        
        #################################希腊文继续##################
        book_g = cursorg.execute('select * from bible_greek where c4book_no=? and c5chapter_no=? and c6verse_no=?', (bookno, chapterno, verseno)).fetchall()
        if book_g:
            bookall = str(book_g[0][2]) + ' ' + str(book_g[0][3]) + '-' + str(book_g[0][4]) + ' ' + str(book_g[0][1])
        else:
            bookall = '这节希腊文没有'
        bookall_list.append(bookall)
        #################################希腊文继续##################

        bookall_list.append('\n')


        #print('\n'.join(bookall_list))
        #input()
    write2file('ckehg.txt', '\n'.join(bookall_list))
finally:
    closedb(connc, cursorc)
    closedb(conne, cursore)
    closedb(connk, cursork)
    closedb(connh, cursorh)
    closedb(conng, cursorg)
