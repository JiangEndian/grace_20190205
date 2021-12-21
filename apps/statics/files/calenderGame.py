#!/usr/bin/env python3

#安装库：pip3 install pygame numpy opencv-python 
###1.导入语言包##############################
import pygame
#sprite, 小精灵，游戏的所有元素
import random
import os
import numpy as np
import cv2
from MyPython3 import *
import jewishcalendar, torah
###1.导入语言包##############################

def getJewishMonthName(month, year):
    if month == 1:
        return "Nisan"
    elif month == 2:
        return "Iyyar"
    elif month == 3:
        return "Sivan"
    elif month == 4:
        return "Tammuz"
    elif month == 5:
        return "Av"
    elif month == 6:
        return "Elul"
    elif month == 7:
        return "Tishri"
    elif month == 8:
        return "Heshvan"
    elif month == 9:
        return "Kislev"
    elif month == 10:
        return "Teveth"
    elif month == 11:
        return "Shevat"
    elif month == 12:
        if jewishcalendar.hebrew_leap(year):
            return "Adar I"
        else:
            return "Adar"

    elif month == 13:
        return "Adar II"

#A list of the holidays with their dates and remarks for calculation is available here. https://www.david-greve.de/luach-code/holidays.html
#The following function calculate_holiday takes a Gregorian date and a flag whether for Diaspora is calculated or not, and returns a list of holiday names.
# Returns the weekday from a given hebrew date (0 for Sunday,
# 1 for Monday,...)
def getWeekdayOfHebrewDate(hebDay, hebMonth, hebYear):
  absdate = jewishcalendar.hebrew_to_absdate(hebYear, hebMonth, hebDay)
  return jewishcalendar.get_weekday_from_absdate(absdate)

