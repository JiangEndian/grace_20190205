#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *
from newestMyPython3 import *

#字体设置
global ft
ft = getfont(fontsize=120)
#ft = getfont('Times', 110)

#canvas的长和宽设定
global cx
cx = 7000
global cy
cy = 750
#纵屏截图，拼图，分割。。。

#Y轴的步子
global sy
sy = 34

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
kx = 0.2
global ky
ky = 1

#canvase开始画画,没有明确纪年的，推算的时间的。如族长时代们～
def cr(cvst, who, whenson, age, color, other='空白'):
    global ft
    global cy
    global bx
    global by
    global bAA
    global bBC
    global kx
    global ky
    def bAD(after=0):#通过BC计算AD
        global bBC
        return 1-(bBC-after)
    if bAA == 1:#刚开始时画标尺
        cvst.create_line(1,(sy/2)*ky,cx*kx,(sy/2)*ky,fill='black')#上线
        cvst.create_line(1,(cy-sy/2)*ky,cx*kx,(cy-sy/2)*ky,fill='black')#下线
        for ix in [i*300 for i in range(int(cx/100))]:
            cvst.create_line(ix*kx,(sy/2)*ky,ix*kx,sy*0.7*ky,fill='black')#上线标尺
            cvst.create_text(ix*kx,sy*0.95*ky,text='AA' + str(ix),font=ft,fill='black')
            if ix<3970:
                cvst.create_text(ix*kx,sy*ky+sy/4,text='BC'+str(3970-ix),font=ft,fill='black')
            elif ix>3970:
                cvst.create_text(ix*kx,sy*ky+sy/4,text='AD'+str(ix-3969),font=ft,fill='black')
            cvst.create_line(ix*kx,(cy-sy/2)*ky,ix*kx,(cy-sy*0.7)*ky,fill='black')#下线标尺
            cvst.create_text(ix*kx,(cy-sy*0.9)*ky,text='AA' + str(ix),font=ft,fill='black')
            if ix<3970:
                cvst.create_text(ix*kx,(cy-sy)*ky-sy/4,text='BC'+str(3970-ix),font=ft,fill='black')
            elif ix>3970:
                cvst.create_text(ix*kx,(cy-sy)*ky-sy/4,text='AD'+str(ix-3969),font=ft,fill='black')
        by = sy/2 + by#画完标尺，下移图画

    #AD1年为AA3970年，那么，BC1年，为AA3969年（AA:AfterAdam)
    #if whenson == 0:
    if True:
        msgt1 = 'AA%d-AA%d年 %s 持续:%d年' % (bAA,bAA+age, who, age)
    else:
        msgt1 = 'AA%d-AA%d年  事件:%s  交任:%d年  持续:%d年' % (bAA,bAA+age, who, whenson, age)
    if bBC > bAD() and (bBC-age) > bAD(age):#生死都在公元前
        #if len(other) < 16:
        if True:
            msgt2 = 'BC%d-BC%d年' % (bBC,bBC-age)
        else:
            msgt2 = 'BC%d-BC%d年' % (bBC,bBC-age,)
    elif bBC < bAD():#生于公元后
        if True:
            msgt2 = 'AD%d-AD%d年' % (bAD(),bAD(age))
        else:
            msgt2 = 'AD%d-AD%d年\n%s' % (bAD(),bAD(age), other)
    else:#生于公元前，但死于公元后
        if True:
            msgt2 = 'BC%d-AD%d年' % (bBC,bAD(age))
        else:
            msgt2 = 'BC%d-AD%d年\n%s' % (bBC,bAD(age), other)
    msgt = msgt1 + '  ' + msgt2

    #满足条件，隐藏一些条的文字

    #计算新的高度nsy
    nsy = (msgt.count('\n')+1) * sy / 2 

    if by + nsy > cy - sy*1.5:#如果y轴画过了，重新回到sy*1.5开始画
        by = sy * 1.5
    #画矩形，开始位置，长宽，填充,然后在末处画一条纵线/纵线提前画了
    #cvst.create_line((bx+age)*kx, 0, (bx+age)*kx, cy, fill=color)
    cvst.create_rectangle(bx*kx, by*ky, (bx+age)*kx, (by+nsy)*ky, fill=color)
    cvst.pack()

    #显示这些信息，个别调整一些X的位置，以便文字显示不重叠
    cvst.create_text((bx+age/2)*kx, (by+nsy/2)*ky, text=msgt, font=ft, fill='black')

    #开始位置和时间前进喽
    bx += whenson
    by += nsy
    bAA += whenson
    bBC -= whenson

