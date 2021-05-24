#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#妈呀，我以前怎么设计的啊，太吊了！！！现在我完全看不懂。。。狗屎。。。20191209

from data4bibletime import *
import tkinter as tk
from tkinter import *
from newestMyPython3 import *
global voice_name_list
voice_name_list = []

def init(x=1):
    #字体设置
    global ft
    #ft = getfont(fontsize=130)
    ft = getfont('WenQuanYi Micro Hei Mono',fontsize=180*x)
    #ft = getfont(fontsize=150)
    #fto = getfont(fontsize=150)
    global fto
    fto = ft
    #print('ft=',ft)
    
    #canvas的长和宽设定
    global cx
    cx = 7000
    global cy
    cy = 4000
    #纵屏截图，拼图，分割。。。
    
    #Y轴的步子
    global sy
    sy = 45
    #print('sy=',sy)
    #开始位置及时间AA,BC的设定
    global bx
    bx = 0
    global by
    by = sy
    global bAA
    bAA = 1
    global bBC
    bBC = 3969
    
    #画面X轴和Y轴的缩放系数
    global kx
    kx = 1*x
    #print('kx=',kx)
    global ky
    ky = 1*x
    #print('ky=',ky)
    
    #输出成文本
    global alldata
    alldata = ''
    
    #详细输出指定年限的信息
    global restudy_year
    global bx4line
    #restudy_year=(2000, 2500)
    now_day = int(getnowtime()[6:])
    restudy_year=((now_day-1)*200,now_day*200)
    #print(restudy_year)
    #exit()
    #restudy_year=(2000, 2500)
    bx = -restudy_year[0]+350
    bx4line = bx
    by = sy/2 + by#画完标尺，下移图画.现在标尺最后画了，所以直接前移了
    #by -= (restudy_year[0]/5)


