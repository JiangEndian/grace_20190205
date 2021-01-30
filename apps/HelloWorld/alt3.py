from django.http import HttpResponseRedirect 
from django.shortcuts import render

from tableDefine import * #导入自定义的东西

##现在的任务是：
global my_dict
my_dict = {}


#用前打开生成数据库
def create_database_link():
    global common
    global every_week
    global every_month
    global every_year
    global conn, cursor
    conn, cursor = opendb('language_voice_diction_english/PlanDatabase.sqlite')
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
    
    common = Common()
    every_week = EveryWeek()
    every_month = EveryMonth()
    every_year = EveryYear()
def close_database_link():
    global conn, cursor
    closedb(conn,cursor)
    
def alt3(request):
    global common_info
    global every_year_info
    global every_month_info
    global every_week_info
    global my_dict
    
    #1、未复习且未有dump则查询好，并放到dict中dump
    #   此阶段生成四个info文件，准备用来查询及操作
    if os.path.exists('language_voice_diction_english/4web_restudy/已复习') and not os.path.exists('language_voice_diction_english/4web_restudy/common_info'):
        my_dict['showinfo'] = '本日已复习'
        my_dict['con'] = 't1'
        my_dict['env'] = 't2'
        my_dict['ext'] = 't3'
        return HttpResponseRedirect('/alt1234') #复习完的直接回主页
        #return render(request, 'alt3.html', my_dict)
    elif os.path.exists('language_voice_diction_english/4web_restudy/common_info'):
        every_year_info = loadffile('language_voice_diction_english/4web_restudy/every_year_info')
        every_month_info = loadffile('language_voice_diction_english/4web_restudy/every_month_info')
        every_week_info = loadffile('language_voice_diction_english/4web_restudy/every_week_info')
        common_info = loadffile('language_voice_diction_english/4web_restudy/common_info')

        all_restudy_list = [len(every_year_info), len(every_month_info), len(every_week_info), len(common_info)]
        all_restudy = all_restudy_list[0] +all_restudy_list[1] + all_restudy_list[2] + all_restudy_list[3]

        all_time = all_restudy*16
        all_time_m = int(all_time // 60)
        all_time_s = int(all_time % 60)
        if all_restudy_list[2] + all_restudy_list[1] + all_restudy_list[0]== 0:
            my_dict['showinfo'] = '待复习%s条(%s.%s)，将load继续' % (all_restudy, all_time_m, all_time_s)
        elif all_restudy_list[1] + all_restudy_list[0]== 0:
            my_dict['showinfo'] = '待复习%s(w:%s)条(%s.%s)，将load继续' % (all_restudy, all_restudy_list[2], all_time_m, all_time_s)
        elif all_restudy_list[0] == 0:
            my_dict['showinfo'] = '待复习%s(m:%s,w:%s)条(%s.%s)，将load继续' % (all_restudy, all_restudy_list[1], all_restudy_list[2], all_time_m, all_time_s)
        else:
            my_dict['showinfo'] = '待复习%s(y:%s,m:%s,w:%s)条(%s.%s)，将load继续' % (all_restudy, all_restudy_list[0], all_restudy_list[1], all_restudy_list[2], all_time_m, all_time_s)
    else:
        #day = datetime.now() + timedelta(days=0) + timedelta(hours=8) 
        #原来的复习没问题，这个得到的时间，就比我的时钟慢8个点了，奇怪，一样的过程。。。不懂，加上
        day = datetime.now() + timedelta(days=0)
        #后来查了下django时区问题，在setting里面改了时区为上海，然后，就没事了。。。（现在在韩国改为首尔了）
        week_day = day.strftime('%w')
        month_day = day.strftime('%d')
        ymd = day.strftime('%Y%m%d')
        
        #提前年的，所以，年的单独调出。把这两句复制到py3里，就可以准确演算了
        y_day = datetime.now() + timedelta(days=72)
        monthday = y_day.strftime('%m%d')
        #print('monthday='+monthday)

        create_database_link()
        global common
        global every_week
        global every_month
        global every_year
        every_year_info = every_year.find('MonthDay', monthday)
        dump2file('language_voice_diction_english/4web_restudy/every_year_info', every_year_info)
        every_month_info = every_month.find('Day', month_day)
        dump2file('language_voice_diction_english/4web_restudy/every_month_info', every_month_info)
        every_week_info = every_week.find('Day', week_day)
        dump2file('language_voice_diction_english/4web_restudy/every_week_info', every_week_info)
        common_info = common.find('Ymd', ymd)
        dump2file('language_voice_diction_english/4web_restudy/common_info', common_info)
        close_database_link()
        all_restudy = len(every_year_info)+len(every_month_info)+len(every_week_info)+len(common_info)
        my_dict['showinfo'] = '将开始dump新的%s条复习，时间:%s' % (all_restudy, str(day))
        
#2、每次调用，读取一次dict，并相应accept_cmd修改数据库和dict
    if every_year_info:
        temp_info = list(every_year_info)
        for e_info in temp_info:
            my_dict['con'] = e_info[2]
            my_dict['env'] = e_info[3]
            my_dict['ext'] = e_info[4]
            my_dict['every_info'] = 'year'
            #20200302更新：添加获取下一条的预读
            next_info_index = temp_info.index(e_info)+1
            if len(temp_info) > 1:
                next_info = temp_info[next_info_index]
                my_dict['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            break
    elif every_month_info:
        temp_info = list(every_month_info)
        for e_info in temp_info:
            my_dict['con'] = e_info[2]
            my_dict['env'] = e_info[3]
            my_dict['ext'] = e_info[4]
            my_dict['every_info'] = 'month'
            #20200302更新：添加获取下一条的预读
            next_info_index = temp_info.index(e_info)+1
            if len(temp_info) > 1:
                next_info = temp_info[next_info_index]
                my_dict['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            break
    elif every_week_info:
        temp_info = list(every_week_info)
        for e_info in temp_info:
            my_dict['con'] = e_info[2]
            my_dict['env'] = e_info[3]
            my_dict['ext'] = e_info[4]
            my_dict['every_info'] = 'week'
            #20200302更新：添加获取下一条的预读
            next_info_index = temp_info.index(e_info)+1
            if len(temp_info) > 1:
                next_info = temp_info[next_info_index]
                my_dict['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            break
    elif common_info:
        temp_info = list(common_info)
        for e_info in temp_info:
            my_dict['con'] = e_info[2]
            my_dict['env'] = e_info[3]
            my_dict['ext'] = e_info[4]
            my_dict['every_info'] = 'common'
            #20200302更新：添加获取下一条的预读
            next_info_index = temp_info.index(e_info)+1
            if len(temp_info) > 1:
                next_info = temp_info[next_info_index]
                my_dict['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            break
#3、直到，查完事，结束并删除dump文件，生成已复习
    else:
        os.remove('language_voice_diction_english/4web_restudy/every_year_info')
        os.remove('language_voice_diction_english/4web_restudy/every_month_info')
        os.remove('language_voice_diction_english/4web_restudy/every_week_info')
        os.remove('language_voice_diction_english/4web_restudy/common_info')
        write2file('language_voice_diction_english/4web_restudy/已复习', '复习完成')
        return HttpResponseRedirect('/alt1234')
    #测试直接把env置为video标签可行不
    if len(my_dict['env']) < 3:
        my_dict['env'] = '''<br/><video controls preload loop autoplay width="320" height="240" src="/static/grace_voice/TOEFL/2HoursWorship490x360.mp4" type="video/mp4"></video><br/>'''
    #context的'hello'对应模板html的变量{{ hello }}
    return render(request, 'alt3.html', my_dict)
    

def accept_cmd_alt3(request):
    global my_dict
    global common
    global every_week
    global every_month
    global every_year
    global common_info
    global every_year_info
    global every_month_info
    global every_week_info
    request.encoding='utf-8'
    every = request.GET['every']
    cmd = request.GET['cmd']
    print('every:%s, cmd:%s' % (every, cmd))
    #处理前打开数据库连接
    create_database_link()
    ############处理年的##############
    if every == 'year':
        if cmd == '8':
            every_year.delete('Other2',my_dict['ext'])
            every_month.add(Day=getnowtime('d'), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
            common.add(Ymd=getdaystime(1), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
            common.add(Ymd=getdaystime(3), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
            common.add(Ymd=getdaystime(5), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
        elif cmd == '2':
            every_year.delete('Other2',my_dict['ext'])
        every_year_info.pop(0)
        dump2file('language_voice_diction_english/4web_restudy/every_year_info', every_year_info)
    ############处理月的##############
    elif every == 'month':
        if cmd == '8':
            every_month.delete('Other2', my_dict['ext'])
            every_week.add(Day=getnowtime('week'),Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
            common.add(Ymd=getdaystime(1), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
            common.add(Ymd=getdaystime(3), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
            common.add(Ymd=getdaystime(5), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
        elif cmd == '2':
            every_month.delete('Other2', my_dict['ext'])
            every_year.add(MonthDay=getnowtime('md'),Con=my_dict['con'],  Other1=my_dict['env'], Other2=my_dict['ext'])
        every_month_info.pop(0)
        dump2file('language_voice_diction_english/4web_restudy/every_month_info', every_month_info)
    ############处理周的##############
    elif every == 'week':
        if cmd == '8':
            common.add(Ymd=getdaystime(1), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
            common.add(Ymd=getdaystime(3), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
            common.add(Ymd=getdaystime(5), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
        elif cmd == '2':
            every_week.delete('Other2', my_dict['ext'])
            every_month.add(Day=getnowtime('d'), Con=my_dict['con'], Other1=my_dict['env'], Other2=my_dict['ext'])
        every_week_info.pop(0)
        dump2file('language_voice_diction_english/4web_restudy/every_week_info', every_week_info)
    ############处理Common的##############
    elif every == 'common':
        common_info.pop(0)
        dump2file('language_voice_diction_english/4web_restudy/common_info', common_info)
    #处理完后，关闭数据库
    close_database_link()

    return HttpResponseRedirect('/alt3')

def alt3_all_mp3(request):
    global common_info
    global every_year_info
    global every_month_info
    global every_week_info
    global my_dict
    
    #1、未复习且未有dump则查询好，并放到dict中dump
    #   此阶段生成四个info文件，准备用来查询及操作
    if os.path.exists('language_voice_diction_english/4web_restudy/已复习') and not os.path.exists('language_voice_diction_english/4web_restudy/common_info'):
        my_dict['showinfo'] = '本日已复习'
        my_dict['con'] = 't1'
        my_dict['env'] = 't2'
        my_dict['ext'] = 't3'
        return HttpResponseRedirect('/alt1234') #复习完的直接回主页
        #return render(request, 'alt3.html', my_dict)
    elif os.path.exists('language_voice_diction_english/4web_restudy/common_info'):
        every_year_info = loadffile('language_voice_diction_english/4web_restudy/every_year_info')
        every_month_info = loadffile('language_voice_diction_english/4web_restudy/every_month_info')
        every_week_info = loadffile('language_voice_diction_english/4web_restudy/every_week_info')
        common_info = loadffile('language_voice_diction_english/4web_restudy/common_info')

        all_restudy_list = [len(every_year_info), len(every_month_info), len(every_week_info), len(common_info)]
        all_restudy = all_restudy_list[0] +all_restudy_list[1] + all_restudy_list[2] + all_restudy_list[3]

        all_time = all_restudy*16
        all_time_m = int(all_time // 60)
        all_time_s = int(all_time % 60)
        if all_restudy_list[2] + all_restudy_list[1] + all_restudy_list[0]== 0:
            my_dict['showinfo'] = '待复习%s条(%s.%s)，将load继续' % (all_restudy, all_time_m, all_time_s)
        elif all_restudy_list[1] + all_restudy_list[0]== 0:
            my_dict['showinfo'] = '待复习%s(w:%s)条(%s.%s)，将load继续' % (all_restudy, all_restudy_list[2], all_time_m, all_time_s)
        elif all_restudy_list[0] == 0:
            my_dict['showinfo'] = '待复习%s(m:%s,w:%s)条(%s.%s)，将load继续' % (all_restudy, all_restudy_list[1], all_restudy_list[2], all_time_m, all_time_s)
        else:
            my_dict['showinfo'] = '待复习%s(y:%s,m:%s,w:%s)条(%s.%s)，将load继续' % (all_restudy, all_restudy_list[0], all_restudy_list[1], all_restudy_list[2], all_time_m, all_time_s)
    else:
        #day = datetime.now() + timedelta(days=0) + timedelta(hours=8) 
        #原来的复习没问题，这个得到的时间，就比我的时钟慢8个点了，奇怪，一样的过程。。。不懂，加上
        day = datetime.now() + timedelta(days=0)
        #后来查了下django时区问题，在setting里面改了时区为上海，然后，就没事了。。。（现在在韩国改为首尔了）
        week_day = day.strftime('%w')
        month_day = day.strftime('%d')
        ymd = day.strftime('%Y%m%d')
        
        #提前年的，所以，年的单独调出。把这两句复制到py3里，就可以准确演算了
        y_day = datetime.now() + timedelta(days=72)
        monthday = y_day.strftime('%m%d')
        #print('monthday='+monthday)

        create_database_link()
        global common
        global every_week
        global every_month
        global every_year
        every_year_info = every_year.find('MonthDay', monthday)
        dump2file('language_voice_diction_english/4web_restudy/every_year_info', every_year_info)
        every_month_info = every_month.find('Day', month_day)
        dump2file('language_voice_diction_english/4web_restudy/every_month_info', every_month_info)
        every_week_info = every_week.find('Day', week_day)
        dump2file('language_voice_diction_english/4web_restudy/every_week_info', every_week_info)
        common_info = common.find('Ymd', ymd)
        dump2file('language_voice_diction_english/4web_restudy/common_info', common_info)
        close_database_link()
        all_restudy = len(every_year_info)+len(every_month_info)+len(every_week_info)+len(common_info)
        my_dict['showinfo'] = '将开始dump新的%s条复习，时间:%s' % (all_restudy, str(day))
        
#2、每次调用，读取一次dict，并相应accept_cmd修改数据库和dict
    alt3_all_mp3 = []
    alt3_all_text_list = [] 
    if every_year_info:
        temp_info = list(every_year_info)
        for e_info in temp_info:
            #my_dict['con'] = e_info[2]
            #my_dict['env'] = e_info[3]
            #my_dict['ext'] = e_info[4]
            alt3_all_text_list.append(e_info[2])
            alt3_all_text_list.append(e_info[3])
            alt3_all_text_list.append('year')
            alt3_all_text_list.append('\n')
            alt3_all_mp3.append(e_info[4])
            #my_dict['every_info'] = 'year'
            #20200302更新：添加获取下一条的预读
            #next_info_index = temp_info.index(e_info)+1
            #if len(temp_info) > 1:
                #next_info = temp_info[next_info_index]
                #my_dict['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            #break
    if every_month_info:
        temp_info = list(every_month_info)
        for e_info in temp_info:
            #my_dict['con'] = e_info[2]
            #my_dict['env'] = e_info[3]
            #my_dict['ext'] = e_info[4]
            alt3_all_text_list.append(e_info[2])
            alt3_all_text_list.append(e_info[3])
            alt3_all_text_list.append('month')
            alt3_all_text_list.append('\n')
            alt3_all_mp3.append(e_info[4])
            #my_dict['every_info'] = 'month'
            #20200302更新：添加获取下一条的预读
            #next_info_index = temp_info.index(e_info)+1
            #if len(temp_info) > 1:
                #next_info = temp_info[next_info_index]
                #my_dict['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            #break
    if every_week_info:
        temp_info = list(every_week_info)
        for e_info in temp_info:
            #my_dict['con'] = e_info[2]
            #my_dict['env'] = e_info[3]
            #my_dict['ext'] = e_info[4]
            alt3_all_text_list.append(e_info[2])
            alt3_all_text_list.append(e_info[3])
            alt3_all_text_list.append('week')
            alt3_all_text_list.append('\n')
            alt3_all_mp3.append(e_info[4])
            #my_dict['every_info'] = 'week'
            #20200302更新：添加获取下一条的预读
            #next_info_index = temp_info.index(e_info)+1
            #if len(temp_info) > 1:
                #next_info = temp_info[next_info_index]
                #my_dict['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            #break
    if common_info:
        temp_info = list(common_info)
        for e_info in temp_info:
            #my_dict['con'] = e_info[2]
            #my_dict['env'] = e_info[3]
            #my_dict['ext'] = e_info[4]
            alt3_all_text_list.append(e_info[2])
            alt3_all_text_list.append(e_info[3])
            alt3_all_text_list.append('common')
            alt3_all_text_list.append('\n')
            alt3_all_mp3.append(e_info[4])
            #my_dict['every_info'] = 'common'
            #20200302更新：添加获取下一条的预读
            #next_info_index = temp_info.index(e_info)+1
            #if len(temp_info) > 1:
                #next_info = temp_info[next_info_index]
                #my_dict['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            #break
#3、直到，查完事，结束并删除dump文件，生成已复习
    #else:
        #os.remove('language_voice_diction_english/4web_restudy/every_year_info')
        #os.remove('language_voice_diction_english/4web_restudy/every_month_info')
        #os.remove('language_voice_diction_english/4web_restudy/every_week_info')
        #os.remove('language_voice_diction_english/4web_restudy/common_info')
        #write2file('language_voice_diction_english/4web_restudy/已复习', '复习完成')
        #return HttpResponseRedirect('/alt1234')

    #context的'hello'对应模板html的变量{{ hello }}
    #return render(request, 'alt3.html', my_dict)
    alt3_all_text_string = '\n'.join(alt3_all_text_list)
    write2file('alt3_all_text_string', alt3_all_text_string)
    alt3_all_mp3_string = '\n'.join(alt3_all_mp3)
    write2file('alt3_all_mp3_string', alt3_all_mp3_string)

    runsyscmd('bash alt3_all.bash', 'no')

    return HttpResponseRedirect('/static/grace_voice/alt3_all_mp3/alt3_all.zip')
    #/static/grace_voice/alt3_all_mp3.mp3
