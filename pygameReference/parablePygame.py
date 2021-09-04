#!/usr/bin/env python3

#安装库：pip3 install pygame numpy opencv-python 
###1.导入语言包##############################
import pygame
#sprite, 小精灵，游戏的所有元素
import random
import os
from get_data_list import data_list
###1.导入语言包##############################

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
moneySprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
heartSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
deathSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
aliveSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
running = True
paused = False
global allMoneys
###2.一些常数################################

###3.必要用的函数和类########################
#修改图片的亮度和饱和度
def editBrightness(inputImgPath, outputImgPath, brightness, saturation):
    MAX_VALUE = 100.0 #可调整的+-最大范围

    #读取，转化，并BGR转为HLS
    image = cv2.imread(inputImgPath, cv2.IMREAD_COLOR).astype(np.float32) / 255.0
    hlsImg = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    
    #调整亮度
    hlsImg[:, :, 1] = (1.0 + brightness / float(MAX_VALUE)) * hlsImg[:, :, 1]
    hlsImg[:, :, 1][hlsImg[:, :, 1] > 1] = 1
    #调整饱和度
    #hlsImg[:, :, 2] = (1.0 + saturation / float(MAX_VALUE)) * hlsImg[:, :, 2]
    #hlsImg[:, :, 2][hlsImg[:, :, 2] > 1] = 1

    #HLS转为BGR
    lsImg = cv2.cvtColor(hlsImg, cv2.COLOR_HLS2BGR) * 255
    lsImg = lsImg.astype(np.float32)
    cv2.imwrite(outputImgPath, lsImg)
def reduceBrightness2Dark(imgName, outPutDir):
    for i in range(101): #-100到100需要range(-100, 101)
        editBrightness(imgName, outPutDir+'/'+str(i)+imgName, -i, 0)
#reduceBrightness2Dark('heart.png', 'hearts') #成功生成0-100，减亮度的图片

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
def loadFont(fontName = 'font.ttf'):
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
        sound = pygame.mixer.Sound(os.path.join(SoundDir, soundName))
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
#年份制转换
def AA2BCorAD(aa):
    if aa < 3970:
        return '%dBC' % (3970-aa)
    else:
        return 'AD%d' % (aa-3969)

#sprite类，需要图，rect位置，然后是update，自己加入allSprites，在这里测试
class RoleOfImg(pygame.sprite.Sprite): #玩家操作的
    def __init__(self, RoleImg, x=None, y=None):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.imageRole = RoleImg
        self.image = RoleImg
        self.rect = self.image.get_rect()
        #self.radius = self.rect.width * 0.5 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        
        if x:
            self.rect.x = x
        else:
            self.rect.x = random.randrange(width) #这里的不能用上面的
        if y:
            self.rect.y = y
        else:
            self.rect.y = random.randrange(height)
        print((self.rect.x, self.rect.y))
            
        self.speedx = 3
        self.speedy = 3
    
        self.lifetime = 0
        self.born = pygame.time.get_ticks()
        self.alive = True
    
        self.elected = False
        
    def update(self):
        if self.alive:
            self.lifetime = (pygame.time.get_ticks() - self.born)/1000
        #print(self.lifetime)
        
        if self.elected:
            electedRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GOLD, electedRect, 3) #不加框线为填充
            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if keyPressed[pygame.K_RIGHT]:
                self.rect.x += self.speedx
            if keyPressed[pygame.K_UP]:
                self.rect.y -= self.speedy
            if keyPressed[pygame.K_DOWN]:
                self.rect.y += self.speedy

global allHeight
allHeight = 30
class RoleOfBTData(pygame.sprite.Sprite): #玩家操作的
    def __init__(self, data):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.startTime = data['start_time']
        self.passTime = data['pass_time']
        self.endTime = self.startTime + self.passTime
        self.startBCAD = AA2BCorAD(self.startTime)
        self.endBCAD = AA2BCorAD(self.endTime)
        self.name = data['name']
        self.story = data['story']

        self.title = 'AA%d-AA%d %s %s-%s' % (self.startTime, self.endTime, self.name, self.startBCAD, self.endBCAD)
        
        self.image = text2Img(self.title, 30)
        self.rect = self.image.get_rect()
        #self.radius = self.rect.width * 0.5 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.rect.x = self.startTime
        global allHeight
        self.rect.y = allHeight
        allHeight += self.rect.height
        
        self.speedx = 3
        self.speedy = 3
    
        self.lifetime = 0
        self.born = pygame.time.get_ticks()
        self.alive = True
    
        self.elected = False
        
    def update(self):
        if self.elected:
            electedRect = pygame.Rect(self.rect.x, self.rect.y, self.passTime, self.rect.height)
            pygame.draw.rect(screen, GOLD, electedRect, 3) #不加框线为填充
            '''keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if keyPressed[pygame.K_RIGHT]:
                self.rect.x += self.speedx
            if keyPressed[pygame.K_UP]:
                self.rect.y -= self.speedy
            if keyPressed[pygame.K_DOWN]:
                self.rect.y += self.speedy'''
        else:
            oriRect = pygame.Rect(self.rect.x, self.rect.y, self.passTime, self.rect.height)
            pygame.draw.rect(screen, GRAY, oriRect, 2) #不加框线为填充
    