#canvase开始画画,没有明确纪年的，推算的时间的。如族长时代们～
def cr(cvst, who, whenson, age, color, other='空白'):
    color_font = color
    global ft
    global cy
    global bx
    global by
    global bAA
    global bBC
    global kx
    global ky
    global alldata
    global restudy_year
    global voice_name_list
    def bAD(after=0):#通过BC计算AD
        global bBC
        return 1-(bBC-after) #bBC为1时，bAD为0,选用BC。bBC为0及以后，bAD为1及更大，先用bAD

    def colorto(color1):#切换字色
        #如果color1为'hide',则显示为灰色
        if color1 == 'hide':
            return '#aaaaaa'
        #效果不好，直接都用黑色吧
        return 'black'
        if color1 == '#00FFFF':
            return '#FF0000'
        elif color1 == '#FFFF00':
            return '#0000FF'
        elif color1 == '#00FF00':
            return '#FF00FF'
        elif color1 == '#FFFFFF':
            return color1
        else:
            return 'black'

    #if bAA == 1:#刚开始时画标尺
    if False:#刚开始时画标尺
        cvst.create_line(bx,(sy/2)*ky,cx*kx,(sy/2)*ky,fill='black')#上线
        cvst.create_line(bx,(cy-sy/2)*ky,cx*kx,(cy-sy/2)*ky,fill='black')#下线
        for ix in [i*100 for i in range(int(cx/100))]:
            ix += bx
            cvst.create_line(ix*kx,(sy/4)*ky,ix*kx,sy*0.5*ky,fill='black')#上线标尺
            cvst.create_text(ix*kx,sy*0.85*ky,text='AA' + str(ix-bx),font=ft,fill='black')
            if ix-bx<3970:
                cvst.create_text(ix*kx,sy*ky+sy/4,text='BC'+str(3970-ix+bx),font=ft,fill='black')
            elif ix-bx>3970:
                cvst.create_text(ix*kx,sy*ky+sy/4,text='AD'+str(ix-3969-bx),font=ft,fill='black')
            cvst.create_line(ix*kx,(cy-sy/4)*ky,ix*kx,(cy-sy*0.5)*ky,fill='black')#下线标尺
            cvst.create_text(ix*kx,(cy-sy*0.9)*ky,text='AA' + str(ix-bx),font=ft,fill='black')
            if ix-bx<3970:
                cvst.create_text(ix*kx,(cy-sy)*ky-sy/4,text='BC'+str(3970-ix+bx),font=ft,fill='black')
            elif ix-bx>3970:
                cvst.create_text(ix*kx,(cy-sy)*ky-sy/4,text='AD'+str(ix-3969-bx),font=ft,fill='black')
        by = sy/2 + by#画完标尺，下移图画

    #AD1年为AA3970年，那么，BC1年，为AA3969年（AA:AfterAdam)
    if whenson == 0:
        msgt1 = 'AA%d-AA%d年  事件:%s  持续:%d年' % (bAA,bAA+age, who, age)
    else:
        msgt1 = 'AA%d-AA%d年  事件:%s  持续:%d年' % (bAA,bAA+age, who, age)
        #msgt1 = 'AA%d-AA%d年  事件:%s  交任:%d年  持续:%d年' % (bAA,bAA+age, who, whenson, age)
    time_ad_bc='' 
    if bBC > bAD() and (bBC-age) > bAD(age):#生死都在公元前。bBC不能=bAD()。bAD=1-bBC，不相等
        if len(other) < 16:
            msgt2 = 'BC%d-BC%d年 %s' % (bBC,bBC-age, other)
        else:
            msgt2 = 'BC%d-BC%d年\n%s' % (bBC,bBC-age, other)
    elif bBC < bAD():#生于公元后 #BC0年时，已算为AD1年
        if len(other) < 16:
            msgt2 = 'AD%d-AD%d年 %s' % (bAD(),bAD(age), other)
        else:
            msgt2 = 'AD%d-AD%d年\n%s' % (bAD(),bAD(age), other)
    else:#生于公元前，但死于公元后
        if len(other) < 16:
            msgt2 = 'BC%d-AD%d年 %s' % (bBC,bAD(age), other)
        else:
            msgt2 = 'BC%d-AD%d年\n%s' % (bBC,bAD(age), other)
    #满足条件的给简化掉
    msgt = msgt1 + '  ' + msgt2
    msgt = msgt.split('\n')[0].split('  ')[1].split(':')[1]

    #if bAA<restudy_year[0] or bAA>restudy_year[1]:
        #if bAA>(restudy_year[0]-200) and (bAA<restudy_year[1]+200):
            #color_font = 'hide'
        #else:
            #msgt = msgt.split('\n')[0].split('  ')[1].split(':')[1]
    #else:
        #voice_name_list.append('/home/ed/grace_voice_file/voice4bt_data/'+who+'.mp3')
        #cvlc_play_mp3('/home/ed/grace_voice_file/voice4bt_data/'+who+'.mp3')

