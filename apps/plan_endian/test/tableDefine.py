#!/usr/bin/env python3

from MyPython3 import *

##################四张表定义#####################
tableCommon = OrderedDict()
tableCommon['ID'] = PrimaryField('id')
tableCommon['Ymd'] = StringField('ymd') #日期
tableCommon['Con'] = StringField('content') #计划内容
tableCommon['Other1'] = StringField('other1')
tableCommon['Other2'] = StringField('other2')
tableCommon['other3'] = StringField('other3')
############################
tableEveryWeek = OrderedDict()
tableEveryWeek['ID'] = PrimaryField('id')
tableEveryWeek['Day'] = StringField('day') #星期几
tableEveryWeek['Con'] = StringField('content') #计划内容
tableEveryWeek['Other1'] = StringField('other1')
tableEveryWeek['Other2'] = StringField('other2')
tableEveryWeek['other3'] = StringField('other3')
############################
tableEveryMonth = OrderedDict()
tableEveryMonth['ID'] = PrimaryField('id')
tableEveryMonth['Day'] = StringField('day') #几号
tableEveryMonth['Con'] = StringField('content') #计划内容
tableEveryMonth['Other1'] = StringField('other1')
tableEveryMonth['Other2'] = StringField('other2')
tableEveryMonth['other3'] = StringField('other3')
############################
tableEveryYear = OrderedDict()
tableEveryYear['ID'] = PrimaryField('id')
tableEveryYear['MonthDay'] = StringField('monthday') #几月几日
tableEveryYear['Con'] = StringField('content') #计划内容
tableEveryYear['Other1'] = StringField('other1')
tableEveryYear['Other2'] = StringField('other2')
tableEveryYear['other3'] = StringField('other3')
##################四张表定义#####################


##################删除昨天的计划#################
def yesterday(common):
    ystday = getdaystime(-1)
    #print(ystday)
    #print(common.find('Ymd', ystday))
    common.delete('Ymd', ystday)
##################删除昨天的计划#################



##################增加显示每日计划#####################
if sys.argv[0] in ['./endiantoday.py', './tomorrowplan.py', './nextmonthplan.py']:
    print('\t%s' % sys.argv[0])
    print('___________________________\n')

    ##这个是计算该读哪一章箴言/传道书了
    now = datetime.now()
    if sys.argv[0] == './endiantoday.py':
        todayday = int(now.strftime('%d'))
    elif sys.argv[0] == './tomorrowplan.py':
        todayday = int((now+timedelta(days=1)).strftime('%d'))
    else:
        todayday = 365
    print('잠언%d' % todayday)
    print('전도서%d' % (12 if todayday % 12 == 0 else todayday % 12))

    ##这个是打印文件里面的列表的
    everyday = readffile('everydaytodolist.txt')
    print(everyday.strip())

    print('___________________________\n')