bibletime = tk.Tk()
bibletime.title('BibleTime...')
#一个Y轴滚动条
scrollbary = Scrollbar(bibletime)
scrollbary.set(0.5,1)
scrollbary.pack(side=RIGHT)
#一个X轴滚动条
scrollbarx = Scrollbar(bibletime, orient=HORIZONTAL)
scrollbarx.set(0.5,1)
scrollbarx.pack()
#把这个东西设置好同时绑定到滚动条上
#cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)#加上set后，win不好使
cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=scrollbarx, yscrollcommand=scrollbary)#不加set,mint好使...
cvs.pack()
#对滚动条进行配置，滚动时触发什么
scrollbarx.config(command=cvs.xview)
scrollbary.config(command=cvs.yview)

color1 = 'pink'
color2 = 'yellow'
color3 = '#00FF00'#闪绿色
color4 = '#00FFFF'#青色
color5 = '#FFFFFF'#白色不显示

#对单词进行块分割
def asciicount(text):
    nums = 0
    for num in range(10):
        nums += text.count(str(num))
    for symbol in '{' '}' '[' ']' '<' '>' '/' '*' '-' '=' 'B' 'C' 'A' 'D' ' ':
        nums += text.count(symbol)
#    print(nums)
    return nums

#asciicount('江飞0123456789 {} [] ')

def strdef(strlist, charnums=33):
    text = ''
    alltext = ''
    spacenum = 0
    for word in strlist:
        text += word + ' '
        if len(text) - asciicount(text)/2 >= charnums:
            #print(len(text), text)
            if word != strlist[-1]:
                alltext += text + '\n'
            else:
                alltext += text
            text = ''
    alltext += text
    return alltext

#cr(cvs, '事件', 交任, 持续, 'color', '大事记')

temp = '''创造 光 空气 植物 光体 飞鸟和鱼 陆地生物和人 安息 亚当 伊甸 起名 夏娃 蛇诱 堕落 星爆 惩罚 救恩 被逐 人类史开始 该隐 亚伯 生塞特 相似'''.split(' ')
cr(cvs, '''亚当入世''' ,  130, 930,  color1, strdef(temp,33))


cr(cvs, '''塞特''' ,  105,  912,  color2, '''生以挪士''')
cr(cvs, '''以挪士''' ,  90,  905,  color1, '''生该南''')
cr(cvs, '''该南''' ,  70,  910,  color2, '''生玛勒列''')
cr(cvs, '''玛勒列''' ,  65, 895,   color1, '''生雅列''')
cr(cvs, '''雅列''' ,  162, 962,   color2, '''生以诺''')
cr(cvs, '''以诺''' ,  65, 365,   color1, '''与神同行300年 神将他取走 生玛土撒拉''')
cr(cvs, '''玛土撒拉''' ,  187, 969,   color2, '''人类史最长寿的男人 生拉麦''')
cr(cvs, '''拉麦''' ,  182, 777,   color1, '''给儿子起名挪亚时很感慨''')
cr(cvs, '''挪亚''' ,  480, 950,   color2, '''500岁 闪 含 雅弗 世界败坏 挪亚蒙恩 指示方舟''')
cr(cvs, '''方舟''', 119, 119, color1, '''300×50×30（肘^3） 三层 同时传道''')
cr(cvs, '''洪水''', 2, 1, color2, '''挪亚600.2.17开始 洪水审判 601.2.27地干 新规 彩虹之约 农夫挪亚 闪 雅弗 含 迦南 宁录 巴别之变''')


#cr(cvs, '''百岁闪''' , 0, 500,   color1, '''创11：10,洪水后两年闪100,此时挪亚602\n即挪亚502岁生了闪 不明所以   生亚法撒''')
cr(cvs, '''百岁闪''' , 0, 500,   color1, '''生亚法撒''')


