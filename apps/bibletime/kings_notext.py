#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *
from newestMyPython3 import *

#字体设置
global ft
ft = getfont(fontsize=140)
#ft = getfont('Times', 100)

#canvas的长和宽设定
global cx
cx = 7000
global cy
cy = 1000

#Y轴的步子
global sy
sy = 40

#开始位置及时间AA,BC的设定
global bx
bx = 2
global by
by = sy
global bAA
bAA = 1
global bBC
bBC = 3969

#画面X轴和Y轴的缩放系数
global kx
kx = 5
global ky
ky = 1

global upnorth
upnorth = True


#对单词进行块分割,第一个是计算占用半块的非汉字数
def asciicount(text):
    nums = 0 
    for num in range(10):
        nums += text.count(str(num))
    for symbol in '{' '}' '[' ']' '<' '>' '/' '*' '-' '=' 'B' 'C' 'A' 'D' ' ':
        nums += text.count(symbol)
        #    print(nums)
    return nums                 
#asciicount('江飞0123456789 {} [] ')
def strdef(strlist, charnums=200):
    text = ''
    alltext = ''
    spacenum = 0 
    for word in strlist:
        text += word + ' ' 
        if len(text) - asciicount(text)/2 >= charnums:
            #print(len(text), text)
            alltext += text + '\n'
            text = ''
    alltext += text
    return alltext
                                                                                                            
#canvase开始画画,没有明确纪年的，推算的时间的。如族长时代们～
def cr(cvst, who, whenson, age, color, other='', syadd=False, strdefe=200):
    global ft
    global cy
    global bx
    global by
    global bAA
    global bBC
    global kx
    global ky
    global upnorth
    #if who == '罗波安' or who == '玛拿西':
    if who == '罗波安':
        bx = 2
    def bAD(after=0):#通过BC计算AD
        global bBC
        return 1-(bBC-after)
    #if bAA == 1:#刚开始时画标尺
    if who == '耶罗波安一世':
        cvst.create_line(2,5,1366,5,fill='black')#上线
        for ix in [i*100 for i in range(14)]:
            cvst.create_line(ix,2,ix,10,fill='black')#上线标尺
            cvst.create_text(ix,20,text=str(ix),font=ft,fill='black')
        cvst.create_line(1300,1,1300,800,fill='black')#右线
        for iy in [i*50 for i in range(20)]:
            cvst.create_line(1300,iy,1290,iy,fill='black')
            cvst.create_text(1280,iy,text=str(iy),font=ft,fill='black')

    #AD1年为AA3970年，那么，BC1年，为AA3969年（AA:AfterAdam)
    if whenson == 0:
        msgt1 = 'AA%d-AA%d年  事件:%s  持续:%d年' % (bAA,bAA+age, who, age)
    else:
        msgt1 = 'AA%d-AA%d年  事件:%s  交任:%d年  持续:%d年' % (bAA,bAA+age, who, whenson, age)
    if bBC > bAD() and (bBC-age) > bAD(age):#生死都在公元前
        if len(other) < 6:
            msgt2 = 'BC%d-BC%d年  大事记:%s' % (bBC,bBC-age, other)
        else:
            msgt2 = 'BC%d-BC%d年  大事记:\n%s' % (bBC,bBC-age, other)
    elif bBC < bAD():#生于公元后
        if len(other) < 6:
            msgt2 = 'AD%d-AD%d年  大事记:%s' % (bAD(),bAD(age), other)
        else:
            msgt2 = 'AD%d-AD%d年  大事记:\n%s' % (bAD(),bAD(age), other)
    else:#生于公元前，但死于公元后
        if len(other) < 6:
            msgt2 = 'BC%d-AD%d年  大事记:%s' % (bBC,bAD(age), other)
        else:
            msgt2 = 'BC%d-AD%d年  大事记:\n%s' % (bBC,bAD(age), other)
    msgt = msgt1 + '  ' + msgt2
    #重设msgt为列王适用
    def sisnum(s):
        for i in 1, 2, 3, 4, 5, 6, 7, 8, 9:
            if s == str(i):
               return True
    if sisnum(other.split()[0][0]):
        msgt = '%s %s' % (who, other)
    else:
        msgt = '%s %.2f %s' % (who, age, other)
    msgt = strdef(msgt.split(), strdefe)
    #msgt = msgt.split()[0] + ' ' + msgt.split()[1] + ' ' + '(%.1f)' % whenson
    msgt = msgt.split()[0] + ' ' + msgt.split()[1] 
    #print(who,' %.2f' % age)
