#!/usr/bin/env python3

from tableDefine import *
from chinese_voice import *

#import virtkey #模拟按键的。。。
#vk = virtkey.virtkey()

#def defaultCMD(KEY, v=vk):
    #v.press_unicode(ord(KEY))
    #v.release_unicode(ord(KEY))
def addExt(dataobj, con):
    extend = dataobj.find(NAME='Con', value=con)[0][4]
    if extend == None:
        extend = input('InputExt:')
    else:
        extend = extend + '\n' + input('InputExt:')
    #print(extend)
    dataobj.update(NAME='Con', value=con, Other2=extend)
    print(dataobj.find(NAME='Con', value=con))

def acceptInput(dataobj, con):
    #defaultCMD('2')
    CMD = input() or '2'
    print(CMD)
    if CMD == 'EXT':
        addExt(dataobj, con)
        input()
    elif CMD == 'NO':
        #print(dataobj.find(NAME='Con', value=con))
        #input()
        #dataobj.delete(NAME='Con', value=con)
        #input()
        pass
    elif CMD == 'exit':
        exit()
    return CMD

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
        ISp = '______________________________________________\n'
        #ISp = ''
        global common 
        global every_week 
        global every_month
        global every_year
        #print('\t%s' % getdaystime(0))
        #input(ISp)

        day = datetime.now() + timedelta(days=daydelta)
        week_day = day.strftime('%w')
        month_day = day.strftime('%d')
        monthday = day.strftime('%m%d')
        ymd = day.strftime('%Y%m%d')
        
        
        def printExtConEnv(ext, con, env, file_name):
            if ext and env:
                #print('%s\n\n%s\n\n补充/感想:\n%s' % (env, con, ext))
                print('%s\n\n%s\n\n补充/感想:\n%s' % (con, env, ext))
                print(ISp)
                texts = con+'。'+env+'。'+ext
            elif env:
                #print('%s\n\n%s\n' % (env, con))
                print('%s\n\n%s\n' % (con, env))
                print(ISp)
                texts = con+'。'+env
            elif ext:
                print('%s\n\n补充/感想:\n%s' % (con, ext))
                print(ISp)
                texts = con+'。'+ext
            else:
                print('%s' % (con))
                print(ISp)
                texts = con
            file_name = '/home/ed/grace_voice_file/voice4gs_data/'+file_name
            if os.path.exists(file_name):
                cvlc_play_mp3(file_name)
            else:
                texts2voice_file(texts, file_name)
                cvlc_play_mp3(file_name)

        #统一先查好，避免因为数据变表而重复查询
        every_year_info = every_year.find('MonthDay', monthday)
        every_month_info = every_month.find('Day', month_day)
        every_week_info = every_week.find('Day', week_day)
        #打印안내서...
        #input('YES, NO, EXT, exit')
        if every_year_info:
            for ey_info in every_year_info:
                runsyscmd()
                print(ISp)
                con = ey_info[2]
                env = ey_info[3]
                ext = ey_info[4]
                file_name = ey_info[5]
                printExtConEnv(ext, con, env, file_name)
                print('Year\n____')

                CMD = acceptInput(every_year, con)
                if CMD == 'NO' or CMD == '8':
                    every_year.delete('Con', con)
                    every_month.add(Day=getnowtime('d'), Con=con, Other1=env, Other2=ext, Other3=file_name)
                elif CMD == 'YES' or CMD == 'dd':
                    if input('确定删除吗？y/n:') == 'y':
                        every_year.delete('Con', con)

        if every_month_info:
            for em_info in every_month_info:
                runsyscmd()
                print(ISp)
                con = em_info[2]
                env = em_info[3]
                ext = em_info[4]
                file_name = em_info[5]
                printExtConEnv(ext, con, env, file_name)
                print('Month\n_____')
                CMD = acceptInput(every_month, con)

                if CMD == 'YES' or CMD == '2':
                    #print('delete%s' % con)
                    every_month.delete(NAME='Con', value=con)
                    #print('insert%s' % con)
                    every_year.add(MonthDay=getnowtime('md'), Con=con, Other1=env, Other2=ext, Other3=file_name)
                elif CMD == 'NO' or CMD == '8':
                    #print('%s-1' % times)
                    every_month.delete(NAME='Con', value=con)
                    every_week.add(Day=getnowtime('week'), Con=con, Other1=env, Other2=ext, Other3=file_name)

        if every_week_info:
            for ew_info in every_week_info:
                runsyscmd()
                print(ISp)
                con = ew_info[2]
                env = ew_info[3]
                ext = ew_info[4]
                file_name = ew_info[5]
                printExtConEnv(ext, con, env, file_name)
                print('Week\n____')
                CMD = acceptInput(every_week, con)

                if CMD == 'YES' or CMD == '2':
                    every_week.delete(NAME='Con', value=con)
                    every_month.add(Day=getnowtime('d'), Con=con, Other1=env, Other2=ext, Other3=file_name)
                elif CMD == 'NO' or CMD == '8':
                    #print('%s-1' % times)
                    #every_week.update(NAME='Other3', value=times, Other3=int(times)-1)
                    common.add(Ymd=getdaystime(1), Con=con, Other1=env, Other2=ext, Other3=file_name)
                    common.add(Ymd=getdaystime(3), Con=con, Other1=env, Other2=ext, Other3=file_name)
                    common.add(Ymd=getdaystime(5), Con=con, Other1=env, Other2=ext, Other3=file_name)

        common_info = common.find('Ymd', ymd)
        if common_info:
            for c_info in common_info:
                runsyscmd()
                print(ISp)
                con = c_info[2]
                env = c_info[3]
                ext = c_info[4]
                file_name = c_info[5]
                printExtConEnv(ext, con, env, file_name)
                print('common')
                input()
                #acceptInput(common, con)
        

        
        runsyscmd()
        #print('축하합니다.今天任务完成！')

    yesterday(common) #删除昨天的    

    ############显示今天的###########
    #print('___________________________\n\n')
    everyday = readffile('everydaytoread.txt')
    if everyday:
        print(everyday.strip())
        input()
    showOneDay()
    #showAllTable()

finally:
    closedb(conn,cursor)