cr(cvs, '''亚法撒''' ,  35,  438,  color2, '''生沙拉''')
cr(cvs, '''沙拉''' ,  30,  433,  color1, '''生希伯''')
cr(cvs, '''希伯''' ,  34,  464,  color2, '''生法勒''')
cr(cvs, '''法勒''' ,  30,  239,  color1, '''生拉吴''')
cr(cvs, '''拉吴''' ,  32,  239,  color2, '''生西鹿''')
cr(cvs, '''西鹿''' ,  30,  230,  color1, '''生拿鹤''')
cr(cvs, '''拿鹤''' , 29,  148,   color2, '''生他拉''')


#cr(cvs, '''他拉''' ,  130, 205,   color1, '''创11：26节 和挪亚500岁生3个儿子一样的描述 不明所以   生亚伯兰\n亚伯兰娶妹子撒莱 拿鹤娶侄女密迦 三拉一得出吾珥至哈兰 他拉死''')
cr(cvs, '''他拉''' ,  130, 205,   color1, '''生亚伯兰 亚伯兰 妹子撒莱 拿鹤 侄女密迦 三拉一得 出吾珥至哈兰 他拉死''')


temp = '''75岁 蒙召 到迦南 饥荒 下埃及 法老 怒送 南地 罗得分 四王胜五王 救罗得 麦基洗德 所多玛王 #立约# 夏甲插曲 85岁 86岁 以实玛利 100岁 以撒'''.split()
cr(cvs, '亚伯兰', 85, 175, color2, strdef(temp))


cr(cvs, '''立约到立法''', 14, 430, color1, '''加3：17,立约与立法的时间距为430年（出12：40,430年 从亚伯兰在埃及算起）''')


temp = '''撒拉90 亚伯拉罕 割礼 应许以撒 灭所多玛 罗得家 摩押 押扪 基拉耳王 亚比米勒 亚伯拉罕100 撒拉91 生以撒'''.split()
cr(cvs, '''亚伯兰99''', 1, 1, color2, strdef(temp, 70))


temp = '''以撒生 摆筵席 逐夏甲 巴兰旷野 亚亚约 30岁甘心被献 拿鹤消息 撒拉127去世 买坟地 4年后 以撒40 娶利百加 60双子 （父妾 基土拉 分财散子 175死） 雅各 以扫 红豆汤 基拉耳 非利士王 亚比米勒 昌盛 挖井 以亚约'''.split()#127-91=36,36-》40 4年 迎来利百加
cr(cvs, '''以撒''', 60, 180, color1, strdef(temp, 36))


temp = '''40以扫娶妻 利百加之计 77至拉班 以扫再娶 伯特利异梦 饮羊 20年 打工 娶妻 生娃 生约瑟 挣家业 {流便 西缅 利未 犹大 （但 拿弗他利） （迦得 亚设） 以萨迦 西布伦 约瑟 便雅悯} 被召回 偷走* 追搜怒斥 雅拉约 见以扫 瘸腿 迎以扫 示剑* 底拿 西利屠城 伯特利 以法他 （伯利恒） 便雅悯 以得台 流便 至以撒 以扫分'''.split()#过14年 91岁生约瑟 至拉班时 91-14=77 84娶妻   
cr(cvs, '''雅各''', 91, 147, color2, strdef(temp))


temp = '被偏爱 打报告 彩衣 17做梦 看望 被卖 波提乏 （犹大 书亚 他玛 法勒斯） 蒙恩 诱惑 不从 被冤下监 蒙恩 28解梦 信好 好坏 被忘 双七梦 30见法老 解梦出策 治理埃及 31丰年 得妻生子 38饥荒 38见兄 要见便雅悯 通事传话 哭 银包 父亲之痛 犹大担保 见便雅闵 哭 银杯 犹大护弟 哭 相认 原谅 哭 约瑟之意 法老之令 39见雅各 哭 130雅各 全家70人 埃及歌珊 奉养 五一分 玛以以玛 领受双分 雅各祝福'.split()
cr(cvs, '''约瑟''', 39, 110, color1, strdef(temp))


