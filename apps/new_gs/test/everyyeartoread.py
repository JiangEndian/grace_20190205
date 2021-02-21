#!/usr/bin/env python3

from tableDefine import *

def addEveryWeek():
    global every_week
    day = input('Day(%s):' % getnowtime('week')) or getnowtime('week')
    con = input('EveryWeekContent:')
    print('请确认(%s:%s).' % (day, con))
    if input('InputYES2Save:') == 'YES':
        every_week.add(Day=day, Con=con)

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
    env = input('EveryYearEnvironment:') #[ɪnˈvaɪrənmənt]环境
    print('请确认:%s\n%s\n%s' % (monthday, env, con))
    if input('InputYES2Save:') == 'YES':
        every_year.add(MonthDay=monthday, Con=con, Other1=env)

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
    addEveryYear()

finally:
    closedb(conn,cursor)

