#!/usr/bin/env python3

from aip import AipSpeech
from MyPython3 import *

""" 你的 APPID AK SK """
APP_ID = '15480868'
API_KEY = '2QT7r6p9H8PKCdzpL14mm2xD'
SECRET_KEY = 'LzGuG24eXu2qvsqiAQGGT9zhHHwkR8Iw'
 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#新库吧。换新库吧。同时，处理数据时，加上当时的时间秒数，来作为文件名，一个一个的处理，有错误时再看。读取的时候，就那样放一遍意思下，有就有，没就没。。。拉倒吧。。。
#得弄个自动切割的，来合成完整的一段话。。。嗯，先从bt开始吧，合成语音，附上去。
#1、判断文本字数并分割文本
#2、按文本提交得到数个result
#3、每个result都不为dict，才可一起写入

#分割文本为指定大小以内的文本列表
def texts2text_list(texts):
    texts_list = list(texts)
    numbers = 0
    text_list = []
    text_one = ''
    for char in texts_list:
        text_one = text_one + char
        numbers += 1
        if numbers >= 500:
            text_list.append(text_one)
            text_one = ''
            numbers = 0
    if text_one:
        text_list.append(text_one)
    return text_list

#转换一个文本到语音
def text2voice(text, per=4, spd=5):
    result  = client.synthesis(text, 'zh', 1, {
    'vol': 15, #音量0-15
    'per':per, #发音人0女,1男,3情感男,4情感女
    'spd':spd #语速0-9
    })
    return result
#转换文本列表到语音列表
def voice2voice_list(text_list, **kw):
    voice_list = []
    for text in text_list:
        voice_list.append(text2voice(text,**kw))
    return voice_list
 
#转换语音列表为一个语音文件
def voice_list2voice_file(voice_list, file_name):
    for voice in voice_list:
        if isinstance(voice, dict):
            print('%s有错误，回车跳过此条转换继续。' % file_name)
            input()
            return 0
    with open(file_name, 'ab') as f: #二进制打开用于追加
        for voice in voice_list:
            f.write(voice)

#终极合成_任意长文本转到一个语音文件
def texts2voice_file(texts, file_name, **kw):
    text_list = texts2text_list(texts)
    voice_list = voice2voice_list(text_list, **kw)
    voice_list2voice_file(voice_list, file_name)
    

now = datetime.now()

year = now.strftime('%Y')
month = now.strftime('%m')
day = now.strftime('%d')
week = now.strftime('%w')
if str(week) == '0':
    week = '日'

texts_date = '今天是%s年%s月%s日周%s。' % (year, month, day, week)

texts1 = '早上好，江飞，该起床了。'

file_name = '早安.mp3'

CMD = 'rm %s' % file_name
runsyscmd(CMD)

def spd_0123_texts_voice(texts, file_name, texts_date):
    texts2voice_file(texts, file_name, spd=0)
    texts2voice_file(texts, file_name, spd=0)
    texts2voice_file(texts, file_name, spd=0)
    texts2voice_file(texts, file_name, spd=1)
    texts2voice_file(texts, file_name, spd=1)
    texts2voice_file(texts_date, file_name, spd=2)
    texts2voice_file(texts, file_name, spd=2)
    texts2voice_file(texts_date, file_name, spd=2)
    texts2voice_file(texts, file_name, spd=3)
    texts2voice_file(texts_date, file_name, spd=3)


spd_0123_texts_voice(texts1, file_name, texts_date)
cvlc_play_mp3(file_name)