cr(cvs, '''以色列在埃及''', 145, 225, color2, '''雅各死 葬于那坟地 哥哥们求饶恕 哭<我岂能代替神呢 神的意思是好的>亲爱话安慰
让以色列人起誓 约瑟死 创世记完 BC1560 含逐闪 18代新王兴 利未-歌辖-暗兰·小姑-亚伦&摩西-出埃及''')

temp = '''雅各繁盛 新王苦待 收生婆 雅各强盛 丢男孩 摩西生 三月弃 被收养 40岁摩西 热心 至米甸 40年放羊 何烈山异象 神之名 Yahweh 被迫领导 同工亚伦 言明不容 血郎 百姓信 祸患 层层诉苦 安慰 苦愁不听 见法老 容我的百姓去 神迹 不行'''.split()
cr(cvs, '''摩西''', 80, 120, color1, strdef(temp))


cr(cvs, '''立法到建殿''', 0, 480, color2, '''王上6：1,出埃及后480年 所罗门王4年2月 建殿''')


temp = '''十灾{血 蛙 虱 蝇 畜疫 疮 冰雹 蝗虫 黑暗 长子} 妥协 拒绝 逾越节 催促 夺财 60万 约瑟骨 离开 绕道 云火柱 追兵怨 红海 水灭 水护 歌唱 玛拉怨 律典 汛怨 鹌鹑 40年吗哪 水怨 磐石出水 战亚玛力人 岳父 出谋 西奈山 律法 会幕 祭司长 法版 金牛犊 烈怒 恳求 烈怒碎版 饮罪 亚伦辩 利未杀 舍己赎罪 摘饰候 摩西求 神的荣耀 双版上山 五祭七节 （燔祭 素祭 平安祭 赎罪祭 赎愆祭） 逾越节 除酵节 初熟节 五旬节 吹角节 住棚节 赎罪日 双版下山 发光 蒙脸 圣所献 礼物和人 工成祝福 成圣 亚伦献祭 二子死： <亲近人中显为圣 众民面前得荣耀> <祭司禁宣泄己情 神的膏油在其身> 利未人 祭司分 食例 人口调查 加底斯 巴尼亚 12探子 击杀 恳求 徘徊 恶信死 强上败 可拉妒 会众攻击 神怒 亚伦站 亚伦之杖 加低斯 米利巴水 兄弟之情 何珥山亚伦死 吗哪怨 铜蛇 亚摩利王 西宏 巴珊王噩 摩押王 巴勒 巴兰 <咒诅变祝福 拣选与无罪> 什亭 非尼哈 民数 无仅 立约书亚 米甸人 报仇 巴兰死 军长赎命 河东三派 摩押之嘱 逃城 讲律法 证歌'''.split()
cr(cvs, '''出埃及与旷野''', 40, 40, color1, strdef(temp, 48))


temp = '''摩西祝福 观望 摩西死 81岁约书亚？ 刚强壮胆×4 探子 喇合 红绳 约旦断 吉甲滚 吃地天止 元帅 绕城禁声 呼喊墙塌 喇合活 亚干贪财 艾城 哀哉与起来 亚割灭 焚艾 基利心祝福 以巴路咒诅 基遍计 五王恨 基遍求 以刀杀 冰雹杀 日停月止 军长踏五王 刚强壮胆 26年征服 年迈未得 分地 示罗会幕 但人越界 设立逃城 证坛 示剑约 约书亚死 懂事长老尚在 示剑埋骨 以利亚撒死 士师记'''.split()#约书亚到分裂共476年 以色列得地450 约书亚推测与迦勒同岁 40岁探地 81岁接任 
cr(cvs, '''约书亚81?''', 29, 29, color2, strdef(temp, 44))


cr(cvs, '27年元老死？', 27, 27, color1, '''犹大西缅同去 约瑟灭路斯 不全逐的波金哭 旧代死新代兴（27年？）''')


