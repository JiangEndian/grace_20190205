#!/usr/bin/env python3

from tableDefine import *

finishedYear = 2083

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

        day = datetime.datetime.now() + datetime.timedelta(days=daydelta)
        week_day = day.strftime('%w')
        month_day = day.strftime('%d')
        monthday = day.strftime('%m%d')
        ymd = day.strftime('%Y%m%d')

        common_info = common.find('Ymd', ymd)
        if common_info:
            for c_info in common_info:
                print(c_info[2])
        
        every_week_info = every_week.find('Day', week_day)
        if every_week_info:
            for ew_info in every_week_info:
                print('W:%s' % ew_info[2])
        
        every_month_info = every_month.find('Day', month_day)
        if every_month_info:
            for em_info in every_month_info:
                print('M:%s' % em_info[2])

        every_year_info = every_year.find('MonthDay', monthday)
        if every_year_info:
            for ey_info in every_year_info:
                print('Y:%s' % ey_info[2])

    yesterday(common) #删除昨天的    
    
    #################显示明天的#############
    this_year_by_AD = getdaystime(1)
    this_year_by_AA = 3969 + int(this_year_by_AD[0:4])
    life_days = -(datetime.datetime(1994, 9, 7) - datetime.datetime.now()).days
    remain_days = 13630 - life_days
    life_days_second = str(13630*24*60*60-(-(datetime.datetime(1994, 9, 7, 12, 12, 12) - datetime.datetime.now()).total_seconds())).split('.')[0]
    #print(life_days_second)
    #exit()
    #print('%s' % this_year_by_AD + ' / AA' + str(this_year_by_AA) + ' 距6000年:-%s(已活:%s)' % (str(remain_days), str(life_days)))
    #print('%s' % this_year_by_AD + ' / AA' + str(this_year_by_AA) + ' 距6000年:-%s秒(神已养活:%s)' % (str(life_days_second), str(life_days)))
    print('%s' % this_year_by_AD + ' / AA' + str(this_year_by_AA) + '(神已养活:%s)' % (str(life_days)))
    print('___________________________\n')
    #添加耶稣今年来的概率
    probability = (1-(1999/2000)**(this_year_by_AA-4000))*100
    #print('%s年耶稣有 %.2f%% 的可能会来，方舟进度:%.2f%%' % (this_year_by_AD[0:4], probability, (finishedYear/7000*100)))
    print('%s年耶稣有 %.2f%% 的可能会来' % (this_year_by_AD[0:4], probability))
    #添加实践T的任务，每天
    #print('%s实践T_ NEW(一句/每法)' % getdaystime(1))
    showOneDay(1)
    print('___________________________\n')

    ##这个是打印文件里面的列表的
    everyday = readffile('everydaytodolist.txt')
    print(everyday.strip())
    print('___________________________\n')
finally:
    closedb(conn,cursor)

