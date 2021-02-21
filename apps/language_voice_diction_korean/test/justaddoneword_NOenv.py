#!/usr/bin/env python3

from tableDefine import *
from MyPython3 import *

global voice_number
voice_number = 1001

global dir_name
dir_name = input('输入文件夹名：')
cvlc_play_mp3('~/grace_voice_file/%s/wavFile1001.wav' % dir_name, 1, '-', '=')
if input('确认有声音？文件夹无误？YES?') != 'YES':
    exit(0)

def addEveryWeek():
    global every_week
    global common
    global voice_number
    global dir_name
    #day = input('Day(%s):' % getnowtime('week')) or getnowtime('week')
    day = getnowtime('week')
    con = input('word:')
    if not con:
        print('wordEmpty...')
        exit()
    #env = input('mean:') #[ɪnˈvaɪrənmənt]环境
    env = ''
    f_name = '%s/wavFile%s.wav' % (dir_name, str(voice_number))
    voice_number += 1
    
    if True:
        every_week.add(Day=day, Con=con, Other1=env, Other2=f_name)
        print(every_week.find('Con', con))
        common.add(Ymd=getdaystime(1), Con=con, Other1=env, Other2=f_name)
        common.add(Ymd=getdaystime(3), Con=con, Other1=env, Other2=f_name)

def addEveryMonth():
    global every_month
    day = input('Day(%s):' % getnowtime('d')) or getnowtime('d')
    con = input('EveryMonthContent:')
    print('请确认(%s:%s).' % (day, con))
    if input('InputYES2Save:') == 'YES':
        every_month.add(Day=day, Con=con)

def addEveryYear():
    global every_year
    monthday = input('MonthDay(%s):' % getnowtime('md')) or getnowtime('md')
    con = input('EveryYearContent:')
    print('请确认(%s:%s).' % (monthday, con))
    if input('InputYES2Save:') == 'YES':
        every_year.add(MonthDay=monthday, Con=con)

def addCommon(*days):
    global common
    con = input('Content:')
    print('请确认(%s:%s).' % (','.join(days), con))
    if input('InputYES2Save:') == 'YES':
        for day in days:
            common.add(Ymd=day, Con=con)

def showAllTable():
    global common
    global every_week
    global every_month
    global every_year
    print('common:', common.find())
    print('every_week:', every_week.find())
    print('every_month:', every_month.find())
    print('every_year:', every_year.find())

try:
    conn, cursor = opendb('PlanDatabase.sqlite')

    class Common(MyORM): #通用的计划放这里
        conn = conn
        cursor = cursor
        tableInfo = tableCommon
    class EveryWeek(MyORM): #通用的计划放这里
        conn = conn
        cursor = cursor
        tableInfo = tableEveryWeek
    class EveryMonth(MyORM): #通用的计划放这里
        conn = conn
        cursor = cursor
        tableInfo = tableEveryMonth
    class EveryYear(MyORM): #通用的计划放这里
        conn = conn
        cursor = cursor
        tableInfo = tableEveryYear
    
    global common
    global every_week
    global every_month
    global every_year
    common = Common()
    every_week = EveryWeek()
    every_month = EveryMonth()
    every_year = EveryYear()

    def showOneDay(daydelta=0): 
        global common 
        global every_week 
        global every_month
        global every_year

        day = datetime.now() + timedelta(days=daydelta)
        week_day = day.strftime('%w')
        month_day = day.strftime('%d')
        monthday = day.strftime('%m%d')
        ymd = day.strftime('%Y%m%d')

        common_info = common.find('Ymd', ymd)
        if common_info:
            print(common_info[0][2])
        
        every_week_info = every_week.find('Day', week_day)
        if every_week_info:
            print('W:%s' % every_week_info[0][2])
        
        every_month_info = every_month.find('Day', month_day)
        if every_month_info:
            print('M:%s' % every_month_info[0][2])

        every_year_info = every_year.find('MonthDay', monthday)
        if every_year_info:
            print('Y:%s' % every_year_info[0][2])
    
    #showAllTable()
    #showOneDay()
    while True:
        addEveryWeek()

finally:
    closedb(conn,cursor)