class RoleOfTimeline(pygame.sprite.Sprite): #玩家操作的
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.image = pygame.Surface((7000, 3))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speedx = 3
        self.speedy = 3
    
        self.elected = False
        
    '''def update(self):
        if self.elected:
            electedRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GOLD, electedRect, 3) #不加框线为填充
            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if keyPressed[pygame.K_RIGHT]:
                self.rect.x += self.speedx
            if keyPressed[pygame.K_UP]:
                self.rect.y -= self.speedy
            if keyPressed[pygame.K_DOWN]:
                self.rect.y += self.speedy''' #不要移动

class RoleOfYearTag(pygame.sprite.Sprite): #玩家操作的
    def __init__(self, x=0, y=0, year=0):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.image = text2Img(str(year), 18)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speedx = 3
        self.speedy = 3
    
        self.elected = False
        
    '''def update(self):
        if self.elected:
            electedRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GOLD, electedRect, 3) #不加框线为填充
            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if keyPressed[pygame.K_RIGHT]:
                self.rect.x += self.speedx
            if keyPressed[pygame.K_UP]:
                self.rect.y -= self.speedy
            if keyPressed[pygame.K_DOWN]:
                self.rect.y += self.speedy'''

class Background(pygame.sprite.Sprite): #玩家操作的
    def __init__(self, x=0, y=0, year=0):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.image = text2Img(str(year), 18)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speedx = 3
        self.speedy = 3
    
        self.elected = False
        
    '''def update(self):
        if self.elected:
            electedRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GOLD, electedRect, 3) #不加框线为填充
            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if keyPressed[pygame.K_RIGHT]:
                self.rect.x += self.speedx
            if keyPressed[pygame.K_UP]:
                self.rect.y -= self.speedy
            if keyPressed[pygame.K_DOWN]:
                self.rect.y += self.speedy'''
###3.必要用的函数和类########################


###4.开始游戏设定与循环########################
width = 1200
height = 700
screen = startPygame(width, height)
def newTextRole(text, fontsize=30):
    role = text2Img(text, fontsize)
    RoleOfImg(role)

RoleOfTimeline()
for ix in [i*100 for i in range(70)]:
    RoleOfYearTag(ix, 3, ix)

for data in data_list:
    RoleOfBTData(data)

RoleOfTimeline(0, allHeight)
for ix in [i*100 for i in range(70)]:
    RoleOfYearTag(ix, allHeight-3, ix)
#newTextRole('亚当')

while running:
    clock.tick(60)
    #大世界交互规则
    for event in pygame.event.get(): #只能获得一次，多次判断放一起
        #if event.type==pygame.MOUSEBUTTONDOWN and event.button==1/2/3
        #if pygame.mouse.get_pressed()[0]/1/2 #只能获得一次，要多次判断，放一起
        #keyPressed = pygame.key.get_pressed() #
        #if keyPressed[pygame.K_LEFT]:
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                paused = not paused
            elif event.key == pygame.K_i:
                cmd = input('生成新角色或q退出: ')
                while cmd != 'q':
                    newTextRole(cmd)
                    cmd = input('生成新角色或q退出: ')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for role in allSprites:
                role.elected = False
                if role.rect.collidepoint(event.pos):
                    role.elected = True
    #全体的wsad
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_w]:
        for role in allSprites:
            role.rect.y += role.speedy*4
    if keyPressed[pygame.K_s]: 
        for role in allSprites:
            role.rect.y -= role.speedy*4
    if keyPressed[pygame.K_a]: 
        for role in allSprites:
            role.rect.x += role.speedx*3
    if keyPressed[pygame.K_d]: 
        for role in allSprites:
            role.rect.x -= role.speedx*3

    if paused:
        continue

    #hits = pygame.sprite.spritecollide(heart, moneySprites, True, pygame.sprite.collide_circle) 
    #hits = pygame.sprite.groupcollide(heartSprites, moneySprites, False, True, pygame.sprite.collide_circle) 
    
    #大世界交互规则

    #更新显示画面
    screen.fill(BLACK)
    #screen.fill(SKYBLUE)
    allSprites.update()
    allSprites.draw(screen)
    #这个画字，用在sprite里不好使，在这里，还得在sprite更新draw完后
    pygame.display.update()

pygame.quit()
###4.开始游戏设定与循环########################