def calculate_holiday(g_day, g_month, g_year, diaspora):
  absdate = jewishcalendar.gregorian_to_absdate(g_year, g_month, g_day)
  hebYear, hebMonth, hebDay = jewishcalendar.absdate_to_hebrew(absdate)

  listHolidays = []
  
  if hebDay == 1:
    listHolidays.append("New Moon")

  # Holidays in Nisan

  hagadolDay = 14
  while getWeekdayOfHebrewDate(hagadolDay, 1, hebYear) != 6:
    hagadolDay -= 1
  if hebDay == hagadolDay and hebMonth == 1:
    listHolidays.append("Shabat Hagadol")

  if hebDay == 14 and hebMonth == 1:
    listHolidays.append("Erev Pesach")
  if hebDay == 15 and hebMonth == 1:
    listHolidays.append("Pesach I")
  if hebDay == 16 and hebMonth == 1:
    if diaspora:
      listHolidays.append("Pesach II")
    else:
      listHolidays.append("Chol Hamoed")
  if hebDay == 17 and hebMonth == 1:
    listHolidays.append("Chol Hamoed")
  if hebDay == 18 and hebMonth == 1:
    listHolidays.append("Chol Hamoed")
  if hebDay == 19 and hebMonth == 1:
    listHolidays.append("Chol Hamoed")
  if hebDay == 20 and hebMonth == 1:
    listHolidays.append("Chol Hamoed")
  if hebDay == 21 and hebMonth == 1:
    if not diaspora:
      listHolidays.append("Pesach VII (Yizkor)")
    else:
      listHolidays.append("Pesach VII")
  if hebDay == 22 and hebMonth == 1:
    if diaspora:
      listHolidays.append("Pesach VIII (Yizkor)")

  # Yom Hashoah

  if getWeekdayOfHebrewDate(27, 1, hebYear) == 5:
    if hebDay == 26 and hebMonth == 1:
      listHolidays.append("Yom Hashoah")
  elif hebYear >= 5757 and getWeekdayOfHebrewDate(27, 1, hebYear) == 0:
    if hebDay == 28 and hebMonth == 1:
      listHolidays.append("Yom Hashoah")
  else:
    if hebDay == 27 and hebMonth == 1:
      listHolidays.append("Yom Hashoah")

  # Holidays in Iyar

  # Yom Hazikaron

  if getWeekdayOfHebrewDate(4, 2, hebYear) == 5: # If 4th of Iyar is a Thursday ...
    if hebDay == 2 and hebMonth == 2: # ... then Yom Hazicaron is on 2th of Iyar
      listHolidays.append("Yom Hazikaron")
  elif getWeekdayOfHebrewDate(4, 2, hebYear) == 4:
    if hebDay == 3 and hebMonth == 2:
        listHolidays.append("Yom Hazikaron")
  elif hebYear >= 5764 and getWeekdayOfHebrewDate(4, 2, hebYear) == 0:
    if hebDay == 5 and hebMonth == 2:
      listHolidays.append("Yom Hazikaron")
  else:
    if hebDay == 4 and hebMonth == 2:
      listHolidays.append("Yom Hazikaron")

  # Yom Ha'Azmaut

  if getWeekdayOfHebrewDate(5, 2, hebYear) == 6:
    if hebDay == 3 and hebMonth == 2:
      listHolidays.append("Yom Ha'Atzmaut")
  elif getWeekdayOfHebrewDate(5, 2, hebYear) == 5:
    if hebDay == 4 and hebMonth == 2:
      listHolidays.append("Yom Ha'Atzmaut")
  elif hebYear >= 5764 and getWeekdayOfHebrewDate(4, 2, hebYear) == 0:
    if hebDay == 6 and hebMonth == 2:
      listHolidays.append("Yom Ha'Atzmaut")
  else:
    if hebDay == 5 and hebMonth == 2:
      listHolidays.append("Yom Ha'Atzmaut")

  if hebDay == 14 and hebMonth == 2:
    listHolidays.append("Pesach Sheni")
  if hebDay == 18 and hebMonth == 2:
    listHolidays.append("Lag B'Omer")
  if hebDay == 28 and hebMonth == 2:
    listHolidays.append("Yom Yerushalayim")

  # Holidays in Sivan

  if hebDay == 5 and hebMonth == 3:
    listHolidays.append("Erev Shavuot")
  if hebDay == 6 and hebMonth == 3:
    if diaspora:
      listHolidays.append("Shavuot I")
    else:
      listHolidays.append("Shavuot\n(Yizkor)")
  if hebDay == 7 and hebMonth == 3:
    if diaspora:
      listHolidays.append("Shavuot II\n(Yizkor)")

  # Holidays in Tammuz

  if getWeekdayOfHebrewDate(17, 4, hebYear) == 6:
    if hebDay == 18 and hebMonth == 4:
      listHolidays.append("Fast of Tammuz")
  else:
    if hebDay == 17 and hebMonth == 4:
      listHolidays.append("Fast of Tammuz")

  # Holidays in Av

  if getWeekdayOfHebrewDate(9, 5, hebYear) == 6:
    if hebDay == 10 and hebMonth == 5:
      listHolidays.append("Fast of Av")
  else:
    if hebDay == 9 and hebMonth == 5:
      listHolidays.append("Fast of Av")
  if hebDay == 15 and hebMonth == 5:
    listHolidays.append("Tu B'Av")

  # Holidays in Elul

  if hebDay == 29 and hebMonth == 6:
    listHolidays.append("Erev Rosh Hashana")

  # Holidays in Tishri

  if hebDay == 1 and hebMonth == 7:
    listHolidays.append("Rosh Hashana I")
  if hebDay == 2 and hebMonth == 7:
    listHolidays.append("Rosh Hashana II")
  if getWeekdayOfHebrewDate(3, 7, hebYear) == 6:
    if hebDay == 4 and hebMonth == 7:
      listHolidays.append("Tzom Gedaliah")
  else:
    if hebDay == 3 and hebMonth == 7:
      listHolidays.append("Tzom Gedaliah")
  if hebDay == 9 and hebMonth == 7:
    listHolidays.append("Erev Yom Kippur")
  if hebDay == 10 and hebMonth == 7:
    listHolidays.append("Yom Kippur\n(Yizkor)")
  if hebDay == 14 and hebMonth == 7:
    listHolidays.append("Erev Sukkot")
  if hebDay == 15 and hebMonth == 7:
    if diaspora:
      listHolidays.append("Sukkot I")
    else:
      listHolidays.append("Sukkot")
  if hebDay == 16 and hebMonth == 7:
    if diaspora:
      listHolidays.append("Sukkot II")
    else:
      listHolidays.append("Chol Hamoed")
  if hebDay == 17 and hebMonth == 7:
    listHolidays.append("Chol Hamoed")
  if hebDay == 18 and hebMonth == 7:
    listHolidays.append("Chol Hamoed")
  if hebDay == 19 and hebMonth == 7:
    listHolidays.append("Chol Hamoed")
  if hebDay == 20 and hebMonth == 7:
    listHolidays.append("Chol Hamoed")
  if hebDay == 21 and hebMonth == 7:
    listHolidays.append("Hoshana Raba")
  if hebDay == 22 and hebMonth == 7:
    if not diaspora:
      listHolidays.append("Shemini Atzereth\n(Yizkor)")
      listHolidays.append("Simchat Torah")
    else:
      listHolidays.append("Shemini Atzereth\n(Yizkor)")
  if hebDay == 23 and hebMonth == 7:
    if diaspora:
      listHolidays.append("Simchat Torah")

  # Holidays in Kislev

  if hebDay == 25 and hebMonth == 9:
    listHolidays.append("Chanukka I")
  if hebDay == 26 and hebMonth == 9:
    listHolidays.append("Chanukka II")
  if hebDay == 27 and hebMonth == 9:
    listHolidays.append("Chanukka III")
  if hebDay == 28 and hebMonth == 9:
    listHolidays.append("Chanukka IV")
  if hebDay == 29 and hebMonth == 9:
    listHolidays.append("Chanukka V")
  # Holidays in Tevet

  if hebDay == 10 and hebMonth == 10:
    listHolidays.append("Fast of Tevet")

  if jewishcalendar.hebrew_month_days(hebYear, 9) == 30:
    if hebDay == 30 and hebMonth == 9:
      listHolidays.append("Chanukka VI")
    if hebDay == 1 and hebMonth == 10:
      listHolidays.append("Chanukka VII")
    if hebDay == 2 and hebMonth == 10:
      listHolidays.append("Chanukka VIII")
  if jewishcalendar.hebrew_month_days(hebYear, 9) == 29:
    if hebDay == 1 and hebMonth == 10:
      listHolidays.append("Chanukka VI")
    if hebDay == 2 and hebMonth == 10:
      listHolidays.append("Chanukka VII")
    if hebDay == 3 and hebMonth == 10:
      listHolidays.append("Chanukka VIII")

  # Holidays in Shevat

  if hebDay == 15 and hebMonth == 11:
    listHolidays.append("Tu B'Shevat")

  # Holidays in Adar (I)/Adar II

  if jewishcalendar.hebrew_leap(hebYear):
    monthEsther = 13
  else:
    monthEsther = 12
    
  if getWeekdayOfHebrewDate(13, monthEsther, hebYear) == 6:
    if hebDay == 11 and hebMonth == monthEsther:
      listHolidays.append("Fast of Esther")
  else:
    if hebDay == 13 and hebMonth == monthEsther:
      listHolidays.append("Fast of Esther")

  if hebDay == 14 and hebMonth == monthEsther:
    listHolidays.append("Purim")
  if hebDay == 15 and hebMonth == monthEsther:
    listHolidays.append("Shushan Purim")

  if jewishcalendar.hebrew_leap(hebYear):
    if hebDay == 14 and hebMonth == 12:
      listHolidays.append("Purim Katan")
    if hebDay == 15 and hebMonth == 12:
      listHolidays.append("Shushan Purim Katan")

  return listHolidays

