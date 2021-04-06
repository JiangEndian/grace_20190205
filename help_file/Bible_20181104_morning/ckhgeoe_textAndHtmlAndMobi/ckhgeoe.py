#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3
from newestMyPython3 import *
import re

VersionInfo = '''
和合本/KRV/Hebrew/LXXBr/NIV/Original/WEB

Old Testament ---------------------------------------------

Genesis, Exodus, Leviticus, Numbers, Deuteronomy,

Joshua, Judges, Ruth, Samuel 1/2, Kings 1/2, Chronicles 1/2, Ezra, Nehemiah, Esther,

Job, Psalms, Proverbs, Ecclesiastes, Song of Songs,

Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel,

Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi,


New Testament --------------------------------------------

Matthew, Mark, Luke, John,

Acts,

Romans, Corinthians 1/2, Galatians, Ephesians, Philippians, Colossians, Thessalonians 1/2, Timothy 1/2, Titus, Philemon,

Hebrews, James, Peter 1/2, John 1/2/3, Jude,

Revelation.


search for hebrew even no vowel: א.ל.ה.ים

background, foreground setting.
set bg=light/dark
hi Normal guibg=white/black guifg=black/white

'''
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
    
dictbibleC = {1:'创世纪', 2:'出埃及记', 3:'利未记', 4:'民数记', 5:'申命记', 6:'约书亚记', 7:'士师记', 8:'路得记', 9:'撒母耳记上', 10:'撒母耳记下', 11:'列王纪上', 12:'列王纪下', 13:'历代志上', 14:'历代志下', 15:'以斯拉记', 16:'尼希米记', 17:'以斯帖记', 18:'约伯记', 19:'诗篇', 20:'箴言', 21:'传道书', 22:'雅歌', 23:'以赛亚书', 24:'耶利米书', 25:'耶利米哀歌', 26:'以西结书', 27:'但以理书', 28:'何西阿书', 29:'约珥书', 30:'阿摩司书', 31:'俄巴底亚书', 32:'约拿书', 33:'弥迦书', 34:'那鸿书', 35:'哈巴谷书', 36:'西番雅书', 37:'哈该书', 38:'撒迦利亚书', 39:'玛拉基书', 40:'马太福音', 41:'马可福音', 42:'路加福音', 43:'约翰福音', 44:'使徒行传', 45:'罗马书', 46:'哥林多前书', 47:'哥林多后书', 48:'加拉太书', 49:'以弗所书', 50:'腓立比书', 51:'歌罗西书', 52:'帖撒罗尼迦前书', 53:'帖撒罗尼迦后书', 54:'提摩太前书', 55:'提摩太后书', 56:'提多书', 57:'腓利门书', 58:'希伯来书', 59:'雅各书', 60:'彼得前书', 61:'彼得后书', 62:'约翰一书', 63:'约翰二书', 64:'约翰三书', 65:'犹大书', 66:'启示录'}

dictbibleEweb = {1:'Genesis', 2:'Exodus', 3:'Leviticus', 4:'Numbers', 5:'Deuteronomy', 6:'Joshua', 7:'Judges', 8:'Ruth', 9:'Samuel 1', 10:'Samuel 2', 11:'Kings 1', 12:'Kings 2', 13:'Chronicles 1', 14:'Chronicles 2', 15:'Ezra', 16:'Nehemiah', 17:'Esther', 18:'Job', 19:'Psalms', 20:'Proverbs', 21:'Ecclesiastes', 22:'Song of Songs', 23:'Isaiah', 24:'Jeremiah', 25:'Lamentations', 26:'Ezekiel', 27:'Daniel', 28:'Hosea', 29:'Joel', 30:'Amos', 31:'Obadiah', 32:'Jonah', 33:'Micah', 34:'Nahum', 35:'Habakkuk', 36:'Zephaniah', 37:'Haggai', 38:'Zechariah', 39:'Malachi', 40:'Matthew', 41:'Mark', 42:'Luke', 43:'John', 44:'Acts', 45:'Romans', 46:'Corinthians 1', 47:'Corinthians 2', 48:'Galatians', 49:'Ephesians', 50:'Philippians', 51:'Colossians', 52:'Thessalonians 1', 53:'Thessalonians 2', 54:'Timothy 1', 55:'Timothy 2', 56:'Titus', 57:'Philemon', 58:'Hebrews', 59:'James', 60:'Peter 1', 61:'Peter 2', 62:'John 1', 63:'John 2', 64:'John 3', 65:'Jude', 66:'Revelation'}

