import tkinter as tk

# top = tk.Tk()
# top.title('Hello..')

# labelHello = tk.Label(top, text = 'Hello, Tkinter!', bg='blue')
# labelHello.pack()

# top.mainloop()## 运行并显示窗口


# def drawCircle(self, x, y, r, **kwargs):
    # return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    
# top = tk.Tk()
# top.title('Canvas Test')

# cvs = tk.Canvas(top, width =600, height =400)
# cvs.pack()

# cvs.create_line(50, 50, 50, 300)## x1,y1, x2,y2##左上角为0,0

# cvs.create_line(100, 50, 200, 300, fill='red', dash=(4,4), arrow=tk.LAST)

# cvs.create_rectangle(200, 40, 400, 50, fill='blue')##x1,y1, x2,y2##画矩形

# cvs.create_oval(450, 50, 550, 200, fill = 'green')

# drawCircle(cvs, 450, 300, 50, fill='red')


# cvs.create_polygon(200, 250, 350, 250, 350, 350, 220, 300, fill='yellow')


# top.mainloop()
global cx
cx = 2000
global cy
cy = 1600

global alltime##x 
alltime = 1
global y
y = 0
## 画面缩放
global k## xk
k = 2.5
global yk
yk = 0.5
def cr(cvst, who, age, whenson, color):
    global y
    global alltime
    global cy
    global k 
    global yk
    cvst.create_rectangle(alltime/k, y/yk, (alltime+age)/k, (y+16)/yk, fill=color)
    cvst.pack()
    cvst.create_line((alltime+age)/k,0,(alltime+age)/k,cy,fill='black')
    if who == '挪亚*洪水':
        cvst.create_line((alltime+480)/k,0,(alltime+480)/k,cy,fill='red')
        cvst.create_line((alltime+600)/k,0,(alltime+600)/k,cy,fill='red')
        cvst.create_text((alltime+540)/k, (16)/yk, text='480挪亚方舟600', fill='red')
    msgtext = who + ':生:' + str(alltime) + '年:生子:' + str(whenson) + '岁:寿:' + str(age) + '岁:离:' + str(alltime+age) + '年'
    cvst.create_text((alltime+age//2)/k, (y+8)/yk, text=msgtext, fill='black')
    alltime = alltime + whenson
    y = y + 16
    
bibletime = tk.Tk()
bibletime.title('BibleTime...')

cvs = tk.Canvas(bibletime, width=cx, height=cy)
cvs.pack()



# cr(cvs, 'jinag', 1000, 70, 'yellow')
# cr(cvs, '恩', 900, 90, 'green')
# cr(cvs, 'dian', 800, 70, 'yellow')
## 上课补那些东西。。。
cr(cvs, '亚当' ,  930,  130,  'yellow')
cr(cvs, '塞特' ,  912,  105,  'green')
cr(cvs, '以挪士' ,  905,  90,  'yellow')
cr(cvs, '该南' ,  910,  70,  'green')
cr(cvs, '玛勒列' ,  895,  65,  'yellow')
cr(cvs, '雅列' ,  962,  162,  'green')
cr(cvs, '以诺' ,  365,  65,  'yellow')
cr(cvs, '玛土撒拉' ,  969,  187,  'green')
cr(cvs, '拉麦' ,  777,  182,  'yellow')
cr(cvs, '挪亚*洪水' ,  950,  502,  'green')
cr(cvs, '闪' ,  600,  100,  'yellow')
cr(cvs, '亚法撒' ,  438,  35,  'green')
cr(cvs, '沙拉' ,  433,  30,  'yellow')
cr(cvs, '希伯' ,  464,  34,  'green')
cr(cvs, '法勒' ,  239,  30,  'yellow')
cr(cvs, '拉吴' ,  239,  32,  'green')
cr(cvs, '西鹿' ,  230,  30,  'yellow')
cr(cvs, '拿鹤' ,  148,  29,  'green')
cr(cvs, '他拉' ,  205,  130,  'yellow')
cr(cvs, '亚伯拉罕' ,  175,  100,  'green')
cr(cvs, '以撒' ,  180,  60,  'yellow')
cr(cvs, '雅各' ,  147,  55,  'green')## 以扫40岁娶迦南女子，雅各走娶妻，7年得妻，4子犹大
## 接下来的不知的寿命设为70岁，不知的生子年龄设为50岁
cr(cvs, '犹大*他玛' ,  120,  83,  'yellow')## 雅各见约瑟时130岁，约瑟见法老30岁，过9年左右，39岁约瑟，见130雅各，雅各91岁生约瑟，约瑟17岁被卖，此时，犹大63岁生三子，长大，娶妻他玛，生子约，83岁
cr(cvs, '法勒斯' ,  70,  50,  'green')


# cr(cvs, '希斯仑' ,  70,  50,  'yellow')
# cr(cvs, '亚兰' ,  70,  50,  'green')
# cr(cvs, '亚米拿达' ,  70,  50,  'yellow')
# cr(cvs, '拿顺' ,  70, 50,  'green')
# cr(cvs, '撒门*喇合' ,  70,  50,  'yellow')
# cr(cvs, '波阿斯*路得' ,  70,  50,  'green')
# cr(cvs, '俄备得' ,  70,  50,  'yellow')
# cr(cvs, '耶西' ,  70,  50,  'green')
# cr(cvs, '大卫*乌利亚妻' ,  70,  50,  'yellow')
# cr(cvs, '所罗门' ,  120,  50,  'green')
# cr(cvs, '罗波安' ,  120,  50,  'yellow')
# cr(cvs, '亚比雅' ,  120,  50,  'green')
# cr(cvs, '亚撒' ,  120,  50,  'yellow')
# cr(cvs, '约沙法' ,  120,  50,  'green')
# cr(cvs, '约兰' ,  120,  50,  'yellow')
# cr(cvs, '乌西亚' ,  120,  50,  'green')
# cr(cvs, '约坦' ,  120,  50,  'yellow')
# cr(cvs, '亚哈斯' ,  120,  50,  'green')
# cr(cvs, '希西家' ,  120,  50,  'yellow')
# cr(cvs, '玛拿西' ,  120,  50,  'green')
# cr(cvs, '亚们' ,  120,  50,  'yellow')
# cr(cvs, '约西亚' ,  120,  50,  'green')
# cr(cvs, '耶哥尼雅' ,  120, 50 ,  'yellow')
# cr(cvs, '撒拉铁' ,  120,  50,  'green')
# cr(cvs, '所罗巴伯' ,  120, 50 ,  'yellow')
# cr(cvs, '亚比玉' ,  120, 50 ,  'green')
# cr(cvs, '以利亚敬' ,  120,  50,  'yellow')
# cr(cvs, '亚所' ,  120,  50,  'green')
# cr(cvs, '撒督' , 120 ,  50,  'yellow')
# cr(cvs, '亚金' ,  120,  50,  'green')
# cr(cvs, '以律' ,  120, 50 ,  'yellow')
# cr(cvs, '以利亚撒' ,  120,  50,  'green')
# cr(cvs, '马但' , 120 ,  50,  'yellow')
# cr(cvs, '雅各' ,  120,  50,  'green')
# cr(cvs, '约瑟*马利亚' , 120 ,50  ,  'yellow')
# cr(cvs, '耶稣' ,  33,  0,  'green')






















# cvs.create_rectangle(50, 50, 100, 100, fill='red')## x1, y1, x2, y2...

bibletime.mainloop()