def getDaysHolidays(gYear, gMonth, gDay):
    holidays = calculate_holiday(gDay, gMonth, gYear, diaspora=True)
    #print(holidays)
    return holidays

#Calculating weekly torah sections
#The function getTorahSections in torah.py expects the Jewish month, day and year of the Shabbat and a boolean whether to calculate for diaspora (True) or Israel (False) and returns a string with the torah sections or an empty string if there are no torah sections on that day.
def getDaysTorah(gYear, gMonth, gDay):
#for i in range(366):
    diaspora = True
    torahStr = torah.getTorahSections(gMonth, gDay, gYear, diaspora)
    if torahStr != "":
        #print("Torah section(s): " + torahStr)
        return "Torah section(s): " + torahStr
    else:
        #print("No torah section(s) on that day")
        return None

def getMonthTorah():
    today = getdaystime(0)
    year = int(today[:4])
    month = int(today[4:6])
    #gDay = int(today[6:8])
    day = '-'
    diaspora = True
    lastDay = jewishcalendar.last_day_of_gregorian_month(month, year)
    torahMonth = []
    for day in range(1,lastDay+1):
        torahStr = torah.getTorahSections(month, day, year, diaspora)
        if torahStr != "":
            print(str(day) + "." + str(month) + "."+str(year) + ": " + torahStr)
            torahMonth.append(str(day) + "." + str(month) + "."+str(year) + ": " + torahStr)
    return torahMonth

