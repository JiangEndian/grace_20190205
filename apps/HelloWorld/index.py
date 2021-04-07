from django.http import HttpResponseRedirect 
from django.shortcuts import render
from django.http import HttpResponse
import os
from MyPython3 import *

def submitToGithub(request):
    dictOfInfo = {}
    dictOfInfo['justForInfo'] = runsyscmd('cd ../ && ./add_commit_push.bash')
    return render(request, 'justForInfo.html', dictOfInfo)

def index(request):
    restudy_info = {}
    #tasks_part1 = 20
    #tasks_all = 20
    tasks_part1 = 12
    tasks_all = 12
    #给textarea显示的文本文件,以及,提交也是向这个文件
    restudy_info['TextArea'] = readffile('from_net')

    if int(getnowtime('week')) % 2 == 0: #02456
        show_exercise = 'YES'
        all_tasks = tasks_all
    else:
        show_exercise = 'NO' 
        all_tasks = tasks_part1
    restudy_info['show_exercise'] = show_exercise
    restudy_info['all_tasks'] = all_tasks


    #新加生成file_name参数的文件名
    def touch_file(file_name):
        runsyscmd('touch file_name_files/%s' % file_name)

    if request.GET.get('file_name'):
        touch_file(request.GET.get('file_name'))
        if 'exercise' in request.GET.get('file_name'):
            return HttpResponseRedirect('static/exercise.html')
    
    #获取file_name_files文件夹内的文件们
    file_name_list = os.listdir("file_name_files")
    finished = len(file_name_list)
    if finished >= tasks_part1 and show_exercise == 'NO':
        restudy_info['finished_all'] = '√'
        restudy_info['show_life_code'] = 'lifecode'
    elif finished >= tasks_all:
        restudy_info['finished_all'] = '√'
        restudy_info['show_life_code'] = 'lifecode'

    for file_name_one in file_name_list:
        restudy_info[str(file_name_one)] = '√'

    

    #再在返回的字典里附加上已复习的条数
    restudy_info['finished'] = str(finished)

    #这是一开始的alt1234的进度相关的
    restudy_info['alt1'] = '进度中alt1'
    restudy_info['alt1_common'] = 'alt1_common'

    restudy_info['alt2'] = '进度中alt2'
    restudy_info['alt2_common'] = 'alt2_common'

    restudy_info['alt3'] = '进度中alt3'
    restudy_info['alt3_common'] = 'alt3_common'
    restudy_info['alt3_all'] = 'alt3_all'

    restudy_info['worshipAndBible'] = '...'

    restudy_info['alt4'] = '进度中alt4'
    restudy_info['alt4_common'] = 'alt4_common'
    
    #获取plan_endian，并永久保存请求者的IP在文本statics/files/IPList里
    runsyscmd('/home/ed/grace_20190205/apps/plan_endian/cat_tomorrow2plan_info.bash')
    #获取IP
    #ip = '00000000'
    #x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #if x_forwarded_for:
        #ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
    #else:
        #ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP
    #获取IP
    #写入IP并读取之
    #write2fileAppend('statics/files/IPList', ip)
    restudy_info['plan_endian'] = readffile('plan_endian/plan_info') 
    #restudy_info['plan_endian'] = readffile('plan_endian/plan_info') + '\n' + readffile('statics/files/IPList')
    #获取plan_endian，并永久保存请求者的IP在文本statics/files/IPList里

    if os.path.exists('new_gs/4web_restudy/已复习') and not os.path.exists('new_gs/4web_restudy/common_info'):
        restudy_info['alt1'] = 'alt1已复习'
        restudy_info['alt1_common'] = ''
    elif not os.path.exists('new_gs/4web_restudy/common_info'):
        #restudy_info['alt1'] = 'alt1'
        #初始显示信息改为显示锻炼
        restudy_info['alt1'] = '膝盖自由落体摆动3分钟. '

        restudy_info['alt1_common'] = ''

    if os.path.exists('language_voice_diction_korean/4web_restudy/已复习') and not os.path.exists('language_voice_diction_korean/4web_restudy/common_info'):
        restudy_info['alt2'] = 'alt2已复习'
        restudy_info['alt2_common'] = ''
    elif not os.path.exists('language_voice_diction_korean/4web_restudy/common_info'):
        #restudy_info['alt2'] = 'alt2'
        #初始显示信息改为显示锻炼
        restudy_info['alt2'] = '身体侧屈看同侧脚。15*3. '

        restudy_info['alt2_common'] = ''

    if os.path.exists('language_voice_diction_english/4web_restudy/已复习') and not os.path.exists('language_voice_diction_english/4web_restudy/common_info'):
        restudy_info['alt3'] = 'alt3已复习'
        restudy_info['alt3_common'] = ''
        restudy_info['alt3_all'] = ''
    elif not os.path.exists('language_voice_diction_english/4web_restudy/common_info'):
        #restudy_info['alt3'] = 'alt3'
        #初始显示信息改为显示锻炼
        restudy_info['alt3'] = '1.撑抬起上身趴下，15*3. 2.身体左右翻转感受脊柱一节节旋转，3-5分钟。'

        restudy_info['alt3_common'] = ''
        restudy_info['alt3_all'] = ''
    
    if os.path.exists('WorshipAndBible/4web_restudy/已复习') and not os.path.exists('WorshipAndBible/4web_restudy/common_info'):
        restudy_info['worshipAndBible'] = '!!!'
    elif not os.path.exists('WorshipAndBible/4web_restudy/common_info'):
        restudy_info['worshipAndBible'] = '???'

    if os.path.exists('language_voice_diction_hebrew/4web_restudy/已复习') and not os.path.exists('language_voice_diction_hebrew/4web_restudy/common_info'):
        restudy_info['alt4'] = 'alt4已复习'
        restudy_info['alt4_common'] = ''
    elif not os.path.exists('language_voice_diction_hebrew/4web_restudy/common_info'):
        #restudy_info['alt4'] = 'alt4'
        #初始显示信息改为显示锻炼
        restudy_info['alt4'] = '小腿垂直床_腰腿一线3min*3. '
        restudy_info['alt4_common'] = ''
    
    #restudy_info['alt1_common'] = ''
    #restudy_info['alt2_common'] = ''
    #restudy_info['alt3_common'] = ''
    #restudy_info['alt4_common'] = ''
    return render(request, 'index.html', restudy_info)


    