#    msgt = who
    #满足条件，隐藏一些条的文字
    if age == 480 or age == 430:
        msgt = ''

    #计算新的高度nsy
    nsy = (msgt.count('\n')+1) * sy / 2 

    #if by + nsy > cy - sy*1.5:#如果y轴画过了，重新回到sy*1.5开始画
    #    by = sy * 1.5
    #画矩形，开始位置，长宽，填充,然后在末处画一条纵线,if的作用是判断，南国开始了，不画竖线条了。
    if who == '罗波安':
        upnorth = False
       # by -= 165
    if upnorth:
        cvst.create_line((bx+age)*kx, 0, (bx+age)*kx, cy, fill='green')
    if who == '@希西家':
       # by -= 180
        pass
    cvst.create_rectangle(bx*kx, by*ky, (bx+age)*kx, (by+nsy)*ky, fill=color, outline=color)
    cvst.pack()
    #显示这些信息
    #if who == '耶罗波安一世':
    if False:
        cvst.create_text((bx+age)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')
    else:
        cvst.create_text((bx+age/2)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')

    #开始位置和时间前进喽
    bx += whenson
    if syadd == True:
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
FullScreenApp(bibletime)
bibletime.title('BibleTime...')
#一个Y轴滚动条
#scrollbary = Scrollbar(bibletime)
#scrollbary.set(0.5,1)
#scrollbary.pack(side=RIGHT)
#一个X轴滚动条
#scrollbarx = Scrollbar(bibletime, orient=HORIZONTAL)
#scrollbarx.set(0.5,1)
#scrollbarx.pack()
#把这个东西设置好同时绑定到滚动条上
#cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)#加上set后，win不好使
#cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=scrollbarx, yscrollcommand=scrollbary)#不加set,mint好使...
global cvs
cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white')#不加set,mint好使...
cvs.pack()
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
bibletime.bind('<Up>', cup) #窗体绑定按键与方法
bibletime.bind('<Down>', cdown)
bibletime.bind('<Left>', cleft)
bibletime.bind('<Right>', cright)
#对滚动条进行配置，滚动时触发什么
#scrollbarx.config(command=cvs.xview)
#scrollbary.config(command=cvs.yview)

color1 = 'pink'
color2 = 'yellow'
#对滚动条进行配置，滚动时触发什么
#scrollbarx.config(command=cvs.xview)
#scrollbary.config(command=cvs.yview)

color1 = 'pink'
color2 = 'yellow'
color3 = '#00FF00'#闪绿色
color4 = '#00FFFF'#青色
color5 = '#FFFFFF'#白色不显示

#cr(cvs, '事件', 交任, 持续, 'color', '大事记')

#北国诸王
cr(cvs, '耶罗波安一世', 20, 20, color1, '22 牛犊 凡民祭司 自定节期 神人裂坛 老先知骗 耶罗波安的妻 亚希雅 预言灾祸',  syadd=True, strdefe=60)
cr(cvs, '拿答', 1, 1, color2, '2 行恶如父 巴沙叛杀全家', syadd=True)
cr(cvs, '巴沙', 23, 23,  color1, '24 行恶如祖 耶户责备')
cr(cvs, '以拉', 1, 1, color2, '2 喝醉 心利叛杀全家', syadd=True)
cr(cvs, '心利', 7/365, 7/365, color1, '7天 民立暗利 自焚宫殿', syadd=True)
cr(cvs, '暗利', 11, 11, color2, '12 暗利民强 提比尼死 暗利王 买撒玛利亚山 造撒玛利亚城 行恶如祖更甚')
cr(cvs, '亚哈', 19, 19, color1, '22 行恶如祖更甚 以为轻 娶耶洗别 建庙筑坛造偶像 希伊勒 重修耶利哥 （以利亚 祷告 藏 乌鸦 西顿的撒勒法寡妇 见亚哈 迦密山之证 降雨 亚哈告 耶洗别誓杀 逃 罗腾树下求死 吃喝走 何烈山洞 神的指示 七千人 以利沙） 便哈达攻撒玛利亚 无理要 亚哈从 更无理 长老百姓 不从 先知传达 七千名 杀敌 敌王兵同逃 先知提醒 再战 神人传达 杀敌十万 墙杀二万七千 便哈达投降 亚哈放 先知门徒 不打狮咬 打伤 喻王 闷闷不乐回宫 贪拿伯园 拒绝 闷闷不乐回宫 躺墙绝食 耶洗别恶计 长老贵胄照行 拿伯死 下去得园 以利亚传达 亚哈自卖 从耶洗别 王自卑 延祸 约沙法 同去 400先知 米该雅 使者劝 吉言* 王要 实话* 言祸 西底家 打脸* 米该雅 下监受苦 改装王 随便开弓 亚哈亡',strdefe=80)
cr(cvs, '亚哈谢', 1, 1, color2, '2 行恶学父母 如耶罗波安 摩押叛 楼落 求假神 以利亚传达 五十夫长 神权胜王权 见王 传达 王死 无儿 兄弟继位', syadd=True)
cr(cvs, '约兰', 11, 11, color1, '12 （以利亚/沙 伯特利 耶利哥 先知门徒 约旦河 打水 加倍感动 火车火马 升天 看见 师衣打水 耶利哥先知门徒 迎接 寻找未得 盐治水 童子事件） 王行恶 约沙法 以东王 攻摩押 三王无水 见以利沙 弹琴灵降 挖沟 次日早晨水来 呆萌摩押王 打败摩押 摩押王长子祭 以人遭怒 三王回国 （妇人儿子器皿油 书念妇人 得子 死 无言见神人 不离同去 神人祈祷 救活劝走 毒野瓜 面治 二十饼一百人 乃缦 小女子于主母言 乃缦见主 亚兰王许信 带礼物去 以色列王撕衣 以利沙 不见之命 乃缦气忿 仆人劝 大事小事 照做 洁净 送礼不受 求土求恕 基哈西爱财 受财受沾染 嫌小扩建 斧头浮现 争战 卧房话传 围多坍 开眼见 敌目昏迷 引撒玛利亚 开眼 不可杀 款待 放回 亚兰军 不再犯境 便哈达围城 撒玛利亚饥荒 妇人食子 王怒以利沙 以利沙传达 多话军长 四痳疯病人 死地绝境 无选之择 发了 报好信 不信与窥探 掳掠营盘 军长弹压 死 七年妇回 王询基哈西 复活事 恰巧妇人来求 归还 至大马色 亚兰王便哈达病 差哈薛见 病必好人必死 神人看哭 哈薛王） 以东立拿叛 同亚哈谢与哈薛争战 伤 回耶斯列治伤 亚哈谢来访 以利沙差先知门徒膏耶户 耶户王叛约兰', strdefe=100)
cr(cvs, '耶户', 28, 28, color2, '去耶斯列 二使者不回 二王套车迎 拿伯田相遇 满弓穿心 约兰亡 抛田 亚哈谢逃 击伤 米吉多死 臣仆葬尸 至耶斯列 耶洗别化妆 太监顺命扔 耶户进去吃喝 欲葬只寻 写信撒玛利亚 首领 长老 尊贵人 教养者 杀众子 首级堆 往撒玛利亚 杀亚哈谢弟兄 恰遇利甲儿子约拿达 灭尽亚哈家 计杀巴力庙 厕所 灭巴力拜牛犊 应许四代', strdefe=80)
cr(cvs, '约哈斯', 14, 14, color1, '17 行恶 神发怒 交敌手 恳求 见以受欺 应允 赐拯救者 仍犯罪 哈薛灭民 仅留残兵')
cr(cvs, '约阿施', 15, 15, color2, '行恶 以利沙 死病 王来看他 打地三次 神人发怒 葬埋 死人碰活 败便哈达 三败收城')
cr(cvs, '耶罗波安二世', 40, 40, color1, '41 行恶 收地 如约拿传 神未要灭 借其拯救')
cr(cvs, '撒迦利雅', 0.5, 0.5, color2, '6月 行恶 沙龙叛杀', syadd=True)
cr(cvs, '沙龙', 0.5, 0.5, color1, '1月 米拿现 杀 篡位', syadd=True)
cr(cvs, '米拿现', 11, 11, color2, '10 攻杀剖妇 行恶 亚述王 普勒来攻 1000银贡 索大富户 亚述王回', syadd=True)
cr(cvs, '比加辖', 2, 2, color1, '行恶 利玛利子 将军比加 众帮叛杀', syadd=True)
cr(cvs, '比加', 20, 20, color2, '20 行恶 亚述来掳 何细亚叛杀')
cr(cvs, '何细亚', 9, 9, color1, '行恶 撒缦来攻 服事进贡 背叛 差人见梭 亚述王囚 攻以遍地 围都三年 攻取 掳人 迁人', syadd=True, strdefe=10)


#南国诸王
cr(cvs, '罗波安', 17, 17, color1, '17 备战 示玛雅解散 埃及王示撒攻耶城 夺宝', syadd=True)
cr(cvs, '亚比央', 2, 2, color2, '3 行恶 大卫之故', syadd=True)
cr(cvs, '@亚撒', 40, 40, color1, '41 效法大卫 除娈童除偶像贬太后 巴沙来攻 亚兰王便哈达应助')
cr(cvs, '@约沙法', 20, 20, color2, '25 行正 亲北 得金失意')
cr(cvs, '约兰', 7, 7, color1, '8 杀诸兄弟', syadd=True)
cr(cvs, '亚哈谢', 1, 1, color2, '亚哈家女婿 行恶如亚哈家 同约兰与哈薛争战 下耶斯列探访亚哈谢 死', syadd=True)
cr(cvs, '亚他利雅', 6, 6, color1, '7 剿灭王室 约示巴藏约阿施 圣殿6年 7年立约见王子 耶何耶大膏约阿施王 杀亚他利雅 王民神约 亚巴力', syadd=True, strdefe=25)
cr(cvs, '@约阿施', 37, 37, color2, '40 7岁登基 耶何耶大教训时行正 奉纳修殿 诚实与信任 哈薛来犯 送礼不上 臣仆叛杀')
cr(cvs, '@亚玛谢', 40, 40, color1, '29 行正仿父 杀叛饶子 盐谷杀 攻西拉 约帖 挑战以王 约阿施使 败以东 心高气傲 安居既罢 不听 犹大败 拆墙掳掠 背叛 王逃拉吉 叛杀 驮尸埋葬', strdefe=35)
cr(cvs, '@乌西雅', 29, 29, color2, '52 亚撒利雅 行正仿父 降大痳疯 约坦代管')
cr(cvs, '@约坦', 15, 15, color1, '16 行正仿父 建殿上门 亚兰王利汛 比加 攻击', syadd=True)
cr(cvs, '亚哈斯', 6, 6, color2, '16 行恶如北 利汛比加 围困不胜 送礼亚述 应允 大马色迎 见坛画 乌利亚做 大坛献祭 铜坛求神 改圣殿', syadd=True, strdefe=20)
cr(cvs, '@希西家', 29, 29, color1, '行正仿祖 废丘坛 毁柱像 砍木偶 碎铜蛇 专靠神 守诫命 同在亨通 叛亚述 攻非利士 西拿基立 攻取坚城 求饶领罚 倾家荡产 三将至 拉伯撒基 言语之重 百姓不言 披麻进殿 见以赛亚  神的安慰 亚述古实 使者之信 入殿 祈求 应允 胜败之因 早先所作 古时所立 神使杀敌 亚述王回 尼尼微庙 二子杀逃 一子继位 死病 祷告痛哭 医治 征兆 痊愈 巴比伦王 使者来访 全秀 以赛亚来 传达', strdefe=25)
cr(cvs, '玛拿西', 55, 55, color2, '行恶如外 造父所毁 效法亚哈 天上万象 神殿筑坛 多行恶事 殿内立像 诱民行恶 更甚 众先知 传达判言')
cr(cvs, '亚们', 2, 2, color1, '行恶如父 臣叛杀 民杀叛 立子', syadd=True)
cr(cvs, '@约西亚', 31, 31, color2, '行正如祖 修殿 诚实信任 得律法书 王听撕衣 求问回复 怜悯公义 念书立约 废偶像 守逾越节 法老攻亚述 王去抵挡 米吉多杀 臣仆葬尸', syadd=True)
cr(cvs, '约哈斯', 0.25, 0.25, color1, '3月 行恶 法老锁罚 带埃及死 以利亚敬 改约雅敬', syadd=True)
cr(cvs, '约雅敬', 11, 11, color2, '征民法老 行恶 服侍巴比伦王 尼布甲尼撒 三年叛 神使敌攻 BC605 约雅敬 但以理 贵族王族', syadd=True)
cr(cvs, '约雅斤', 100/365, 100/365, color1, '100天 巴比伦王夺埃管 法老不再出 行恶仿父 巴比伦军 围困耶城 尼王亲来 投降 尼王8年 掳殿宫人 只剩极穷 立叔玛探雅 BC597 约雅斤 以西结 首领和技工', syadd= True)
cr(cvs, '西底家', 11, 11, color2, '改西底家 行恶 神发怒 西底家叛 尼王来攻 城破兵逃 捉王审判 杀子剜眼 尼王19年 尼布撒拉旦 焚殿宫屋 拆墙掳人 留最穷 掠殿 犹大被掳 基大利省长 以实玛利杀 众民惧迦勒底人 至埃及 以未米罗达元年 约雅手蒙恩 BC586 西底家 南国灭', syadd=True, strdefe=70)
cr(cvs, '被掳70年', 70, 70, color1, '被掳70年', syadd=True, strdefe=70)
cr(cvs, '开始归回', 113, 113, color2, '三次归回', syadd=True, strdefe=70)

x1 = 900
y1 = 270
def draw_prophet(x1, y1, color, text):
    x2 = x1+300
    y2 = y1+35
    cvs.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
    cvs.create_text((x1+x2)/2, (y1+y2)/2, text=text, font=ft, fill='black')

draw_prophet(900, 270, color3, '以赛亚·南')
draw_prophet(350, 140, color3, '以利亚·北')
draw_prophet(380, 180, color3, '以利沙·北')
draw_prophet(380, 220, color3, '约珥·南')
draw_prophet(360, 260, color3, '俄巴底亚·南')


cvs.pack()
bibletime.mainloop()