'''
###附：常用重要函数##########################
bin(8) #0b1000，转为2进行
oct(8) #0o10，转为8进制
hex(16) #0x10，转为16进制
divmod(7, 3) #(2, 1) #商和余数的元组
round(10.2222, 2) #10.22，返回浮点数的四舍五入值
pow(x, y) #x**y
sum() #对可迭代对象求和
min() #返回所有参数的最小值
max() #最大值
list() #创建或把序列转为列表
tuple() #转为元组
dict(a='a', b='b', t='t') #{'a': 'a', 'b': 'b', 't': 't'}
dict(zip(['one', 'two', 'three'], [1, 2, 3])) #{'three': 3, 'two': 2, 'one': 1} 
dict([('one', 1), ('two', 2), ('three', 3)]) #{'three': 3, 'two': 2, 'one': 
set() #生成个不重复的元素集，删除重复的。还可以计算交集、差集、并集
ord('A') #65，查看某个ascii对应的十进制数
chr(65) #'A'，反向ord
ascii('中国') #"'\\u4e2d\\u56fd'" 返回任何对象的可读版本。
sorted(iterable, key=None, reverse=False) #排序，
sorted(L, key=lambda x:x[1]) #每个输入的x的x[1]
#sort 是应用在list 的方法，无返回
#sorted可以对所有可迭代的对象进行排序操作，返回个新的list
reversed(seq) #返回一个反转的迭代器
slice(start, stop[, step]) #a[slice(0,5,2)] #等价于a[0:5:2]
all() #如果迭代器(元组或列表)的所有元素都为真，那么返回True，否则返回False
any() #如果迭代器里有一个元素为真，那么返回True，否则返回False
map(function, iterable) #会根据提供的函数对指定序列做映射。返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器
exec() #执行储存在字符串或文件中的Python语句，更复杂
hash() #返回该对象的哈希值
###附：常用重要函数##########################
'''

###2.一些常数################################
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
GOLD = (255, 215, 0)
SKYBLUE = (135, 206, 235)
GRAY = '#808080'
GOLD1 = '#D4AF37' #head
SILVER = '#C0C0C0' #breast and arms
BRONZE = '#CD7F32' #belly and thighs
IRON = '#a19d94' #legs
CLAY = '#b66a50' #feet part of Iron, part of clay
STONE = '#888c8d' #small, biggest one. 


clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()
running = True
paused = False
###2.一些常数################################

###3.必要用的函数和类########################
#修改图片的亮度和饱和度

#pygame的开始及设置
def startPygame(width, height, title='title'):
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen

#载入图片并设置colorKey，载入声音
def loadImg(imgDir, imgName, colorKey=BLACK):
    img = pygame.image.load(os.path.join(imgDir, imgName)).convert()
    img.set_colorkey(colorKey)
    return img
def loadImgs(imgDir, imgRange, imgName): #配合上面的reduceBrightness2Dark生成的数字开头的图片
    imgs = []
    for i in range(imgRange):
        imgs.append(loadImg(imgDir, str(i)+imgName))
    return imgs
def loadFont(fontName = 'arial'):
    if fontName != 'arial':
        return os.path.join((fontName))
    else:
        return pygame.font.match_font(fontName)
