#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_data_list import data_list
from newestMyPython3 import write2file

global sy
sy = 30
global by
by = 3*sy


#######################年份制转换##################
def AA2BCorAD(aa):
    if aa <= 3970: #3968年都属于BC
        return '%dBC' % (3970-aa)
    else:
        return 'AD%d' % (aa-3969)
#######################年份制转换##################
   

#######################画图画字#####################
global font
font = '20px 微软雅黑'
if False: #为折叠帮助的。。。
    pass
    #fillText(String text,float x,float y,[float maxwidth]):填充字符串
    #strokeText(String text,float x,float y,[float maxwidth])：绘制边框
    #font="bold 45px宋体"
    #textAlign：设置绘制字符串的水平对齐方式,start|end|right|center
    #textBaseAlign：垂直对齐方式：top|hanging|middle|alphabetic|bottom
    pass
def print_one_rect(data, color):
    global by
    global sy
    global font

    start_t = data['start_time']
    pass_t = data['pass_time']

    end_t = start_t + pass_t
    start_bcad = AA2BCorAD(start_t)
    end_bcad = AA2BCorAD(end_t)

    name = data['name']
    story = data['story']

    #nsy = (story.count('\n')+2) * sy
    
    #画出矩形来
    print('cxt.fillStyle=\"%s\";' % color)
    print('cxt.fillRect(%s,%s,%s,%s)' % (start_t, by, pass_t, sy))

    #写出标题和内容的字
    print(r'cxt.fillStyle = "#000000";') #先更换填充色
    print('cxt.font = \"%s\";' % font)
    title = 'AA%d-AA%d  %s  %s-%s' % (start_t, end_t, name, start_bcad, end_bcad)
    print('cxt.fillText(\"%s\", %s, %s)' % (title, start_t, by+sy/1.5))
    by += sy
    #写内容的
    #for one in data['story'].split('\n'):
        #print('cxt.fillText(\"%s\", %s, %s)' % (one, data['start_time'], by+sy/1.5))
        #by += sy #纵坐标前进
#######################画图画字#####################


color1 = '#00FFFF'
color2 = '#FF55FF'
color3 = '#00FF00'#闪绿色
color4 = '#FFaaaa'


flag = True
#根据数据画图
RainbowColor = ['#FF0000', '#FF7F00', '#FFFF00','#00FF00','#0000FF','#4B0082','#9400D3']
global times
times = 0
for data in data_list:
    color = RainbowColor[times%7]
    times += 1
    other = ''
    #if data['name'] == '耶稣': #把色彩换成彩虹。
        #color = color3
    #elif flag:
        #color = color1
        #flag = not flag
    #else:
        #color = color2
        #flag = not flag
    #画出矩形并写字
    print_one_rect(data, color)


##########################画刻度线#####################
#画上线
print('cxt.moveTo(0,%s);' % str(2*sy))
print('cxt.lineTo(7700,%s);' % str(2*sy))
print('cxt.stroke();')
#画上线标尺
for ix in [i*100 for i in range(77)]:
    print('cxt.moveTo(%s, %s);' % (str(ix), str(2*sy)))
    print('cxt.lineTo(%s, %s);' % (str(ix), str(sy*2.5)))
    print('cxt.stroke();')
    print(r'cxt.fillStyle = "#000";')
    print('cxt.font = \"%s\";' % font)
    print('cxt.fillText(\"%s\", %s, %s)' % (AA2BCorAD(ix), str(ix), sy))
    print('cxt.fillText(\"%s\", %s, %s)' % ('AA%s' % ix, str(ix), 1.7*sy))
#画下线
by += sy
print('cxt.moveTo(0,%s);' % str(by))
print('cxt.lineTo(7700,%s);' % str(by))
print('cxt.stroke();')
#画下线标尺
for ix in [i*100 for i in range(77)]:
    print('cxt.moveTo(%s, %s);' % (str(ix), str(by)))
    print('cxt.lineTo(%s, %s);' % (str(ix), str(by-sy/2)))
    print('cxt.stroke();')
    print(r'cxt.fillStyle = "#000";')
    print('cxt.font = \"%s\";' % font)
    print('cxt.fillText(\"%s\", %s, %s)' % ('AA%s' % ix, str(ix), by+0.7*sy))
    print('cxt.fillText(\"%s\", %s, %s)' % (AA2BCorAD(ix), str(ix), by+1.5*sy))
##########################画刻度线#####################
by += sy #最后canvas的高度再调整下
##########################最后根据调度重新调整canvas的高度
HTML_TEMP='''<!DOCTYPE HTML>
<html>
<body>
<canvas id="myCanvas" width="7700" height="%d" style="border:1px solid #c3c3c3;">
Your browser does not support the canvas element.
</canvas>
<script type="text/javascript">
var c=document.getElementById("myCanvas");
var cxt=c.getContext("2d");''' % (by+sy)
write2file('temp.html', HTML_TEMP) #调整后写入第一部分文件
##########################最后根据调度重新调整canvas的高度


