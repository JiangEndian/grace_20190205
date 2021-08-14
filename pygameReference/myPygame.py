#!/usr/bin/env python3

#安装库：pip3 install pygame numpy opencv-python 
###1.导入语言包##############################
import pygame
#sprite, 小精灵，游戏的所有元素
import random
import os
import numpy as np
import cv2
###1.导入语言包##############################

###2.一些常数################################
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
GOLD = (255, 215, 0)
SKYBLUE = (135, 206, 235)
GRAY = '#808080'
clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()
moneySprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
heartSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
deathSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
aliveSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
running = True
paused = False
global allMoneys
allMoneys = 0
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
def loadFont(fontName = 'arial'):
    if fontName != 'arial':
        return os.path.join((fontName))
    else:
        return pygame.font.match_font(fontName)
defaultFont = loadFont()
def textImg(text, imgW=50, imgH=40, textSize=20, font=defaultFont, color=WHITE, colorKey=BLACK):
    textSurf = pygame.font.Font(font, textSize).render(text, True, color)
    #居中方法1
    #img = pygame.Surface((imgW, imgH))
    #textW = textSurf.get_width()
    #textH = textSurf.get_height()
    #img.blit(textSurf, [imgW/2-textW/2, imgH/2-textH/2]) #以左上角来居中
    #居中方法2
    img = pygame.Surface((imgW, imgH))
    text_rect = textSurf.get_rect()
    text_rect.centerx = imgW/2
    text_rect.centery = imgH/2 #以中居中，更容易理解
    img.blit(textSurf, text_rect) #虽一样还多一行，但于我而言更容易理解。。。
    img.set_colorkey(colorKey)
    return img
def text2Img(text, textSize=20, font=defaultFont, color=WHITE, colorKey=BLACK):
    textSurf = pygame.font.Font(font, textSize).render(text, True, color)
    #居中方法1
    #img = pygame.Surface((imgW, imgH))
    #textW = textSurf.get_width()
    #textH = textSurf.get_height()
    #img.blit(textSurf, [imgW/2-textW/2, imgH/2-textH/2]) #以左上角来居中
    #居中方法2
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


#sprite类，需要图，rect位置，然后是update，自己加入allSprites，在这里测试
class Heart(pygame.sprite.Sprite): #玩家操作的
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        #self.textImg = textImg('♥', 200, 200, 180, color=RED)
        self.imgNums = 255
        self.images = textImgsWHITE2BLACK('♥', 200, 200, 180, self.imgNums)
    
        #self.images = loadImgs('hearts', 101, 'heart.png')
        self.imageNumber = 0
        self.image = self.images[self.imageNumber]
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.5 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
    
        self.rect.centerx = width/2 #这里的不能用上面的
        self.rect.centery = height/2
            
        self.speedx = 7
        self.speedy = 7
    
        self.lifetime = 0
        self.born = pygame.time.get_ticks()
        self.alive = True
        
    def update(self):
        if self.alive:
            self.lifetime = (pygame.time.get_ticks() - self.born)/1000
        #print(self.lifetime)
        
        self.image = self.images[self.imageNumber]

        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if keyPressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if keyPressed[pygame.K_UP]:
            self.rect.y -= self.speedy
        if keyPressed[pygame.K_DOWN]:
            self.rect.y += self.speedy
            
    
    def blacken(self):
        self.imageNumber += 1
        if self.imageNumber >= self.imgNums:
            self.imageNumber = self.imgNums-1
            self.alive = False #死而又死。。。真是。。。