defaultFont = loadFont()

def textImg(text, imgW=50, imgH=40, textSize=20, font=defaultFont, color=WHITE, colorKey=BLACK):
    textSurf = pygame.font.Font(font, textSize).render(text, True, color)
    img = pygame.Surface((imgW, imgH))
    text_rect = textSurf.get_rect()
    text_rect.centerx = imgW/2
    text_rect.centery = imgH/2 #以中居中，更容易理解
    img.blit(textSurf, text_rect) #虽一样还多一行，但于我而言更容易理解。。。
    img.set_colorkey(colorKey)
    return img

def textsImg(texts, imgW=500, imgH=400, textSize=20, font=defaultFont, color=WHITE, colorKey=BLACK):
    textSurfs = []
    for text in texts:
        textSurfs.append(pygame.font.Font(font, textSize).render(text, True, color))
    img = pygame.Surface((imgW, imgH))
    
    height_all = 0

    for textSurf in textSurfs:
        text_rect = textSurf.get_rect()
        text_rect.x = 0
        text_rect.y = height_all
        height_all += 50

        img.blit(textSurf, text_rect) #虽一样还多一行，但于我而言更容易理解。。。
    img.set_colorkey(colorKey)
    return img

def textsImgBigSmall(texts, imgW=500, imgH=400, textSize=20, font=defaultFont, color=WHITE, colorKey=BLACK):
    textSurfs = []
    isFirst = True
    for text in texts:
        if isFirst:
            textSurfs.append(pygame.font.Font(font, textSize).render(text, True, color))
            isFirst = False
        else:
            textSurfs.append(pygame.font.Font(font, int(textSize/3*2)).render(text, True, color))
    img = pygame.Surface((imgW, imgH))
    
    height_all = 0

    for textSurf in textSurfs:
        text_rect = textSurf.get_rect()
        text_rect.centerx = imgW/2
        text_rect.y = height_all
        height_all += 30

        img.blit(textSurf, text_rect) #虽一样还多一行，但于我而言更容易理解。。。
    img.set_colorkey(colorKey)
    return img

def textsImgBigSmallWithYellowBack(texts, imgW=500, imgH=400, textSize=20, font=defaultFont, color=WHITE, colorKey=BLACK):
    textSurfs = []
    isFirst = True
    for text in texts:
        if isFirst:
            textSurfs.append(pygame.font.Font(font, textSize).render(text, True, color))
            isFirst = False
        else:
            textSurfs.append(pygame.font.Font(font, int(textSize/3*2)).render(text, True, color))
    img = pygame.Surface((imgW, imgH))
    img.fill(YELLOW)
    
    height_all = 0

    for textSurf in textSurfs:
        text_rect = textSurf.get_rect()
        text_rect.centerx = imgW/2
        text_rect.y = height_all
        height_all += 30

        img.blit(textSurf, text_rect) #虽一样还多一行，但于我而言更容易理解。。。
    img.set_colorkey(colorKey)
    return img

def text2Img(text, textSize=20, font=defaultFont, bold=False, color=WHITE, colorKey=BLACK):
    textObj = pygame.font.Font(font, textSize)
    textObj.set_bold(bold)
    textSurf = textObj.render(text, True, color)
    text_rect = textSurf.get_rect()
    imgW = text_rect.width #此时还未设置rect位置，就在左上角呢x/y/top/bottom/center
    imgH = text_rect.height
    img = pygame.Surface((imgW, imgH))
    text_rect.centerx = imgW/2
    text_rect.centery = imgH/2 #以中居中，更容易理解
    img.blit(textSurf, text_rect) #虽一样还多一行，但于我而言更容易理解。。。
    img.set_colorkey(colorKey)
    return img
