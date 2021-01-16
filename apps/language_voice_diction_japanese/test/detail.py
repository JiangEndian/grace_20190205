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

        SUM = 0

        day = datetime.now() + timedelta(days=daydelta)
        week_day = day.strftime('%w')
        month_day = day.strftime('%d')
        monthday = day.strftime('%m%d')
        ymd = day.strftime('%Y%m%d')

        common_info = common.find('Ymd', ymd)
        SUM = len(common_info)
        SUM = str(SUM)
        #print('Common:'+ymd+':'+SUM)
        #if common_info:
            #for c_info in common_info:
                #print(c_info[2])
        
        every_week_info = every_week.find('Day', week_day)
        SUM = len(every_week_info)
        SUM = str(SUM)
        print('EveryWeek\t'+week_day+'\t'+SUM)
        #if every_week_info:
            #for ew_info in every_week_info:
                #print('W:%s' % ew_info[2])
        
        every_month_info = every_month.find('Day', month_day)
        SUM = len(every_month_info)
        SUM = str(SUM)
        print('EvertyMonth\t'+month_day+'\t'+SUM)
        #if every_month_info:
            #for em_info in every_month_info:
                #print('M:%s' % em_info[2])

        every_year_info = every_year.find('MonthDay', monthday)
        SUM = len(every_year_info)
        SUM = str(SUM)
        print('EveryYear\t'+monthday+'\t'+SUM)
        #if every_year_info:
            #for ey_info in every_year_info:
                #print('Y:%s' % ey_info[2])
        return SUM

    #yesterday(common) #删除昨天的    
    
    #################显示后30天的#############
    ew_sum = len(every_week.find())
    em_sum = len(every_month.find())
    ey_sum = len(every_year.find())
    print('EveryWeekAll\t'+str(ew_sum))
    print('EveryMonthAll\t'+str(em_sum))
    print('EveryYearAll\t'+str(ey_sum))
    print('All:\t'+str(ew_sum+em_sum+ey_sum))
    input()
    for i in range(31):
        #print('%s: %d' % (getdaystime(i), showOneDay(i)))
        showOneDay(i)
        print('\n')
        #print('___________________________\n')
        #showOneDay(i)
        #print('___________________________')

finally:
    closedb(conn,cursor)