temp = '''[离弃 苦难 士师拯救] 恶性循环 士师们 （俄陀聂 以笏 珊迦 底波拉 基甸 陀拉 睚珥 耶弗他 以比赞 以伦 押顿 参孙） 路得故事 （法勒斯 希斯仑 兰 亚米拿达 拿顺 撒们 喇合 [开始士师] 波阿斯 路得 俄备得 耶西 [统一王国] 大卫） 米迦像 无地但 一家/一族 摩西之孙 约拿单 利未人之妾 便雅悯濒危 挽救 '''.split()
cr(cvs, '200年士师记？', 200, 200, color4, strdef(temp, 35))


temp = '''以利加拿 毗尼拿 哭泣哈拿 默祷 无愁 撒母耳 哈拿之歌 恶二* 以利 <尊重儿子过于神> <尊重神 神重看 藐视神 被轻视> 未识 呼召 丢约柜 祭司家事 约柜显耀旅 伯示麦杀 米斯巴 以便以谢 二子不堪 求王 不悦 神释 警告 依从 好扫罗 高喜 上位 救雅比 吉甲立国'''.split()
cr(cvs, '100年撒母耳？', 100, 100, color2, strdef(temp))


temp = '''40扫罗王 先知证清 雷雨 不弃不断 二年时 吉甲越位 约拿单之勇 蜜 扫罗妒 百姓救 灭亚玛力之命 扫罗之惜 <耶和华所悦 听命与顺从> 厌弃与厌弃 求人抬举 亚甲喜怒 不见先知之悲 耶西众子 <人看外貌 神看内心> 牧童大卫 弹琴 歌利亚 兄长之怒 无畏之信 约拿单盟 千千怒 钉 害 约拿单调和 钉 米甲救 拉玛撒母耳 拿约捉 逃至约拿单 结盟 三日离席 扫罗怒子 见哭 亚希米勒 逃至亚吉 装疯 逃至亚杜兰洞 收聚失意人 安置父母 摩押王 祭司灾 以东人多益 救基伊拉 亚比亚他 大卫 必交 逃离 扫罗寻索 约拿单坚固 西弗出卖 西拉哈玛希罗结 （扫追大 非攻扫 扫回） 割衣襟 自责 扫罗哭 拉玛葬先知 收富寡妇 西弗再卖 枪和水瓶 投奔亚吉 16月 备战 扫罗求鬼 洗革拉 大卫夺回 送礼 以色列 战败 扫罗亡 基列雅比 葬扫罗 杀受膏者 死罪 大卫 哀歌 上希伯仑 大卫王'''.split()
cr(cvs, '''扫罗40''', 40, 40, color1, strdef(temp))


temp = '''见基列雅比人 犹大王90月 亚撒黑之悲 帕铁之悲 押尼珥之悲 王举哀 临门二子罪 33年 以色列王 攻占耶路撒冷 推罗王 希兰示好 利乏音谷战 乌撒触约柜 俄别以东福 大卫移柜 献祭跳舞 米甲讽* 建殿意 征胜 秉公行义 洗巴 米非波设 亚扪王 哈嫩辱 败亚扪 <安乐 大卫王 忧患 乌利亚> 王召 款待 杀夫 夺妻 甚不喜悦 拿单之喻 除罪 惩罚 禁食 吃饭 所罗门 耶底底亚 占拉巴 役亚扪 暗嫩 他玛 约拿达 完事 甚恨 逐 押沙龙 二年忍 大卫只怒 自己动手 完事逃 三年 大卫心 约押意 押沙龙回 二年不见 烧田见 拉拢人心 子叛 父逃 以太 撒督 亚比亚他 户筛 洗巴 示每骂 大卫心 亚希多弗 户筛 报信 童子与妇人 大卫过河 玻璃心 巴西莱 备战 王从兵 嘱咐 胜 押沙龙之悲 二信使 答非所问 耿直 王哀 民愧 王出安慰 请回 铙示每 洗巴 米非波设 均分地土 金罕 以色列人 示巴 犹大人 冷宫怨 亚玛撒逾期 亚比筛追示巴 约押杀亚玛撒 妇人救城 完事回家 三年干旱 扫罗热心 基遍人 悬挂七人 利斯巴守护 大卫葬骨 王危 跟随者之志 大卫诗歌 勇士故事 数民罪 降灾 怜悯 亚劳拿禾场 献祭 垂听 灾停 王年迈 亚比煞 未近 亚多尼雅 约押 亚比亚他 拿单 拔示巴'''.split()
cr(cvs, '''大卫''', 40, 40, color2, strdef(temp))


