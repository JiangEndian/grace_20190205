from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import os
from MyPython3 import *
import re

def worshipAndBible(request):
    TextAndAudio = {}
    MonthDay = getnowtime('md')
    FileNameOfAudioAndText = 'WorshipAndBible/'+MonthDay

    ReplaceInfo = re.compile('<.*?>')
    ReplaceInfoNumber = re.compile('\[.*?\]')
    ReplaceInfoSpecial = re.compile('[ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ]')
    TextAndAudio['TranscriptOfAudio'] = ReplaceInfoNumber.sub('', ReplaceInfoSpecial.sub('', ReplaceInfo.sub('', readffile(FileNameOfAudioAndText)))).replace('\n', '\n\n') #把一些<>控制的格式去掉，又把单回车换成双回车
    TextAndAudio['FileOfAudio'] = FileNameOfAudioAndText + '.mp3'


    return render(request, 'worshipAndBible.html', TextAndAudio)

def uploadAudio(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFiles =request.FILES.getlist("myfiles", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFiles:
            return HttpResponse("no files for upload!")
        for oneFile in myFiles:
            FilePath = "./statics/grace_voice/WorshipAndBible/" + oneFile.name
            if os.path.exists(FilePath):
                destination = open("./statics/grace_voice/WorshipAndBible/" + oneFile.name + 'NeedToBeCompressed', 'wb+')    # 打开特定的文件进行二进制的写操作
                for chunk in oneFile.chunks():      # 分块写入文件
                    destination.write(chunk)
                destination.close()
                #现在不用compress了，改mp3wrap了，09:16
                SysCmdForCompressManyMp3ToOne = 'cd ~/grace_voice_file/WorshipAndBible/ && mp3wrap new.mp3 %s %sNeedToBeCompressed && rm %s && rm %sNeedToBeCompressed && mv new*.mp3 %s && mp3val %s -f-nb' % (oneFile.name, oneFile.name, oneFile.name, oneFile.name, oneFile.name, oneFile.name)
                runsyscmd(SysCmdForCompressManyMp3ToOne, 'no')
            else:
                destination = open("./statics/grace_voice/WorshipAndBible/" + oneFile.name, 'wb+')    # 打开特定的文件进行二进制的写操作
                for chunk in oneFile.chunks():      # 分块写入文件
                    destination.write(chunk)
                destination.close()
        return HttpResponseRedirect('/worshipAndBible')

def submitTranscript(request):
    MonthDay = request.POST.get('MonthDay', 'NULL') 
    FileNameOfAudioAndText = 'WorshipAndBible/'+MonthDay
    Text = request.POST.get('Transcript', 'NULL')

    write2fileAppend(FileNameOfAudioAndText, Text)
    return HttpResponseRedirect('/worshipAndBible')
