#!/usr/bin/env python3

from tableDefine import *

def addEveryWeek():
    global every_week
    global common
    #day = input('Day(%s):' % getnowtime('week')) or getnowtime('week')
    day = getnowtime('week')
    con = input('word:')
    if not con:
        print('wordEmpty...')
        exit()
    env = input('mean:') #[ɪnˈvaɪrənmənt]环境
    #print('请确认:%s\n%s\n%s' % (day, env, con))
    #if input('InputYES2Save:') == 'YES':
    if True:
        every_week.add(Day=day, Con=con, Other1=env, Other3=3)
        print(every_week.find('Con', con))
        common.add(Ymd=getdaystime(1), Con=con, Other1=env)
        common.add(Ymd=getdaystime(3), Con=con, Other1=env)

def addExt(dataobj, con):
    extend = dataobj.find(NAME='Con', value=con)[0][4]
    if extend == None:
        extend = input('InputExampleAndIt\'sMean:')
    else:
        extend = extend + '\n' + input('InputExampleAndIt\'sMean:')
    #print(extend)
    dataobj.update(NAME='Con', value=con, Other2=extend)
    print(dataobj.find(NAME='Con', value=con))

def acceptInput(dataobj, con):
    CMD = input() or '2'
    print(CMD)
    #if CMD == 'EXT':
        #addExt(dataobj, con)
        #CMD = input()
    if CMD == 'ADD':
        while CMD == 'ADD':
            addEveryWeek()
            CMD = input()
    elif CMD == 'NO':
        #print(dataobj.find(NAME='Con', value=con))
        #input()
        #dataobj.delete(NAME='Con', value=con)
        #input()
        pass
    elif CMD == 'exit':
        exit()
    return CMD

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
        #ISp = '______________________________________________'
        ISp = ''
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
        
        def printExtConEnv(ext, con, env, times=1):
            print(con)
            print(env)
            CMD = play_enter('~/grace_voice_file/%s' % ext, time4input=1, times=times)
            if CMD == '':
                CMD = '2'
            elif CMD == 'p':
                CMD = input('输入相应命令2/8继续:')
            print(CMD)
            return CMD
            if ext and env:
                #print('%s\n\n%s\n\n补充/感想:\n%s' % (env, con, ext))
                #print('%s\n\n%s\n\n补充/感想:\n%s' % (con, env, ext))
                #print(ISp)
                print(con)
                input()
                print(env)
                input()
                print(ext)
                print(ISp)
                print(ISp)
            elif env:
                #print('%s\n\n%s\n' % (env, con))
                #print('%s\n\n%s\n' % (con, env))
                print(con)
                input()
                print(env)
                print(ISp)
                print(ISp)
            elif ext:
                #print('%s\n\n补充/感想:\n%s' % (con, ext))
                print(con)
                input()
                print(ext)
                print(ISp)
                print(ISp)
            else:
                print('%s' % (con))
                print(ISp)
                print(ISp)
        
        #统一先查好，避免因为数据变表而重复查询
        every_year_info = every_year.find('MonthDay', monthday)[::-1]
        every_month_info = every_month.find('Day', month_day)[::-1]
        every_week_info = every_week.find('Day', week_day)[::-1]
        common_info = common.find('Ymd', ymd)[::-1]
        if common_info:
            for c_info in common_info:
                runsyscmd()
                print('common')
                print(ISp)
                con = c_info[2]
                env = c_info[3]
                ext = c_info[4]
                CMD = printExtConEnv(ext, con, env, 2)
        if every_week_info:
            for ew_info in every_week_info:
                runsyscmd()
                print('_________________________________\n\nWeek\n_________________________________')
                print(ISp)
                con = ew_info[2]
                env = ew_info[3]
                ext = ew_info[4]
                CMD = printExtConEnv(ext, con, env)
                #CMD = acceptInput(every_week, con)

                if CMD == 'YES' or CMD == '2':
                    every_week.delete(NAME='Con', value=con)
                    every_month.add(Day=getnowtime('d'), Con=con, Other1=env, Other2=ext, Other3=2)
                elif CMD == 'NO' or CMD == '8':
                    #print('%s-1' % times)
                    #every_week.update(NAME='Other3', value=times, Other3=int(times)-1)
                    #print('下周继续，加油！')
                    common.add(Ymd=getdaystime(1), Con=con, Other1=env, Other2=ext)
                    common.add(Ymd=getdaystime(3), Con=con, Other1=env, Other2=ext)
                    common.add(Ymd=getdaystime(5), Con=con, Other1=env, Other2=ext)
        if every_month_info:
            for em_info in every_month_info:
                runsyscmd()
                print('_________________________________\n\nMonth\n_________________________________')
                print(ISp)
                con = em_info[2]
                env = em_info[3]
                ext = em_info[4]
                CMD = printExtConEnv(ext, con, env)
                #CMD = acceptInput(every_month, con)

                if CMD == 'YES' or CMD == '2':
                    #print('delete%s' % con)
                    every_month.delete(NAME='Con', value=con)
                    #print('insert%s' % con)
                    every_year.add(MonthDay=getnowtime('md'), Con=con, Other1=env, Other2=ext)
                elif CMD == 'NO' or CMD == '8':
                    #print('%s-1' % times)
                    every_month.delete(NAME='Con', value=con)
                    every_week.add(Day=getnowtime('week'), Con=con, Other1=env, Other2=ext)
        if every_year_info:
            for ey_info in every_year_info:
                runsyscmd()
                print('__________________________________\n\nYear\n__________________________________')
                print(ISp)
                con = ey_info[2]
                env = ey_info[3]
                ext = ey_info[4]
                
                CMD = printExtConEnv(ext, con, env)

                #CMD = acceptInput(every_year, con)
                if CMD == 'NO' or CMD == '8':
                    every_year.delete('Con', con)
                    every_month.add(Day=getnowtime('d'), Con=con, Other1=env, Other2=ext)
                elif CMD == 'YES' or CMD == '2':
                    every_year.delete('Con', con)


                    #input()

                #printExtConEnv(ext, con, env)
                #acceptInput(common, con)
        

        
        runsyscmd()
        print('축하합니다.今天任务完成！')

    yesterday(common) #删除昨天的    

    ############显示今天的###########
    #print('___________________________\n\n')
    #everyday = readffile('everydaytoread.txt')
    #if everyday:
        #print(everyday.strip())
        #input()
    showOneDay()
    #showAllTable()

finally:
    closedb(conn,cursor)

