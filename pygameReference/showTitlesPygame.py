#!/usr/bin/env python3

#安装库：pip3 install pygame numpy opencv-python 
###1.导入语言包##############################
import pygame
#sprite, 小精灵，游戏的所有元素
import random
import os
###1.导入语言包##############################
titles = ['这是一个标题', 
        '短名字', 
        '长～名～字～', 
        '感叹']
width = 1300
height = 700

#游戏设计：边界/标题游走/选中放大/选中被碰撞
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
titleSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
electedSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
otherSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
running = True
backgroundImg = None
###2.一些常数################################

###3.必要用的函数和类########################
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


#sprite类，需要图，rect位置，然后是update，自己加入allSprites，在这里测试
class Title(pygame.sprite.Sprite): #自动的
    def __init__(self, title):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
        self.add(titleSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
        self.add(otherSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.imgTitle = text2Img(title, 50, font='font.ttf', color=GRAY)
        self.imgElected = text2Img(title, 100, font='font.ttf', bold=True, color=GOLD)
    
        #self.images = loadImgs('hearts', 101, 'heart.png')
        self.image = self.imgTitle
        self.rect = self.image.get_rect()
        #self.radius = self.rect.width * 0.5 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
    
        self.rect.centerx = width/2 #这里的不能用上面的
        self.rect.centery = height/2
            
        #self.speedx = 7
        #self.speedy = 7
    
        self.speedx = random.randrange(-4, 4)
        self.speedy = random.randrange(-3, 3)
        #保持方向时除以自身的绝对值，但不能为0
        while self.speedx == 0:
            self.speedx = random.randrange(-4, 4)
        while self.speedy == 0:
            self.speedy = random.randrange(-3, 3)

        self.name = title

    def update(self):
        if self in electedSprites:
            self.image = self.imgElected
        else:
            self.image = self.imgTitle
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        #自动走的
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #判断返回
        if self.rect.right > width: #这种方法保持方向，重新获得速度（非0）
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.right = width
            self.speedx = -self.speedx/abs(self.speedx) * random.randrange(1, 4)
        if self.rect.left < 0:
            #copy一个自己在另一边，继承速度
            self.rect.left = 0
            self.speedx = -self.speedx/abs(self.speedx) * random.randrange(1, 4)
        if self.rect.bottom > height:
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.bottom = height
            self.speedy = -self.speedy/abs(self.speedy) * random.randrange(1, 3)
        if self.rect.top < 0:
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.top = 0
            self.speedy = -self.speedy/abs(self.speedy) * random.randrange(1, 3)

###3.必要用的函数和类########################


###4.开始游戏设定与循环########################
screen = startPygame(width, height)
#heart = Heart() #三个类都在myPygame里，别的用的时候，需要重新定义
for title in titles:
    Title(title)
electedTitle = None
while running:
    #大世界交互规则
    for event in pygame.event.get(): 
    #这只能在一个循环中用一次，之后就不行了
    #更新精灵中也只有第一个精灵能获得
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print("MOUSE") #果然，只能得到一次event
            otherSprites.empty()
            electedTitle = None
            electedSprites.empty()
            for title in titleSprites:
                otherSprites.add(title)
                if title.rect.collidepoint(event.pos):
                    #print(title.name)
                    otherSprites.remove(title)
                    electedSprites.add(title)
                    electedTitle = title
    
    if electedTitle:
        backgroundImg = pygame.transform.scale(electedTitle.imgTitle, (width, height))
        hits = pygame.sprite.spritecollide(electedTitle, otherSprites, False)
        for hit in hits:
            hit.speedx *= -3
            hit.speedy *= -3
        

    #大世界交互规则

    #更新显示画面
    clock.tick(60)
    screen.fill(BLACK)
    if backgroundImg:
        screen.blit(backgroundImg, (0,0)) #把这图片画上去
    #screen.fill(SKYBLUE)
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.update()

pygame.quit()
###4.开始游戏设定与循环########################