class AutoHeart(pygame.sprite.Sprite): #自动的
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
        self.add(heartSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
        self.add(aliveSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.deathImg = text2Img('♥', 90, color=GRAY)
        self.imgNums = 25
        self.images = textImgsWHITE2BLACK('♥', 50, self.imgNums)
    
        #self.images = loadImgs('hearts', 101, 'heart.png')
        self.imageNumber = 0
        self.image = self.images[self.imageNumber]
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.9 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
    
        self.rect.centerx = width/2 #这里的不能用上面的
        self.rect.centery = height/2
            
        #self.speedx = 7
        #self.speedy = 7
    
        self.lifetime = 0
        self.born = pygame.time.get_ticks()
        self.alive = True
        self.money = 0
        
        self.speedx_range = 7
        self.speedy_range = 5
        
        self.speedx = 0
        self.speedy = 0
        #保持方向时除以自身的绝对值，但不能为0
        while self.speedx == 0:
            self.speedx = random.randrange(-self.speedx_range, self.speedx_range)
        while self.speedy == 0:
            self.speedy = random.randrange(-self.speedy_range, self.speedy_range)
    
    def checkBorder(self):
        #判断返回
        if self.rect.right > width: #这种方法保持方向，重新获得速度（非0）
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.right = width
            self.speedx = -self.speedx/abs(self.speedx) * random.randrange(1, self.speedx_range)
        if self.rect.left < 0:
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.left = 0
            self.speedx = -self.speedx/abs(self.speedx) * random.randrange(1, self.speedx_range)
        if self.rect.bottom > height:
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.bottom = height
            self.speedy = -self.speedy/abs(self.speedy) * random.randrange(1, self.speedy_range)
        if self.rect.top < 0:
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.top = 0
            self.speedy = -self.speedy/abs(self.speedy) * random.randrange(1, self.speedy_range)

    def update(self):
        self.checkBorder()
        #自动走的
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.alive:
            self.lifetime = (pygame.time.get_ticks() - self.born)/1000
            #print(self.lifetime)
        
            self.image = self.images[self.imageNumber]
            
            center = self.rect.center
            self.rect = self.image.get_rect()
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            #先画在图片上，之后再把图片移位，先移位了再画，就是刻舟求剑了
            self.rect.center = center
    
            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if keyPressed[pygame.K_RIGHT]:
                self.rect.x += self.speedx
            if keyPressed[pygame.K_UP]:
                self.rect.y -= self.speedy
            if keyPressed[pygame.K_DOWN]:
                self.rect.y += self.speedy
        #else: #本来是死亡判断的，但死后不断的换一个图片没必要。就尸体一个即可
    
    def blacken(self):
        self.money += 1
        if self.alive:
            for i in range(20):
                Money()
            self.imageNumber += 1
            if self.imageNumber >= self.imgNums:
                self.imageNumber = self.imgNums-1
                self.alive = False 
                
                self.image = self.deathImg #死后开始大量吸收，让他人无钱可吸
            
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.radius = self.rect.width * 0.9 / 2
                #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
                self.rect.center = center #画完之后，就是默认左上角，需要移到原位
                self.speedx_range *= 10
                self.speedy_range *= 10
                self.speedx *= 10
                self.speedy *= 10
                self.remove(aliveSprites)
                self.add(deathSprites)

class Money(pygame.sprite.Sprite): #自己行动的
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)
        self.add(moneySprites) #在别的文件里定义的，这里用不了，限定在一个文件内
        #allMoneys += 1 #奇怪，上面的直接就能引用外面的，这个就不行。。。
        #addOneMoney()
        #但能直接引用函数。然后函数能直接用外面的，但不能直接操作外面的
        global allMoneys #直接全球操作吧
        allMoneys += 1
        self.textImg = textImg('$', 30, 30, 30, color=GOLD)
        #self.images = textImgs(self.textImg, 100)
        self.image = self.textImg

        #self.image = pygame.transform.scale(loadImg('hearts', 'money.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.9 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
    
        self.rect.x = random.randrange(1, width-self.rect.width-1)
        self.rect.y = random.randrange(1, height-self.rect.height+1)
        #self.rect.x = 1 #改为都从左上角出来
        #self.rect.y = 1

        self.speedx = random.randrange(-4, 4)
        self.speedy = random.randrange(-3, 3)
        #钱不动人动的吧
        self.speedx = 0
        self.speedy = 0

        
    def update_notuse(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #判断返回
        if self.rect.right > width:
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.speedx = -self.speedx
        if self.rect.bottom > height:
            self.speedy = -self.speedy
        if self.rect.top < 0:
            self.speedy = -self.speedy
    
class MoneyAbsorb(pygame.sprite.Sprite): #动画效果，跟随的
    def __init__(self, followedSprite):
        #def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)
        self.followedSprite = followedSprite
        
        self.imgW = 40
        self.imgH = 40
        self.fontS = 40
        self.textImg = textImg('$', self.imgW, self.imgH, self.fontS, color=GOLD)
        #self.images = textImgs(self.textImg, 20)
        self.imageOri = self.textImg
        
        #self.imageOri = pygame.transform.scale(loadImg('hearts', 'money.png'), (200, 200))
        self.images = scaleImg4Animation(self.imageOri, self.imgW, self.imgH, 40)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        #self.rect.center = center
        self.rect.center = self.followedSprite.rect.center
        self.frame = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.frame_rate = 30
        
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > self.frame_rate:
            self.lastUpdate = now
            self.frame += 1
            if self.frame > (len(self.images)-1):
                self.kill()
            else:
                self.image = self.images[self.frame]
                #center = self.rect.center
                self.rect = self.image.get_rect()
                #self.rect.center = center
                self.rect.center = self.followedSprite.rect.center
###3.必要用的函数和类########################


###4.开始游戏设定与循环########################
width = 1200
height = 700
screen = startPygame(width, height)
#heart = Heart() #三个类都在myPygame里，别的用的时候，需要重新定义
for i in range(6): 
    Money()
    Money()
    AutoHeart() #三个类都在myPygame里，别的用的时候，需要重新定义

while running:
    clock.tick(60)
    #大世界交互规则
    for event in pygame.event.get(): #只能获得一次，多次判断放一起
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
            #得先判断type不然没有key会出错
                paused = not paused
        #if event.type==pygame.MOUSEBUTTONDOWN and event.button==1/2/3
        #if pygame.mouse.get_pressed()[0]/1/2 #只能获得一次，要多次判断，放一起
        #keyPressed = pygame.key.get_pressed() #
        #if keyPressed[pygame.K_LEFT]:
    if paused or len(moneySprites)==0:
        continue

    #hits = pygame.sprite.spritecollide(heart, moneySprites, True, pygame.sprite.collide_circle)
    hits = pygame.sprite.groupcollide(heartSprites, moneySprites, False, True, pygame.sprite.collide_circle)
    for heart in hits: #[{heart:money}, ]
        #absorbAnim = MoneyAbsorb(heart.rect.center) 
        absorbAnim = MoneyAbsorb(heart) 
        #判断动画结束为absorbAnim.alive()
        #Money() #把碰撞生成钱的精灵里，就是blacken里       
        for money in hits[heart]:
            heart.blacken() #其实这个碰撞的结果是一个字典的列表，遍历列表是heart的字典，遍历那字典才是碰到的money的列表
    hits = pygame.sprite.groupcollide(aliveSprites, deathSprites, False, False, pygame.sprite.collide_circle)
    for hit in hits:
    #if len(hits) >= 2: #不是和自己一组的撞了，有一个就是撞了现在
        hit.rect.x -= heart.speedx 
        hit.rect.y -= heart.speedy
        hit.speedx *= -1
        hit.speedy *= -1
        
    
    #大世界交互规则

    #更新显示画面
    screen.fill(BLACK)
    #screen.fill(SKYBLUE)
    allSprites.update()
    allSprites.draw(screen)
    for heart in heartSprites:
        draw_text(screen, str(heart.lifetime), 20, heart.rect.centerx, heart.rect.y, font=defaultFont, color=RED)
        draw_text(screen, str(heart.money), 20, heart.rect.centerx, heart.rect.bottom, font=defaultFont, color=GOLD)
        
    draw_text(screen, str(allMoneys), 20, width/2, 1, font=defaultFont, color=GOLD)
    #这个画字，用在sprite里不好使，在这里，还得在sprite更新draw完后
    pygame.display.update()

pygame.quit()
###4.开始游戏设定与循环########################