def textImgsWHITE2BLACK(text, textSize=20, imgNums=255, font=defaultFont):
    textImgs = []
    stepReduce = int(255/imgNums)
    thisColor = 255
    for i in range(imgNums):
        thisColor -= stepReduce
        if thisColor < 1 or i == imgNums-1:
            thisColor = 1
        color = (thisColor, thisColor, thisColor)
        textSurf = pygame.font.Font(font, textSize).render(text, True, color)
        text_rect = textSurf.get_rect()
        imgW = text_rect.width #此时还未设置rect位置，就在左上角呢x/y/top/bottom/center
        imgH = text_rect.height
        img = pygame.Surface((imgW, imgH))
        text_rect.centerx = imgW/2
        text_rect.centery = imgH/2 #以中居中，更容易理解
        img.blit(textSurf, text_rect) #虽一样还多一行，但于我而言更容易理解。。。
        img.set_colorkey(BLACK)
        textImgs.append(img)
    return textImgs
def loadSound(soundDir, soundName, isBackground=False, volume=1):
    if isBackground:
        pygame.mixer.music.load(os.path.join(soundDir, soundName))
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
    else:
        sound = pygame.mixer.Sound(os.path.join(soundDir, soundName))
        return sound
def scaleImgs(imgs, width, height):
    new_imgs = []
    for img in imgs:
        new_imgs.append(pygame.transform.scale(img, (width, height)))
    return new_imgs
def scaleImg4Animation(img, width, height, numbers): #缩小至0
    scaleImgs = []
    onceScaleWidth = int(width / numbers)
    onceScaleHeight = int(height / numbers)
    for once in range(numbers):
        scaleImgs.append(pygame.transform.scale(img, (width, height)))
        width -= onceScaleWidth
        height -= onceScaleHeight
    return scaleImgs
#画文字，画矩形，画开始
def draw_text(surface, text, size, centerx, y, font=defaultFont, color=WHITE): #任意位置画字
    textSurf = pygame.font.Font(font, size).render(text, True, color)
    text_rect = textSurf.get_rect() #可以这样直接得到rect,也可以直接高宽
    text_rect.centerx = centerx #x居中，不用管多长
    text_rect.top = y #不用管多高，置顶，就向下排就行
    #text_rect.center = center #直接中心不方便调控
    #print(center) #(centerx, centery)
    surface.blit(textSurf, text_rect)
def draw_rect(surface, rectLength, rectHeight, x, y, outline=None, color=WHITE):
    rect2beDraw = pygame.Rect(x, y, rectLenght, rectHeight)
    pygame.draw.rect(surface, color, rect2beDraw, outline)

