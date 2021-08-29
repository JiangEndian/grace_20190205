#!/usr/bin/env python3

#安装库：pip3 install pygame numpy opencv-python 
###1.导入语言包##############################
import pygame
#sprite, 小精灵，游戏的所有元素
import random
import os
###1.导入语言包##############################

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
SPIRITKEY = (56, 255, 12)

clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()
electedSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
spiritSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
fleshSprites = pygame.sprite.Group()
adamSprites = pygame.sprite.Group()
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
def loadFont(fontName = 'font.ttf'):
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
class Adam(pygame.sprite.Sprite): #自动的
    def __init__(self, title="人", x=10, y=10):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
        self.add(adamSprites)
        if pygame.time.get_ticks() - AA0 > BecameFlesh:
            self.add(fleshSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
        else:
            self.add(spiritSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.imgTitle = text2Img('人', 60, font='font.ttf', bold=True, color=SPIRITKEY)
        self.imgElected = text2Img('以色列', 60, font='font.ttf', bold=True, color=GOLD)
    
        #self.images = loadImgs('hearts', 101, 'heart.png')
        self.image = self.imgTitle
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.8 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
    
        self.rect.x = x
        self.rect.y = y

        self.bornTime = pygame.time.get_ticks()
        self.lifeLimit = random.randrange(1, adamsLife)
            
        self.speedMax = 2
        self.speedx = random.randrange(-self.speedMax, self.speedMax)
        self.speedy = random.randrange(-self.speedMax, self.speedMax)
        #保持方向时除以自身的绝对值，但不能为0
        while self.speedx == 0:
            self.speedx = random.randrange(-self.speedMax, self.speedMax)
        while self.speedy == 0:
            self.speedy = random.randrange(-self.speedMax, self.speedMax)

    def update(self):
        if pygame.time.get_ticks() - self.bornTime > self.lifeLimit*1000:
            if not len(allSprites) > allAdams:
                Adam(x=self.rect.x, y=self.rect.y)
                Adam(x=self.rect.x+self.rect.width*2, y=self.rect.y+self.rect.height*2)
                self.kill()
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
            self.speedx = -self.speedx/abs(self.speedx) * random.randrange(1, self.speedMax)
        if self.rect.left < 0:
            #copy一个自己在另一边，继承速度
            self.rect.left = 0
            self.speedx = -self.speedx/abs(self.speedx) * random.randrange(1, self.speedMax)
        if self.rect.bottom > height:
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.bottom = height
            self.speedy = -self.speedy/abs(self.speedy) * random.randrange(1, self.speedMax)
        if self.rect.top < 0:
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.top = 0
            self.speedy = -self.speedy/abs(self.speedy) * random.randrange(1, self.speedMax)
        
    def defeated(self):
        Bowdown(self)

class Bowdown(pygame.sprite.Sprite): #自动的
    def __init__(self, followedSprite):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
        
        self.followedSprite = followedSprite
        
        self.fontS = 60
        self.textImg = text2Img('以色列', textSize=self.fontS, bold=True, color=GOLD)
        #self.images = textImgs(self.textImg, 20)
        self.imageOri = self.textImg
        self.image = self.imageOri
        self.rect = self.image.get_rect()
        #self.rect.center = center
        self.rect.center = self.followedSprite.rect.center
        
        self.images = scaleImg4Animation(self.imageOri, self.rect.width, self.rect.height, 10)

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

class Spirit(pygame.sprite.Sprite): #手动的
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.oriImage = loadImg('.', '2.jpg')
        self.rect = self.oriImage.get_rect()
        scale = 0.3
        self.image = pygame.transform.scale(self.oriImage, (int(self.rect.width*scale), int(self.rect.height*scale)))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.8 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
    
        self.rect.centerx = width/2 #这里的不能用上面的
        self.rect.centery = height/2
            
        self.speedx = 0
        self.speedy = 0
        #保持方向时除以自身的绝对值，但不能为0
    def update(self):
        self.speedx = 0
        self.speedy = 0
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]:
            self.speedx = -4
        elif key_pressed[pygame.K_d]:
            self.speedx = 4
        if key_pressed[pygame.K_w]:
            self.speedy = -4
        elif key_pressed[pygame.K_s]:
            self.speedy = 4
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #判断返回
        if self.rect.right > width: #这种方法保持方向，重新获得速度（非0）
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.right = width
        if self.rect.left < 0:
            #copy一个自己在另一边，继承速度
            self.rect.left = 0
        if self.rect.bottom > height:
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.bottom = height
        if self.rect.top < 0:
            #有时会卡在里面，就是判断返回了，但速度太小，还在里面，又返回
            self.rect.top = 0
###3.必要用的函数和类########################


###4.开始游戏设定与循环########################
width = 1280
height = 720
screen = startPygame(width, height)
AA0 = pygame.time.get_ticks()
BecameFlesh = 9*1000
adamsLife = 5
allAdams = 20
isFlesh = False
spirit = Spirit()
Adam()
while running:
    #大世界交互规则
    for event in pygame.event.get(): 
    #这只能在一个循环中用一次，之后就不行了
    #更新精灵中也只有第一个精灵能获得
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print("MOUSE") #果然，只能得到一次event
            for adam in allSprites:
                if adam.rect.collidepoint(event.pos):
                    #print(title.name)
                    electedSprites.add(adam)
                    adamSprites.remove(adam)
    
    hits = pygame.sprite.spritecollide(spirit, spiritSprites, False, pygame.sprite.collide_circle)
    for hit in hits:
        hit.speedx = spirit.speedx
        hit.speedy = spirit.speedy
        hit.rect.x += hit.speedx*2
        hit.rect.y += hit.speedy*2
    
    hits = pygame.sprite.spritecollide(spirit, electedSprites, False, pygame.sprite.collide_circle)
    for hit in hits:
        hit.rect.x += spirit.speedx
        hit.rect.y += spirit.speedy
        if hit.rect.left<3 and (hit.rect.top<3 or hit.rect.bottom>height-3) or hit.rect.right>width-3 and (hit.rect.top<3 or hit.rect.bottom>height-3):
            Adam()
            hit.kill()
            hit.defeated()
    
    hits = pygame.sprite.groupcollide(adamSprites, adamSprites, False, False, pygame.sprite.collide_circle) #hits = {one:[], one:[]}
    for firstMember in hits:
        for secondMember in hits[firstMember]:
            if firstMember == secondMember:
                pass
            else:
                secondMember.speedx = -secondMember.speedx
                if firstMember.rect.x < secondMember.rect.x:
                    firstMember.rect.right = secondMember.rect.x - 1
                elif firstMember.rect.x > secondMember.rect.x:
                    firstMember.rect.x = secondMember.rect.right + 1
                    
                    
    #467     #hits = pygame.sprite.groupcollide(heartSprites, moneySprites, False, True, pygame.sprite.collide_circle) 
    #hits = pygame.sprite.spritecollide(electedTitle, otherSprites, False)
    #for hit in hits:
        #hit.speedx *= -3
        #hit.speedy *= -3
        

    #大世界交互规则

    #更新显示画面
    clock.tick(60)
    screen.fill(BLACK)
    if pygame.time.get_ticks() - AA0 > BecameFlesh:
        draw_text(screen, '人既属乎血气', 30, width/2, 70)
    else:
        draw_text(screen, '成了有灵的活人', 30, width/2, 10)
        
    #screen.fill(SKYBLUE)
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.update()

pygame.quit()
###4.开始游戏设定与循环########################