dictbibleK = {1:"창세기", 2:"출애굽기", 3:"레위기", 4:"민수기", 5:"신명기", 6:"여호수아", 7:"사사기", 8:"룻기", 9:"사무엘상", 10:"사무엘하", 11:"열왕기상", 12:"열왕기하", 13:"역대상", 14:"역대하", 15:"에스라", 16:"느헤미야", 17:"에스더", 18:"욥기", 19:"시편", 20:"잠언", 21:"전도서", 22:"아가", 23:"이사야", 24:"예레미아", 25:"예레미야 애가", 26:"에스겔", 27:"다니엘", 28:"호세아", 29:"요엘", 30:"아모스", 31:"오바댜", 32:"요나", 33:"미가", 34:"나훔", 35:"하박국", 36:"스바냐", 37:"학개", 38:"스가랴", 39:"말라기", 40:"마태복음", 41:"마가복음", 42:"누가복음", 43:"요한복음", 44:"사도행전", 45:"로마서", 46:"고린도전서", 47:"고린도후서", 48:"갈라디아서", 49:"에베소서", 50:"빌립보서", 51:"골로새서", 52:"데살로니가전서", 53:"데살로니가후서", 54:"디모데전서", 55:"디모데후서", 56:"디도서", 57:"빌레몬서", 58:"히브리서", 59:"야고보서", 60:"베드로전서", 61:"베드로후서", 62:"요한1서", 63:"요한2서", 64:"요한3서", 65:"유다서", 66:"요한계시록"}


def get_all_bible_rows_from_database(file_name, table):
    try:
        all_rows = []
        conn = sqlite3.connect(file_name)
        cursor = conn.cursor()
        all_rows = runsql(cursor, 'select * from ' + table)
    finally:
        closedb(conn, cursor)
        return all_rows

#C中文圣经
all_rows_ChineseBible_verses = get_all_bible_rows_from_database('和合本.db', 'Bible')
#print(len(all_rows_ChineseBible_verses)) #31102

#K韩文圣经
all_rows_KRV_books = get_all_bible_rows_from_database('KRV.SQLite3', 'books')
#print(len(all_rows_KRV_books)) #66
dictbibleK = {}
for one_row in all_rows_KRV_books:
    dictbibleK[one_row[0]] = one_row[2]
#print(dictbibleK) #得到目录
all_rows_KRV_verses = get_all_bible_rows_from_database('KRV.SQLite3', 'verses')
#print(len(all_rows_KRV_verses)) #31103

#H希伯来文圣经
all_rows_Hebrew_books = get_all_bible_rows_from_database('MHBc.SQLite3', 'books')
#print(len(all_rows_Hebrew_books)) #66
dictbibleH = {}
dictbibleH_step = 1
for one_row in all_rows_Hebrew_books:
    #dictbibleH[one_row[0]] = one_row[2]
    dictbibleH[dictbibleH_step] = one_row[2]
    dictbibleH_step += 1
#print(dictbibleH) #得到目录
all_rows_Hebrew_verses = get_all_bible_rows_from_database('bible_hebrew.sqlite', 'bible_hebrew')
#print(len(all_rows_Hebrew_verses)) #31152
all_rows_Hebrew_verses_Original = get_all_bible_rows_from_database('Tanakh.db', 'Bible')
#print(len(all_rows_Hebrew_verses_Original)) #23144

#E英语圣经
all_rows_NIV_books = get_all_bible_rows_from_database('NIV.SQLite3', 'books')
#print(len(all_rows_NIV_books)) #66
dictbibleEniv = {}
dictbibleEweb = {}
dictbibleEweb_step = 1
for one_row in all_rows_NIV_books:
    dictbibleEniv[one_row[0]] = one_row[2]
    dictbibleEweb[dictbibleEweb_step] = one_row[2]
    dictbibleEweb_step += 1
#print(dictbibleE) #得到目录

dictbibleH = dictbibleEweb #希伯来语的目录不对

all_rows_NIV_verses = get_all_bible_rows_from_database('NIV.SQLite3', 'verses')
#print(len(all_rows_NIV_verses)) #31102, same with Chinese Bible
all_rows_web_verses = get_all_bible_rows_from_database('web.db', 'Bible')
#print(len(all_rows_web_verses)) #31103, same with KRV