#sprite类，需要图，rect位置，然后是update，自己加入allSprites，在这里测试
###3.必要用的函数和类########################
class Day(pygame.sprite.Sprite):
    def __init__(self, absdate):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)
        self.isDay = True
        self.isSelected = False
        self.isDayWork = False

        gYear, gMonth, gDay = jewishcalendar.absdate_to_gregorian(absdate)
        self.heYear, self.heMonth, self.heDay = jewishcalendar.absdate_to_hebrew(absdate)
        self.weekday = jewishcalendar.get_weekday_from_absdate(absdate)
        self.weekNumber = int(datetime(gYear, gMonth, gDay).strftime('%U')) #.isocalendar()[1]是从周一算开始的，这个从周日算
        self.locationOfIsrael = (31.771959, 35.217018, 2, 754)
        self.sunRise = jewishcalendar.GetSunrise(gMonth, gDay, gYear, self.locationOfIsrael)
        self.sunSet = jewishcalendar.GetSunset(gMonth, gDay, gYear, self.locationOfIsrael)
        self.holidaysToday = getDaysHolidays(gYear, gMonth, gDay)
        self.torahToday = getDaysTorah(gYear, gMonth, gDay)
        
        self.absdate = absdate
        self.ymd = f'{gYear}' + f'{gMonth:02}' + f'{gDay:02}'
        #print(self.ymd)
        self.isToday = True

        #print(heYear, heMonth, heDay, weekday, "weekNumber" + str(self.weekNumber), sunRise, sunSet, holidaysToday, torahToday)
        
        self.rectWidth = 60
        self.rectHeight = 60
        #self.image = pygame.Surface((rectWidth, rectHeight))
        self.texts = []
        self.texts.append(str(gDay))
        self.texts.append(str(self.heDay))
        
        if len(self.holidaysToday) > 0 or self.weekday == 6:
            self.image = textsImgBigSmall(self.texts, self.rectWidth, self.rectHeight, 30, color=RED)
            self.color = RED
        else:
            self.image = textsImgBigSmall(self.texts, self.rectWidth, self.rectHeight, 30, color=BLUE)
            self.color = GRAY
        
        global centerWeekNumber

        self.rect = self.image.get_rect()
        self.rect.x = self.weekday*(self.rectWidth+10)

        if int(self.ymd) > int(today) and self.weekNumber < centerWeekNumber:
            self.rect.y = height/2 + (self.weekNumber+52-centerWeekNumber)*(self.rectHeight+10)
        else:
            self.rect.y = height/2 + (self.weekNumber-centerWeekNumber)*(self.rectHeight+10)
    
    def checkNextExist(self):
        for sprite in allSprites:
            if self.absdate+1 == sprite.absdate:
                return True
        Day(self.absdate+1)

    def checkPreviousExist(self):
        for sprite in allSprites:
            if self.absdate-1 == sprite.absdate:
                return True
        Day(self.absdate-1)
    
    def update(self):
        global centerWeekNumber
        today = getdaystime(0)
        if today == self.ymd and self.isToday: #都把自己当今天，但检查一下，确实就是第一个，就是今天
            self.isToday = True
            self.image = textsImgBigSmall(self.texts, self.rectWidth, self.rectHeight, 30, color=GREEN)
            self.color = GREEN
            self.rect.y = height/2
            centerWeekNumber = self.weekNumber
        elif today == self.ymd and not self.isToday: #上次证明了不是今天，但成为了今天
            allSprite.empty()
            allSprite.add(self)
            centerWeekNumber = self.weekNumber
            self.isToday = True
            self.rect.y = height/2
            self.isToday = True
        else: #不是今天，确认一次就知道了，以后是今天了，就再说
            self.isToday = False

        if self.isSelected:
            self.image = textsImgBigSmallWithYellowBack(self.texts, self.rectWidth, self.rectHeight, 30, color=self.color)
        else:
            self.image = textsImgBigSmall(self.texts, self.rectWidth, self.rectHeight, 30, color=self.color)
            

        if self.rect.top < height:
            self.checkNextExist()
        if self.rect.bottom > 0:
            self.checkPreviousExist()

class DayDetails(pygame.sprite.Sprite):
    def __init__(self, day):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)
        self.absdate = day.absdate
        self.isDay = False
        self.isDayWork = False

        #print(heYear, heMonth, heDay, weekday, "weekNumber" + str(self.weekNumber), sunRise, sunSet, holidaysToday, torahToday)

        texts = []
        texts.append(f'Week: {day.weekNumber}, Day: {day.weekday+1}.')
        texts.append(f'Jewish: {day.heYear}, {day.heMonth} {getJewishMonthName(day.heMonth, day.heYear)}, {day.heDay}')
        texts.append(f'Sunrise {day.sunRise[0]}:{day.sunRise[1]}, Sunset {day.sunSet[0]}:{day.sunSet[1]}')
        if day.holidaysToday:
            texts.append(f'Holidays: {day.holidaysToday}')
        if day.torahToday:
            texts.append(f'Torah: {day.torahToday}')
            print(day.torahToday)

        self.image = textsImg(texts, 700, 500, textSize = 40)
        
        self.rect = self.image.get_rect()
        self.rect.x = width/10*4
        self.rect.y = height/3*1
    
    def update(self):
        pass

