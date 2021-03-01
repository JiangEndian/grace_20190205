#!/usr/bin/env python3

from tableDefine import *

def addEveryWeek():
    global every_week
    global common
    #day = input('Day(%s):' % getnowtime('week')) or getnowtime('week')
    day = getnowtime('week')
    file_name = getnowtime('ymdhms')+'.mp3'
    #con = input('Content:')
    con = 'ThisIsImage'
    #if not con:
        #print('Content Empty...')
        #exit()
    env = input('FileNameLocatedAtImages') #[ɪnˈvaɪrənmənt]环境
    #print('请确认:%s\n%s\n%s' % (day, env, con))
    #if input('InputYES2Save:') == 'YES':
    if True:
        every_week.add(Day=day, Con=con, Other1=env, Other3=file_name)
        #如果不是要立即复习的，像是课堂笔记之类的，不用加太多
        #不然太重，我会放弃明天的。太可怕了。。。
        #common.add(Ymd=getdaystime(1), Con=con, Other1=env, Other3=file_name)
        #common.add(Ymd=getdaystime(3), Con=con, Other1=env, Other3=file_name)
        #common.add(Ymd=getdaystime(5), Con=con, Other1=env, Other3=file_name)
        print(every_week.find(NAME='Con', value=con))

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
    ew_sum = len(every_week.find())
    em_sum = len(every_month.find())
    ey_sum = len(every_year.find())
    print('EveryWeekAll\t'+str(ew_sum))
    print('EveryMonthAll\t'+str(em_sum))
    print('EveryYearAll\t'+str(ey_sum))
    print('All:\t'+str(ew_sum+em_sum+ey_sum))
    input()

    #计数加入的条数用的。。。
    ALL_ADDED = 0

    while True:
        addEveryWeek()
        ALL_ADDED += 1
        print('ALL_ADDED:', ALL_ADDED)


finally:
    ew_sum = len(every_week.find())
    em_sum = len(every_month.find())
    ey_sum = len(every_year.find())
    print('EveryWeekAll\t'+str(ew_sum))
    print('EveryMonthAll\t'+str(em_sum))
    print('EveryYearAll\t'+str(ey_sum))
    print('All:\t'+str(ew_sum+em_sum+ey_sum))
    #input()
    closedb(conn,cursor)

