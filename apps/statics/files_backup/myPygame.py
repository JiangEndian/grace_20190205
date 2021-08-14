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
clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()
moneySprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
running = True
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
def loadImgs(imgDir, imgRange, imgName):
    imgs = []
    for i in range(imgRange):
        imgs.append(loadImg(imgDir, str(i)+imgName))
    return imgs
def loadFont(fontName = 'arial'):
    if fontName != 'arial':
        return os.path.join((fontName))
    else:
        return pygame.font.match_font(fontName)
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
def scaleImg4Animation(img, width, height, numbers):
    scaleImgs = []
    onceScaleWidth = int(width / numbers)
    onceScaleHeight = int(height / numbers)
    for once in range(numbers):
        scaleImgs.append(pygame.transform.scale(img, (width, height)))
        width -= onceScaleWidth
        height -= onceScaleHeight
    return scaleImgs
#画文字，画矩形，画开始

#检测事件
def checkEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.quit()
            return False
    return True

#sprite类，需要图，rect位置，然后是update，自己加入allSprites，在这里测试
class Heart(pygame.sprite.Sprite): #玩家操作的
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
    
        self.images = loadImgs('hearts', 101, 'heart.png')
        self.imageNumber = 0
        self.image = self.images[self.imageNumber]
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.5 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
    
        self.rect.centerx = width/2 #这里的不能用上面的
        self.rect.centery = height/2
            
        self.speedx = 7
        self.speedy = 7
        
    def update(self):
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
        if self.imageNumber > 100:
            self.imageNumber = 100

class Money(pygame.sprite.Sprite): #自己行动的
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)
        self.add(moneySprites) #在别的文件里定义的，这里用不了，限定在一个文件内
    
        self.image = pygame.transform.scale(loadImg('hearts', 'money.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.65 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
    
        #self.rect.x = random.randrange(1, width-self.rect.width-1)
        #self.rect.y = random.randrange(1, height-self.rect.height+1)
        self.rect.x = 1 #改为都从左上角出来
        self.rect.y = 1

        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 10)

        
    def update(self):
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
    
class MoneyAbsorb(pygame.sprite.Sprite): #动画效果的
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)
        
        self.imageOri = pygame.transform.scale(loadImg('hearts', 'money.png'), (200, 200))
        self.images = scaleImg4Animation(self.imageOri, 200, 200, 20)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
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
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
###3.必要用的函数和类########################


###4.开始游戏设定与循环########################
width = 1200
height = 800
screen = startPygame(width, height)
heart = Heart() #三个类都在myPygame里，别的用的时候，需要重新定义
for i in range(10): 
    Money()

while running:
    #大世界交互规则
    running = checkEvent()
    
    hits = pygame.sprite.spritecollide(heart, moneySprites, True, pygame.sprite.collide_circle)
    for hit in hits:
        absorbAnim = MoneyAbsorb(heart.rect.center) 
        #判断动画结束为absorbAnim.alive()
        Money()
        Money()
        heart.blacken() 
    #大世界交互规则

    #更新显示画面
    clock.tick(60)
    screen.fill(BLACK)
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.update()

pygame.quit()
###4.开始游戏设定与循环########################