class DayWork(pygame.sprite.Sprite):
    def __init__(self, day):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)
        self.absdate = day.absdate
        self.isDay = False
        self.isDayWork = True

        doubleDayWork = ['Hebrew / Greek study, Book translation, Blender, Math', 
                            'Review', 
                            'alt / Searching for tomorrow reading(ckhgeoe)']
        singleDayWork = ['Writing and Preaching', 
                            'Edit', 
                            'alt / Searching for tomorrow reading(ckhgeoe)']
        #print(day.weekday)

        if day.weekday+1 == 7:
            self.texts = ['rest', 'rest']
        elif day.weekday % 2 == 0:
            self.texts = doubleDayWork
        elif day.weekday % 2 == 1:
            self.texts = singleDayWork

        #print(heYear, heMonth, heDay, weekday, "weekNumber" + str(self.weekNumber), sunRise, sunSet, holidaysToday, torahToday)

        self.image = textsImg(self.texts, 700, 500, textSize = 30)
        print(self.texts)
        self.rect = self.image.get_rect()
        self.rect.x = width/10*4
        self.rect.y = height/10*7

        self.timeStamp = pygame.time.get_ticks()
        self.isWorking = False

        self.rest = False
        self.study = False
        self.soundStart = loadSound('.', 'didididi.wav')
        self.soundStop = loadSound('.', 'dinglinglingling.wav')
    
    def playRing(self, ring):
        if ring == 'start':
            self.soundStart.play()
        elif ring == 'stop':
            self.soundStop.play()
    def startWork(self):
        self.playRing('start')
        self.timeStamp = pygame.time.get_ticks()
        self.isWorking = True
        self.study = True
        self.image = textsImg(self.texts, 700, 500, textSize = 40, color=GREEN)
    def stopWork(self):
        self.isWorking = False
        self.image = textsImg(self.texts, 700, 500, textSize = 40, color=WHITE)

    def update(self):
        #一个番茄钟，点击就开始，再点击就停止
        if self.isWorking:
            if self.study:
                now = pygame.time.get_ticks()
                if now - self.timeStamp > 25*1000:
                    self.playRing('stop')
                    self.timeStamp = now
                    self.study = False
                    self.rest = True
            elif self.rest:
                now = pygame.time.get_ticks()
                if now - self.timeStamp > 5 * 1000:
                    self.playRing('start')
                    self.timeStamp = now
                    self.rest = False
                    self.study = True


###4.开始游戏设定与循环########################
width = 1340
height = 670
screen = startPygame(width, height)

today = getdaystime(0)
gYear = int(today[:4])
gMonth = int(today[4:6])
gDay = int(today[6:8])

global centerWeekNumber
centerWeekNumber = int(datetime(gYear, gMonth, gDay).strftime('%U')) #.isocalendar()[1]的是周一算第一天的

absdate = jewishcalendar.gregorian_to_absdate(gYear, gMonth, gDay)
day = Day(absdate)
dayDetails = DayDetails(day) 
dayWork = DayWork(day)

while running:
    clock.tick(1)
    #大世界交互规则
    for event in pygame.event.get(): #只能获得一次，多次判断放一起
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
            #得先判断type不然没有key会出错
                paused = not paused
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            for sprite in allSprites:
                sprite.isSelected = False
                if sprite.rect.collidepoint(event.pos):
                    if sprite.isDay: #对日历天数处理
                        dayDetails.kill()
                        dayWork.kill()
                        dayDetails = DayDetails(sprite)
                        dayWork = DayWork(sprite)
                        sprite.isSelected = True
                    elif sprite.isDayWork: #对番茄钟处理
                        if sprite.isWorking:
                            sprite.stopWork()
                        else:
                            sprite.startWork()
                    
        #if event.type==pygame.MOUSEBUTTONDOWN and event.button==1/2/3
        #if pygame.mouse.get_pressed()[0]/1/2 #只能获得一次，要多次判断，放一起
        #keyPressed = pygame.key.get_pressed() #
        #if keyPressed[pygame.K_LEFT]:
    if paused:
        continue

    #hits = pygame.sprite.spritecollide(heart, moneySprites, True, pygame.sprite.collide_circle)
    
    #hits = pygame.sprite.groupcollide(aliveSprites, deathSprites, False, False, pygame.sprite.collide_circle)
    
    #大世界交互规则

    #更新显示画面
    screen.fill(BLACK)
    #screen.fill(SKYBLUE)
    allSprites.update()
    allSprites.draw(screen)
    draw_text(screen, getnowtime('ymd'), 80, width/3*2, 10)
    draw_text(screen, getnowtime('hm'), 80, width/3*2, 80)

    #这个画字，用在sprite里不好使，在这里，还得在sprite更新draw完后
    pygame.display.update()

pygame.quit()
###4.开始游戏设定与循环########################