#G希腊文圣经
all_rows_Greek_books = get_all_bible_rows_from_database('Sfilos.SQLite3', 'books')
#print(len(all_rows_Greek_books)) #66
dictbibleG = {}
for one_row in all_rows_Greek_books:
    dictbibleG[one_row[1]] = one_row[3]
#print(dictbibleG) #得到目录
all_rows_Greek_verses = get_all_bible_rows_from_database('Sfilos.SQLite3', 'verses')
#print(len(all_rows_Greek_verses)) #31100
all_rows_Greek_verses_Original = get_all_bible_rows_from_database('Greek_original.SQLite3', 'verses')
#print(len(all_rows_Greek_verses_Original)) #7957

#O合成的原文，排列顺序为CKHGEnivOEweb
strinfo = re.compile('[0-9a-zA-Z\-]') #替换掉希腊文的单词号
all_rows_Original_verses = all_rows_Hebrew_verses_Original
for verse in all_rows_Greek_verses_Original:
    new_verse = (0, int(verse[0])/10-7, verse[1], verse[2], strinfo.sub('', verse[3]))
    #print(len(all_rows_Original_verses))
    #print(new_verse)
    #input()
    all_rows_Original_verses.append(new_verse)
#print(len(all_rows_Original_verses)) #31101
#print(len(all_rows_Original)) #31101

strinfo = re.compile('<.*?>') #替换掉希伯来文的<单词号>
def combine_column_of_Bible_of_firstType(row, dictbible):#Book,Chapter,Verse,Scripture
    return dictbible[row[1]] + ' ' + str(row[2]) + '-' + str(row[3]) + ' ' + row[4]
def combine_column_of_Bible_of_secondType(row, dictbible):
    return dictbible[row[0]] + ' ' + str(row[1]) + '-' + str(row[2]) + ' ' + row[3]
def combine_column_of_Bible_of_3rdType(row, dictbible):
    return dictbible[row[2]] + ' ' + str(row[3]) + '-' + str(row[4]) + ' ' + row[1]
def combine_column_of_Bible_of_4thType(row, dictbible, strinfo=strinfo):#Book,Chapter,Verse,Scripture
    new_verse = dictbible[row[1]] + ' ' + str(row[2]) + '-' + str(row[3]) + ' ' + strinfo.sub('', row[4])
    return new_verse


steps = {'stepC':0, 'stepK':0, 'stepH':0, 'stepG':0, 'stepEniv':0, 'stepO':0, 'stepEweb':0}
all_text_list = []
all_text_list.append(VersionInfo)

def oneEnterNextVerseAndOneStayLastVerse(LastVerse, NextVerse): #准备改成verse感觉比较好
    FlagDifferentInNextVerse = False
    HaveNextChapter = False
    HaveLastChapter = False
    RunVerses = [None,'NO']
    #for key in NextVerse:
        #if NextVerse[key] != NextVerse['C']:
            #FlagDifferentInNextVerse = True
            #if NextVerse[key] > NextVerse['C']:
                #RunVerses = [key, 'stop']
            #else:
                #RunVerses = [key, 'others_stop']
    for key in NextVerse:
        if NextVerse[key] == 1:
            #print('==1')
            HaveNextChapter = True #天呐，我把这个赋值写成了==，天呐。。。
        if NextVerse[key] != 1:
            #print('!=1')
            HaveLastChapter = True

    if HaveNextChapter and HaveLastChapter:
        #input('Yes, Different')
        RunVerses = []
        for key in NextVerse:
            if NextVerse[key] != 1:
                pass
                RunVerses.append(key)

    #RunVerses = [None, 'NO']
    return RunVerses
            
        
RunVerses = [None, 'NO']
LastVerse = {}
NextVerse = {}
for KEY in ['C','K','H','G','Eniv','O','Eweb']:
    LastVerse[KEY] = 0
    NextVerse[KEY] = 0