temp =  '''所罗门王 父亲之嘱：刚强 谨守 约押 巴西莱众子 示每 大卫睡 亚多尼雅 亚比煞 死 革亚比亚他 杀约押 杀示每 国位坚定 基遍献祭 求智慧 判孩子 兴盛繁荣 智慧聪明 外交希兰 7年建殿 13年造宫 约柜入殿 祷告 降火 荣光 祝福 献祭 再次显现 外人 子民 俄斐 示巴女王 还礼 666金 极荣华王 七百妃 三百嫔 年老偏离 外患四起 所罗门睡 罗波安王 不听老人 以色裂 BC931分裂'''.split()
cr(cvs, '''所罗门''', 40, 40, color1, strdef(temp,30))

#----------------北国以色列---------------------------------
#cr(cvs, '''北国以色列''', 0, 209, color2, strdef(temp))
cr(cvs, '''北国以色列''', 0, 209, color2, '19 0 BC722 亚述 以色列 南北王图')

#------------------南国犹大--------------------------------------
#cr(cvs, '''南国犹大''', 31, 345, color1, strdef(temp))
cr(cvs, '''南国犹大''', 31, 345, color1, '20 8 BC586 巴比伦 犹大 南北王图')


cr(cvs, '''亚述''', 288, 288, color4, '''灭北国''')
cr(cvs, '''巴比伦''', 3, 73, color4, '''灭南国''')


temp =  '''BC605/BC606 约雅敬 但以理 贵族王族'''.split()
cr(cvs, '''约雅敬''', 11, 11, color1, strdef(temp))


temp = '''BC597 约雅斤 以西结 首领和技工'''.split()
cr(cvs, '''约雅斤''', 1, 1, color2, strdef(temp))


temp = '''BC586 西底家 南国灭'''.split()
cr(cvs, '''玛探雅''', 11, 11, color1, strdef(temp))


cr(cvs, '''被掳70年''', 47, 70, color2, '''但以理在巴比伦 古列元年 神应验 激动王心 通告归回''')


cr(cvs, '''波斯''', 23, 204, color4, '''归回 BC515大利乌一世 马拉松战败 圣殿完工 亚哈随鲁（薛西斯一世）以斯帖BC483-BC473
波斯：古烈 大利乌一世 亚哈随鲁 亚达薛西一世 大利乌二世 亚达薛西二世 大利乌三世''')


temp = '''BC538-BC515 古烈 第二圣殿 BC536 所罗巴伯 BC516 重建圣殿 族长 祭祀 利未人 神激动心之人 四围 资助 古列 器皿 49897人 神殿献礼 筑坛 献祭 守节 建殿 立基 欢呼/哭号 敌扰 亚哈随鲁 才登基 上本奏告 亚达薛西 联合控告 上本 王查 古来常叛 停工 大利乌2年 哈该 撒迦利亚 传达劝勉 建造 神看顾 只问未停 上本 寻典 王令 禁阻 命帮 禁改令 王6年 修成 献殿 守节'''.split()
cr(cvs, '''所罗巴伯''', 58, 23, color2, strdef(temp))


temp = '''BC458/BC457 亚达薛西一世 1754人 复兴信仰 亚达薛西 7年降旨 以斯拉 神帮助 王允求 1.1起 向王夸神 求王耻 禁食祈求 应允 5.1达 考究 遵行 教训 众首领见 通婚罪 举手认罪 与神立约 休外邦妻 按期办理'''.split()
cr(cvs, '''以斯拉''', 14, 1, color1, strdef(temp))


