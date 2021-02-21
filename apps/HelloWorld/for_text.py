from django.http import HttpResponseRedirect 
from django.shortcuts import render

from tableDefine import * #导入自定义的东西


def accept_text(request):
    text = request.GET['text'] 
    runsyscmd('echo %s >> from_net' % text)
    return HttpResponseRedirect('/alt')