for i in range(33000):
    if len(all_rows_ChineseBible_verses) > steps['stepC'] and (RunVerses[0]==None or 'C' in RunVerses):
        all_text_list.append(combine_column_of_Bible_of_firstType(all_rows_ChineseBible_verses[steps['stepC']], dictbibleC))
        LastVerse['C'] = all_rows_ChineseBible_verses[steps['stepC']][3]
        if len(all_rows_ChineseBible_verses) != steps['stepC']+1:
            steps['stepC'] += 1
            NextVerse['C'] = all_rows_ChineseBible_verses[steps['stepC']][3]
    else:
        all_text_list.append('____')
    if len(all_rows_KRV_verses) > steps['stepK'] and (RunVerses[0]==None or 'K' in RunVerses):
        all_text_list.append(combine_column_of_Bible_of_secondType(all_rows_KRV_verses[steps['stepK']], dictbibleK))
        LastVerse['K'] = all_rows_KRV_verses[steps['stepK']][2]
        if len(all_rows_KRV_verses) != steps['stepK']+1:
            steps['stepK'] += 1
            NextVerse['K'] = all_rows_KRV_verses[steps['stepK']][2]
    else:
        all_text_list.append('____')
    if len(all_rows_Hebrew_verses) > steps['stepH'] and (RunVerses[0]==None or 'H' in RunVerses):
        all_text_list.append(combine_column_of_Bible_of_3rdType(all_rows_Hebrew_verses[steps['stepH']], dictbibleH))
        LastVerse['H'] = all_rows_Hebrew_verses[steps['stepH']][4]
        if len(all_rows_Hebrew_verses) != steps['stepH']+1:
            steps['stepH'] += 1
            NextVerse['H'] = all_rows_Hebrew_verses[steps['stepH']][4]
    else:
        all_text_list.append('____')
    if len(all_rows_Greek_verses) > steps['stepG'] and (RunVerses[0]==None or 'G' in RunVerses):
        all_text_list.append(combine_column_of_Bible_of_secondType(all_rows_Greek_verses[steps['stepG']], dictbibleG))
        LastVerse['G'] = all_rows_Greek_verses[steps['stepG']][2]
        if len(all_rows_Greek_verses) != steps['stepG']+1:
            steps['stepG'] += 1
            NextVerse['G'] = all_rows_Greek_verses[steps['stepG']][2]
    else:
        all_text_list.append('____')
    if len(all_rows_NIV_verses) > steps['stepEniv'] and (RunVerses[0]==None or 'Eniv' in RunVerses):
        all_text_list.append(combine_column_of_Bible_of_secondType(all_rows_NIV_verses[steps['stepEniv']], dictbibleEniv))
        LastVerse['Eniv'] = all_rows_NIV_verses[steps['stepEniv']][2]
        if len(all_rows_NIV_verses) != steps['stepEniv']+1:
            steps['stepEniv'] += 1
            NextVerse['Eniv'] = all_rows_NIV_verses[steps['stepEniv']][2]
    else:
        all_text_list.append('____')
    if len(all_rows_Original_verses) > steps['stepO'] and (RunVerses[0]==None or 'O' in RunVerses):
        all_text_list.append(combine_column_of_Bible_of_4thType(all_rows_Original_verses[steps['stepO']], dictbibleEweb))
        LastVerse['O'] = all_rows_Original_verses[steps['stepO']][3]
        if len(all_rows_Original_verses) != steps['stepO']+1:
            steps['stepO'] += 1
            NextVerse['O'] = all_rows_Original_verses[steps['stepO']][3]
    else:
        all_text_list.append('____')
    if len(all_rows_web_verses) > steps['stepEweb'] and (RunVerses[0]==None or 'Eweb' in RunVerses):
        all_text_list.append(combine_column_of_Bible_of_secondType(all_rows_web_verses[steps['stepEweb']], dictbibleEweb))
        LastVerse['Eweb'] = all_rows_web_verses[steps['stepEweb']][2]
        if len(all_rows_web_verses) != steps['stepEweb']+1:
            steps['stepEweb'] += 1
            NextVerse['Eweb'] = all_rows_web_verses[steps['stepEweb']][2]
    else:
        all_text_list.append('____')
    #print('\n'.join(all_text_list))
    #print(steps)
    #input()
    all_text_list.append('\n')
    RunVerses = oneEnterNextVerseAndOneStayLastVerse(LastVerse, NextVerse)
    #if RunVerses[0] != None and len(RunVerses)>2:
    #if RunVerses[0] != None:
    #if True:
        #print(LastVerse)
        #print(NextVerse)
        #print(RunVerses)
        #print(steps)
        
        #input()
BibleName = 'ckhgeoe.txt'
write2file(BibleName, '\n'.join(all_text_list))
print(steps)







#为了kindle的跳转链接处理，网页内部跳转形式