##输出至文本
    #alldata = alldata + msgt1 + '\n' + other + '\n\n'
    #alldata += msgt1 + '  ' + msgt2 + '\n\n'

    #满足条件，隐藏一些条的文字
    #if age == 480 or age == 430:
    if False:
        msgt = ''

    #计算新的高度nsy
    nsy = (msgt.count('\n')+1) * sy / 2 
    
    #重新设定msgt使标题居中
    if msgt.count('\n') > 0:
        newmsgt = msgt.split('\n')
        spacenum = len(newmsgt[1]) - len(newmsgt[0])
        for i in range(spacenum):
            msgt = ' ' + msgt

    #if by + nsy > cy - sy*1.5:#如果y轴画过了，重新回到sy*1.5开始画
        #by = sy * 1.5
    #画矩形，开始位置，长宽，填充,然后在末处画一条纵线,纵线提前画了
    #cvst.create_line((bx+age)*kx, sy/2*ky, (bx+age)*kx, by*ky, fill=color)
    cvst.create_rectangle(bx*kx, by*ky, (bx+age)*kx, (by+nsy)*ky, fill=color, outline=color)
    cvst.pack()

    #显示这些信息，个别调整一些X的位置，以便文字显示不重叠
    #if who in ['亚伯兰', '亚伯兰99', '以撒']:
        #cvst.create_text((bx+age/2-200)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    if True:
        #cvst.create_text((bx+age/2)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill=colorto(color))
        cvst.create_text((bx)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill=colorto(color_font))
    elif who in ['雅各', '约瑟', '以色列在埃及']:
        cvst.create_text((bx+age/2-260)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['摩西', '旷野', '约书亚81?']:
        cvst.create_text((bx+age/2-130)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['27年元老死？']:
        cvst.create_text((bx+age/2-130)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['士师记？', '100年撒母耳？']:
        cvst.create_text((bx+age/2-180)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['扫罗40', '大卫']:
        cvst.create_text((bx+age/2-60)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['尼希米']:
        cvst.create_text((bx+age/2+200)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['希腊']:
        cvst.create_text((bx+age/2+150)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['托勒密王朝', '塞硫西王朝', '马喀比革命', '哈斯摩尼王朝']:
        cvst.create_text((bx+age/2+200)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['罗马', '以东人希律', '耶稣']:
        cvst.create_text((bx+age/2+50)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    elif who in ['巡抚', '耶路撒冷沦陷', '动乱与镇压']:
        cvst.create_text((bx+age/2+200)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    else:
        cvst.create_text((bx+age/2)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')

    #开始位置和时间前进喽
    bx += whenson
    by += nsy
    bAA += whenson
    bBC -= whenson

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.root = master
        # self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        #self.state = False
        self.state = True#初始全屏了
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.root.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.root.attributes("-fullscreen", False)
        return "break"
bibletime = tk.Tk()
#bibletime.attributes('-fullscreen', True)#就是这个全屏的
FullScreenApp(bibletime)
bibletime.attributes('-fullscreen', True)#就是这个全屏的
bibletime.title('BibleTime...')
#一个Y轴滚动条
#scrollbary = Scrollbar(bibletime)
#scrollbary.set(0.5,1)
#scrollbary.pack(side=RIGHT)
#一个X轴滚动条
#scrollbarx = Scrollbar(bibletime, orient=HORIZONTAL)
#scrollbarx.set(0.5,1)
#scrollbarx.pack(side=RIGHT)

#一个测试方法
#测试结果：调用方法传入*args:('0.0', '1.0)，两个都是
def testx(*args, **kw):
    print('x_args:', args)
    print('x_kw:', kw)
def testy(*args, **kw):
    print('y_args:', args)
    print('y_kw:', kw)

#把这个东西设置好同时绑定到滚动条上
#cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=scrollbarx, yscrollcommand=scrollbary)#不加set,mint好使...
#cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=testx, yscrollcommand=testy)#不加set,mint好使...

#开始时可调整放大倍数。不输入默认为1（原来不输入导致错误20191209）
if getcmdargs():
    init(float(getcmdargs()[0]))
else:
    init(1)

cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white')#不加set,mint好使...
cvs.pack()

#在年的开头结尾画根线（话说，这是什么狗屎。。。完全看不懂了。。。20191209周一）
now_day = int(getnowtime()[6:])
cvs.create_line(350, 0, 350, 7000, fill='black')
cvs.create_line(550, 0, 550, 7000, fill='black')

rundata(cr, cvs)
def cup(*args, **kw):
    global cvs
    cvs.yview('scroll', '-1', 'units')
def cdown(*args, **kw):
    global cvs
    cvs.yview('scroll', '1', 'units')
def cleft(*args, **kw):
    global cvs
    cvs.xview('scroll', '-1', 'units')
def cright(*args, **kw):
    global cvs
    cvs.xview('scroll', '1', 'units')
global screenx
screenx = 1
def small(*args, **kw):
    global screenx
    screenx -= 0.1
    init(screenx)
    rundata(cr,cvs)
def large(*args, **kw):
    global screenx
    screenx += 0.1
    init(screenx)
    rundata(cr,cvs)
bibletime.bind('<Up>', cup) #窗体绑定按键与方法
bibletime.bind('<Down>', cdown)
bibletime.bind('<Left>', cleft)
bibletime.bind('<Right>', cright)
#bibletime.bind('<minus>', small)
#bibletime.bind('<equal>', large)

#一个测试方法
#测试结果：调用方法传入参数('scroll', '1/-1', 'units')
#再测试，是只要这样就行了呢。。。我再试试。。。
def testx(*args, **kw):
    cvs.xview('scroll', '1', 'units')#行，好使
    #print('xs_args:', args)
    #print('xs_kw:', kw)
def testy(*args, **kw):
    print('ys_args:', args)
    print('ys_kw:', kw)
#对滚动条进行配置，滚动时触发什么
#scrollbarx.config(command=cvs.xview)
#scrollbary.config(command=cvs.yview)
#scrollbarx.config(command=testx)
#scrollbary.config(command=testy)


#import data4bibletime
#cr(cvs, '事件', 交任, 持续, 'color', '大事记')
by += 1.5*sy
if True:#刚开始时画标尺
    cvs.create_line(bx4line,(sy/2)*ky,cx*kx,(sy/2)*ky,fill='black')#上线
    cvs.create_line(bx4line,(by-sy/2)*ky,cx*kx,(by-sy/2)*ky,fill='black')#下线
    for ix in [i*100 for i in range(int(cx/100))]:
        ix += bx4line
        cvs.create_line(ix*kx,(sy/4)*ky,ix*kx,sy*0.5*ky,fill='black')#上线标尺
        cvs.create_text(ix*kx,sy*0.85*ky,text='AA' + str(ix-bx4line),font=ft,fill='black')
        if ix-bx4line<3970:
            cvs.create_text(ix*kx,sy*ky+sy/4,text='BC'+str(3970-ix+bx4line),font=ft,fill='black')
        elif ix-bx4line>3970:
            cvs.create_text(ix*kx,sy*ky+sy/4,text='AD'+str(ix-3969-bx4line),font=ft,fill='black')
        cvs.create_line(ix*kx,(by-sy/4)*ky,ix*kx,(by-sy*0.5)*ky,fill='black')#下线标尺
        cvs.create_text(ix*kx,(by-sy*0.9)*ky,text='AA' + str(ix-bx4line),font=ft,fill='black')
        if ix-bx4line<3970:
            cvs.create_text(ix*kx,(by-sy)*ky-sy/4,text='BC'+str(3970-ix+bx4line),font=ft,fill='black')
        elif ix-bx4line>3970:
            cvs.create_text(ix*kx,(by-sy)*ky-sy/4,text='AD'+str(ix-3969-bx4line),font=ft,fill='black')
        #by = sy/2 + by#画完标尺，下移图画

#if restudy_year[0]>=1000 and restudy_year[1]<=1500:
if False:
    temp18 = '约伯记： 七子三女 七千羊 三千骆驼 五百对牛 五百母驴 许多仆婢 至大 儿按日筵 请姐妹来 筵过父命 清早献祭 常行 有一天 神子侍立 撒旦其中 神问何来 走来走去 往返而来 神夸约伯 撒旦控告 神允限制 撒旦退去 有一天 儿筵日 畜死儿亡 撕衣剃头 伏地下拜 <赤来赤回 神赏神收 神名当颂> 不以神愚 不妄评神 又一天 如前 再夸 再控告 存命命 撒旦退去 击打约伯 脚掌至头顶 毒疮 炉灰中坐 瓦片刮身 妻言伯责 神福神祸 三友来 七日默坐 约伯咒生 愿未生 切望死 以利法责 约伯诉苦 求死 责友 厌命 比勒达责 诉理 伯答真知 奈人无奈 诉神权 人怎言 只恳求 琐法责 约伯说 责友 炉灰箴言 淤泥坚垒 诉求神 以利法责 诉理 伯言 安慰 愁烦 换位之言 诉苦 比勒达责 伯责友责 诉己悲 琐法责 伯说 恶盛为何 以利法责 捏造攻伯 伯诉苦 求见神诉 比勒达责 伯责友 诉苦 智慧之言* 愿如前 诉现惨 证正求听 三人不再答 以利户怒* 责答说 又说 又说 又说 旋风中答 权能之问 创造之问 与神辨者 可回答吧 承认卑贱 不再说 旋风中答 你岂有能 岂能自救 河马鳄鱼 神不欠人 见神恶己 尘灰懊恼 神怒三人 三人献祭 约伯祈祷 神悦纳他 苦境转回 赏赐加倍 畜×2 人来安慰 送银金 七子三女 女得产业 见四代 日满而死'
    cvs.create_text(350, 500, text=strdef(temp18.split()), font=fto, fill='black')

mystring1 = '这东西，真心是不值得跟别人讲的，别显自己恶心神。好好讲些圣经话造就人。要说：距离亚当被逐6000年将到，距离基督复活升天2000年将到，差遣约相同。'
#输出全部文本
#alldata = temp18 + '\n\n' + alldata + '\n\n' + mystring1
#write2file('alldata.txt', alldata)
while False:
    cvs.xview('scroll', '1', 'units')#好使，好，UDP传按键

##UDP传按键过来。因为检测按键的是py2的应用。。。
#import socket
#import threading

#socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#socket_server.bind(('127.0.0.1', 9876))

#print('Bind UDP on 9876...')

def udp_receive(socket_server):
    while True:
        data, addr = socket_server.recvfrom(1024)
        command = data.decode('utf-8')
        #print(command)
        if command == 'Up':
            cvs.yview('scroll', '-1', 'units')
        elif command == 'Down':
            cvs.yview('scroll', '1', 'units')
        elif command == 'Left':
            cvs.xview('scroll', '-1', 'units')
        elif command == 'Right':
            cvs.xview('scroll', '1', 'units')
        elif command == '`grave':
            exit()

#threading.Thread(target=udp_receive, args=(socket_server,)).start()

#while True:
while False:
    cmd = input('PleaseInput:')
    cmd = cmd.split()
    if 'font' == cmd[0]:
        ft = getfont(fontsize=int(cmd[1]))
        #开始位置及时间AA,BC的设定
        bx = 0 -3300
        by = sy 
        bAA = 1
        bBC = 3969
        cvs.create_rectangle(bx, 0, cx, cy, fill='white', outline='white')
        rundata(cr, cvs)
    elif 'sy' == cmd[0]:
        sy = int(cmd[1])
        #开始位置及时间AA,BC的设定
        bx = 0 -3300
        by = sy 
        bAA = 1
        bBC = 3969
        cvs.create_rectangle(bx, 0, cx, cy, fill='white', outline='white')
        rundata(cr, cvs)
    elif 'cy' == cmd[0]:
        cy = int(cmd[1])
        #开始位置及时间AA,BC的设定
        bx = 0 -3300
        by = sy 
        bAA = 1
        bBC = 3969
        cvs.create_rectangle(bx, 0, cx, cy, fill='white', outline='white')
        rundata(cr, cvs)

#播放朗读音的。。。
#voice_file_names = ' '.join(voice_name_list)
#print(voice_file_names)
#runprocess(cvlc_play_mp3, voice_file_names)

#cvlc_play_mp3('/home/ed/grace_voice_file/voice4bt_data/罗马三教皇.mp3 /home/ed/grace_voice_file/voice4bt_data/教会分裂.mp3', hasBlank=False)

#看诡异事件。。。不用这个也能用。。。上面的False了就不行。。。
bibletime.mainloop()
