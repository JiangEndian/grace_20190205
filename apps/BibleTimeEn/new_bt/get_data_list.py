#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os, sys
import importlib

######################年份制转换#####################
def BCorAD2AA(abcd, year):
    if abcd == 'AD':
        return year+3969
    elif abcd == 'BC':
        return 3970-year
######################年份制转换#####################


#####################把data_py的其他格式转为统一格式##
def data_dict_AD_BC2AA(data_dict):
    #后加的处理事件描述的前后空行###############
    if '\n' in data_dict['story']:
        story = data_dict['story'].split('\n')
    else: #处理只有一行的情况防止story为空时的错误
        story = ['1']
    #print(story)
    if story[0] == '':
        story = story[1:]
        data_dict['story'] = '\n'.join(story)
        if story[-1] == '':
            story = story[:-1]
            data_dict['story'] = '\n'.join(story)
    #后加的处理事件描述的前后空行###############

    #处理年代设定为统一的AA制的start_time和past_time...###
    if 'start_time' in data_dict:
        pass
    elif 'start_time_AD' in data_dict:
        data_dict['start_time'] = BCorAD2AA('AD', data_dict['start_time_AD'])
        if 'pass_time_AD' in data_dict:
            data_dict['pass_time'] = BCorAD2AA('AD', data_dict['pass_time_AD']) - data_dict['start_time']
    elif 'start_time_BC' in data_dict:
        data_dict['start_time'] = BCorAD2AA('BC', data_dict['start_time_BC'])
        if 'pass_time_BC' in data_dict:
            data_dict['pass_time'] = BCorAD2AA('BC', data_dict['pass_time_BC']) - data_dict['start_time']
        elif 'pass_time_AD' in data_dict:
            data_dict['pass_time'] = BCorAD2AA('AD', data_dict['pass_time_AD']) - data_dict['start_time']
    #处理年代设定为统一的AA制的start_time和past_time...###
    
    return data_dict
#####################把data_py的其他格式转为统一格式##
        
data_path = os.path.join(os.path.abspath('.'), 'data_py') #得到data_py文件夹的绝对路径
sys.path.append(data_path) #把此路径加入可导入路径
py_files = [py_file for py_file in os.listdir(data_path) if '.py' in py_file and '.swp' not in py_file] #列出此路径下所有py文件

data_list = [] #存放每个py文件的data_dict
for f in py_files:
    py_file_name = f[:-3]
    data_py = importlib.import_module(py_file_name) #动态导入去掉.py的文件名（模块）
    data_py.data_dict['file_name'] = py_file_name
    data_list.append(data_dict_AD_BC2AA(data_py.data_dict)) #把模块的data_dict处理为标准模式添加进list里


#接收字典，返回其中的start_time键
def func4sort(one_dict): 
    return one_dict['start_time']

#排序字典列表，排序时依func4sort处理过后的值为准，即以start_time的值为准
data_list.sort(key=func4sort)

#for data in data_list:
    #if data['name'] != data['file_name']:
        #print('%s==%s' % (data['name'], data['file_name']))
#