temp = '''BC444-BC425 亚达薛西 贵族家庭 尼希米 42360人 城墙 52日 亚达薛西20年 尼希米 犹大来人 惨况 哭泣悲哀 禁食祈祷 酒政愁容 祖坟城荒 王问 默祷 求差遣 定日期 王喜 求诏书 王允 护送 夜查城 保密 重建 分工作 敌恨嗤笑 墙高一半 敌怒来攻 工作与兵器 不脱衣 天亮 工作 星现 百姓怨弟兄 尼系米怒 筹划 斥责 攻击取利者 归还 不再索要 两袖清风 敌计害 工忙不去 52天修完 城广民稀 日升开 尚守关 按班看守 神感动 家谱计算 7月聚集 请以斯拉 宣读律法 讲明意思 众民哭 当喜乐 吃肥喝甘 明白教训 大大快乐 住棚 喜乐 禁食 披麻 蒙灰 离绝外邦 认罪 称颂 述说神作为 祈求 认罪 立约签名 起誓遵行 掣签住圣城 渐上正轨 回王 祭司结亲 多比雅屋 告假归来 怒抛 净屋 归原用处 利未奔田 斥责管长 招聚供职 1/10 犯安息日 斥责贵胄 关门 商人外宿 警戒 圣安息日 外女妻 省长惩诫 污祭司 赶出 洁净 离绝 尽职 守节'''.split()
cr(cvs, '''尼希米''', 112, 19, color2, strdef(temp))


cr(cvs, '''希腊''', 31, 165, color4, '''BC404-BC331波斯被亚历山大攻陷 亚历山大和大利乌三世几乎同时上位
马拉松战 亚历山大胜 BC333年 亚历山大33岁 死于蚊子 希腊语''')


cr(cvs, '''托勒密王朝''', 103, 100, color4, '''BC301-BC201=托勒密王朝 被安条克三世占领 BC250 70士译本''')
cr(cvs, '''塞硫西王朝''', 31, 31, color4, '''BC198-BC167=塞硫西王朝 安条克把埃及军队赶出去 安条克四世污秽圣殿''')


cr(cvs, '''马喀比革命''', 3, 3, color2, '''BC167马加比革命 BC164洁净圣殿 修殿节 玛他提亚（祭司长）
自称撒都该人（贵族） 把圣殿中的希腊人都杀了 建立哈斯摩尼王朝''')


cr(cvs, '''哈斯摩尼王朝''', 100, 100, color1, '''BC167-BC64=以色列 自由''')


cr(cvs, '''罗马''', 27, 193, color4, '''BC64 罗马占领巴勒斯坦 罗马庞贝将军占领耶路撒冷 希律家族支配犹大''')


cr(cvs, '''以东人希律''', 33, 40, color4, '''BC37-AD4=以东人希律统治犹大 21城 第三圣殿 BC4 耶稣降生''')


temp =  '''BC4-AD31=耶稣在世做工 {西门彼得 安德烈 西庇太之子雅各 约翰 腓利 巴多罗买 多马 税吏马太 亚勒腓之子雅各 达太 奋锐党的西门 卖耶稣的加略人犹大}'''.split()
cr(cvs, '''耶稣''', 7, 34, color3, strdef(temp))


cr(cvs, '''分封王&巡抚''', 40, 35, color4, '''AD4-AD39=分封王&敏感地带巡抚''')
cr(cvs, '''巡抚''', 26, 26, color4, '''AD44=巡抚''')
cr(cvs, '''耶路撒冷沦陷''', 65, 65, color4, '''AD70 罗马提多将军攻陷耶路撒冷 AD130年 驱逐犹太人''')
cr(cvs, '''动乱与镇压''', 2, 2, color4, '''AD135动乱 AD137镇压 禁止犹太人入耶路撒冷''')
cr(cvs, '''全球分散''', 1811, 1811, color2, '''犹太人分散在全世界 直至1948年复国''')
cr(cvs, '''以色列复国''', 69, 69, color1, '''以色列复国 等待弥赛亚''')


#names = [[('亚当入世'),(130),(930)], [('塞特'),(105),(912)], [('以挪士'),(90),(905)], [('该南'),(70),(910)], [('玛勒列'),(65),(895)], [('雅列'),(162),(962)], [('以诺'),(65),(365)], [('玛土撒拉'),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()], [(''),(),()],  ]
#things = {'亚当':[(),(),()], }没有必要在这个形式上浪费时间   
#插入不影响：插入的交付为0 例如：
#总原则就是：交付总数不能变 原来总多少 后来也总多少   


bibletime.mainloop()
