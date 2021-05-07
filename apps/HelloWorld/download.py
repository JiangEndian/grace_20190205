from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import os
from MyPython3 import *
from configurations import *

def download(request):
    file_list = os.listdir("statics/files")
    file_list.sort()
    file_dict = {'file_list':file_list}

    #尝试加个控制页面，设置显示删除与否
    Configurations = readConfigurations('Configurations')
    file_dict['Delete']= Configurations['Delete']

    file_dict['TextArea'] = readffile('from_net')
    return render(request, 'download.html', file_dict)

def deleteFile(request):
    #runsyscmd('mv statics/files/%s /home/ed/DeletedFiles/' % request.GET.get('FileName').replace(' ', '\ ')) #不知道为什么，我9点多起来，6点半左右删了好几个文件。。。
    runsyscmd('date >> /home/ed/DeletedFiles/RecordsOfFileOperation; echo %s >> /home/ed/DeletedFiles/RecordsOfFileOperation; echo >> /home/ed/DeletedFiles/RecordsOfFileOperation' % request.GET.get('FileName').replace(' ', '\ '))
    #file_list = os.listdir("statics/files")
    #file_dict = {'file_list':file_list}
    #return render(request, 'download.html', file_dict) 
    #above one will keep the link with commands, 
    return HttpResponseRedirect('/alt')

def video_view(request):
    file_list = []
    for file_one in os.listdir("statics/files"):
        file_name_splited = os.path.splitext(file_one)
        if len(file_name_splited) > 1:
            if file_name_splited[1] == '.mp4':
                file_list.append(file_one)
    file_dict = {'file_list':file_list}
    return render(request, 'video_view.html', file_dict)


#试着返回JSON数据。为了以后如果扩展可以直接获取数据准备
def video_name(request):
    file_list = []
    for file_one in os.listdir("statics/files"):
        file_name_splited = os.path.splitext(file_one)
        if len(file_name_splited) > 1:
            if file_name_splited[1] == '.mp4':
                file_list.append(file_one)
    file_dict = {'file_list':file_list}
    return JsonResponse(data=file_dict)
    #return render(request, 'video_view.html', file_dict)

def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFiles =request.FILES.getlist("myfiles", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFiles:
            return HttpResponse("no files for upload!")
        for oneFile in myFiles:
            destination = open("./statics/files/" + oneFile.name, 'wb+')    # 打开特定的文件进行二进制的写操作
            for chunk in oneFile.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()
        return HttpResponseRedirect('/alt')


