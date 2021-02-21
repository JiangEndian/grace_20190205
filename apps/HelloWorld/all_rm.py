from tableDefine import * #导入自定义的东西
from django.http import HttpResponseRedirect 
from django.shortcuts import render

def all_rm(request):
    runsyscmd('rm new_gs/4web_restudy/*')
    runsyscmd('rm language_voice_diction_english/4web_restudy/*')
    runsyscmd('rm language_voice_diction_hebrew/4web_restudy/*')
    runsyscmd('rm language_voice_diction_korean/4web_restudy/*')

    runsyscmd('rm file_name_files/*') #加上删除所有已完成的记录,20201207,22:51

    return HttpResponseRedirect('/alt1234')

def life_code(request):
    return render(request, 'life_code.html')


