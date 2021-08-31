#!/usr/bin/env python3

#安装库：pip3 install pygame numpy opencv-python 
###1.导入语言包##############################
import pygame
#sprite, 小精灵，游戏的所有元素
import random
import os
import pickle
###1.导入语言包##############################
global FatherSon
FatherSon = {}
global translation
translation = 'E1:美国大兵,E2:动员兵,SHK:磁爆步兵,JUMPJET:飞行兵,\
GHOST:海豹部队,DESO:生化步兵,CLEG:冷冻兵,CCOMAND:超时空突击队,\
PTROOP:心灵突击队,CIVAN:超时空伊万,TANY:谭雅,FLAKT:煤球兵,\
GGI:重装大兵,INIT:尤里新兵,BRUTE:狂兽人,VIRUS:病狙,LUNR:登月火箭兵,\
HARV:奴隶矿车,APOC:天启,HTNK:犀牛,SAPC:运输船,MTNK:灰熊,HORV:武装矿车,\
CARRIER:航母,ZEP:基洛夫,DRON:蜘蛛,HTK:煤球车,SUB:潜艇,AEGIS:神盾,\
LCRF:运输船,DRED:无畏,SHAD:夜鹰,SQD:乌贼,DLPH:海豚,TNKD:坦杀,HOWL:榴弹炮,\
TTNK:磁爆坦克,LTNK:轻坦克,CMON:超时空矿车,SREF:光棱,HYD:海蝎,\
MGTK:幻影,FV:多功能,DTRUCK:自爆卡车,SMIN:奴隶矿厂,YTNK:盖特坦克,\
BFRT:战斗要塞,TELE:磁电坦克,CAOS:神经突袭车,SCHP:武直,MIND:脑车,\
DISK:碟子,UTNK:激光坦克,ROBO:遥控坦克,SCHD:武直,ORCA:土飞机,HORNET:大黄蜂,\
PDPLANE:运输机,BEAG:黑鹰,POWR:电厂,REFN:矿厂,CNST:基地,PILE:兵营,SAND:沙包,\
DEPT:维修厂,TECH:高科,WEAP:重工,\
HAND:兵营,WALL:围墙,RADR:雷达,NAPSIS:精神控制器,\
NALASR:哨戒炮,NASAM:爱国者,YARD:船厂,GACSPH:超时空,WEAT:闪电风暴,\
NAMISL:核弹,ATESLA:光棱塔,GAP:裂缝,GTGCAN:巨炮,NANRCT:核电,GAPILL:碉堡,\
NAFLAK:防空炮,CAOUTP:前哨站,THOSP:医院,AIRP:机场,CLON:复制中心,OREP:精炼厂,\
PARS01:铁塔,AIRC:空指部,AMRADR:美国空指,PSYB:精神控制塔,BRCK:兵营,\
GGUN:盖特机炮,PSYT:心灵控制塔,NAINDP:工业工厂,YAGRND:回收站,GNTC:基因突变,\
PPET:超级心灵控制,NATBNK:坦克碉堡,NABNKR:战斗碉堡,TESLA:磁爆线圈,\
MaxEC:粒子存在时间,EndStateAI:粒子结束帧号,StateAIAdvance:每帧持续越大越慢,\
MaxDC:间隔多少帧一次伤害'.split(',')

##pickle来进行对象序列化（持久化对象)#######
def isEnLine(line):
    for one in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if one in line:
            return True
    return False

def dump2file(filename, obj):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)
        print(f'dumped {filename}')
def loadffile(filename):
    with open(filename, 'rb') as f:
        print(f'loaded {filename}')
        return pickle.load(f)


if os.path.exists('FatherSon'):
    FatherSon = loadffile('FatherSon')
else:
    print('read from textFile')
    names = os.listdir('rules')
    for name in names:
        with open('rules/'+name, 'r') as f:
            allLines = {}
            for oneLine in f.readlines():
                if isEnLine(oneLine):
                    splitedLine = oneLine.strip('\n').strip(' ').split('=')
                    if len(splitedLine) == 2:
                        allLines[splitedLine[0]] = splitedLine[1]
                    else:
                        allLines[splitedLine[0]] = ''
            FatherSon[name] = allLines
    dump2file('FatherSon', FatherSon)

#for father_son in FatherSon:
    #print(father_son)
#exit(0)
def createRulesIni():
    with open('rulesmd.ini', 'w') as f:
        allTexts = []
        for oneItem in FatherSon.values():
            for name, value in oneItem.items():
                if value:
                    allTexts.append(name+'='+value)
                else:
                    allTexts.append(name)
        f.write('\n'.join(allTexts))
        print(f'writed rulesmd.ini')
        dump2file('FatherSon', FatherSon)
            
def allStrengthX3():
    for father, body in FatherSon.items():
        for name, value in body.items():
            if name == 'Strength':
                FatherSon[father][name] = str(int(value)*3)
                print(f'{father}.{name}X3')
#allStrengthX3()
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
roleSprites = pygame.sprite.Group() #在这里定义的Group不能用在导入的文件里的
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
def loadFont(fontName = 'font.ttf'): #中文字体文件改名为font.ttf
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
def text2Img(text, textSize=40, font=defaultFont, bold=False, color=WHITE, colorKey=BLACK):
    textObj = pygame.font.Font(font, textSize)
    textObj.set_bold(bold)
    textSurf = textObj.render(text, True, color)
    text_rect = textSurf.get_rect()
    imgW = text_rect.width + 20 #此时还未设置rect位置，就在左上角呢x/y/top/bottom/center
    imgH = text_rect.height + 10
    img = pygame.Surface((imgW, imgH)) #留点边界好碰撞用
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
class RoleOfImg(pygame.sprite.Sprite): #
    def __init__(self, father, name, x, y, geneNum=1):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
        self.add(roleSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        global FatherSon #{'':[], }
        global translation
        
        self.father = father
        self.oriName = name.replace('等于', '=')
        self.name = self.oriName
        self.firstName = self.oriName
        if '=' in self.oriName:
            self.name = self.oriName.split('=')[1]
            self.firstName = self.oriName.split('=')[0]
        self.geneNum = geneNum
        #print(name, geneNum)
        
        self.image = text2Img(self.oriName, 20)
        for one in translation:
            one = one.split(':')
            if one[0] in self.name:
                self.image = text2Img(self.oriName+one[1], 20)
            elif one[0] in self.firstName:
                self.image = text2Img(one[1]+self.oriName, 20)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.radius = self.rect.width * 0.5 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        
        self.haveSon = False
        self.sons = []
        self.producedSons = []
        
        if self.name in FatherSon:
            self.haveSon = True
            for sonname, sonbody in FatherSon[self.name].items():
                if sonbody:
                    self.sons.append(sonname + '=' + sonbody.strip('	').strip(' '))
                else:
                    self.sons.append(sonname)
        #self.sons.sort()

        if self.haveSon:
            produceRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GOLD, produceRect, 3)
        #else:
            #GeneLine(self)

        
        self.speedx = 3
        self.speedy = 3
    
        self.lifetime = 0
        self.born = pygame.time.get_ticks()
        self.alive = True
    
        self.elected = False

    def update(self):
        if self.elected:
            electedRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GREEN, electedRect, 1) #不加框线为填充
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_a]:
                self.moveSelfAndSons('LEFT')
            elif key_pressed[pygame.K_d]:
                self.moveSelfAndSons('RIGHT')
            if key_pressed[pygame.K_s]:
                self.moveSelfAndSons('DOWN')
            elif key_pressed[pygame.K_w]:
                self.moveSelfAndSons('UP')
        else:
            unelectedRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GRAY, unelectedRect, 1) #不加框线为填充
        if self.haveSon:
            produceRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GOLD, produceRect, 1)

    def produce(self):
        if self.haveSon:
            self.haveSon = False
            lastSon = None
            firstSon = True
            for one in self.sons:
                one = one.replace('=', '等于')
                if firstSon:
                    lastSon = RoleOfImg(self.name, one, self.rect.x, self.rect.y+self.rect.height+10, self.geneNum +1)
                    firstSon = False
                    self.producedSons.append(lastSon)
                else:
                    if lastSon.rect.right + lastSon.rect.width*1> width:
                        lastSon = RoleOfImg(self.name, one, 0, lastSon.rect.bottom+10, self.geneNum +1)
                    else:
                        lastSon = RoleOfImg(self.name, one, lastSon.rect.x + lastSon.rect.width+10, lastSon.rect.y, self.geneNum +1)
                    self.producedSons.append(lastSon)
    
    def moveSelfAndSons(self, direction):
        if direction == 'LEFT':
            self.rect.x -= self.speedx *4
        elif direction == 'RIGHT':
            self.rect.x += self.speedx *4
        elif direction == 'DOWN':
            self.rect.y += self.speedx *6
        elif direction == 'UP':
            self.rect.y -= self.speedx *6
        for son in self.producedSons:
            son.moveSelfAndSons(direction)
        

###4.开始游戏设定与循环########################
width = 700
height = 720
screen = startPygame(width, height)

def init():
    x = 3
    y = 3
    roles = ['InfantryTypes', 'VehicleTypes', 'AircraftTypes', 'BuildingTypes', 
            'MultiplayerDialogSettings', 'SpecialWeapons', 
            'AudioVisual', 'CrateRules', 'CombatDamage', 'Radiation',
            'Countries', 'Sides', 'IQ', 'General', 'Particles']
    for role in roles:
        lastRole = RoleOfImg(role, role, x, y)
        x = lastRole.rect.right + 10
        if lastRole.rect.right + lastRole.rect.width *1 > width:
            x = 3
            y = lastRole.rect.bottom + 10
init()

noOneElected = True
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
            createRulesIni()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN:
            noOneElected = True
            for role in roleSprites:
                role.elected = False
                if role.rect.collidepoint(event.pos):
                    if event.button == 3:
                        edited = input(f'修改{role.father}的{role.oriName} or i/n/d/di:')
                        if edited == 'i':
                            edited = input('添加同类子项:')
                            firstName, lastName = edited.split('=')
                            FatherSon[role.father][firstName] = lastName
                            print(FatherSon[role.father])
                            dump2file('FatherSon', FatherSon)
                        elif edited == 'n':
                            edited = input(f'复制新的父级{role.father}(先在总类加子项):')
                            newFather = {f'[{edited}]':None}
                            for name, value in FatherSon[role.father].items():
                                if value:
                                    newFather[name] = value
                            input(str(newFather))
                            FatherSon[edited] = newFather
                            dump2file('FatherSon', FatherSon)
                        elif edited == 'd':
                            edited = input(f'确认删除{role.father}这一父级？')
                            FatherSon.pop(role.father)
                            dump2file('FatherSon', FatherSon)
                        elif edited == 'di':
                            edited = input(f'确认删除{role.name}这一子级？')
                            FatherSon[role.father].pop(role.firstName)
                            print(FatherSon[role.father])
                            dump2file('FatherSon', FatherSon)
                        else:
                            if FatherSon[role.father][role.firstName]:
                                if edited:
                                    FatherSon[role.father][role.firstName] = edited
                                else:
                                    print("ChangedNothing!")
                            dump2file('FatherSon', FatherSon)
                    noOneElected = False
                    if event.button == 1: #1/2/3
                        role.elected = True
                        role.rect.x = 3
                        role.rect.y = 3
                        role.produce()
                elif event.button == 1:
                    role.kill()
            if not allSprites:
                #print('sprite_group is empty')
                init()
    #全体的wsad
    #if noOneElected:
    if True:
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_w]:
            for role in allSprites:
                role.rect.y -= role.speedy*4
        if keyPressed[pygame.K_s]: 
            for role in allSprites:
                role.rect.y += role.speedy*4
        if keyPressed[pygame.K_a]: 
            for role in allSprites:
                role.rect.x -= role.speedx*3
        if keyPressed[pygame.K_d]: 
            for role in allSprites:
                role.rect.x += role.speedx*3

    if paused:
        continue

    #hits = pygame.sprite.spritecollide(heart, moneySprites, True, pygame.sprite.collide_circle) 
    #hits = pygame.sprite.groupcollide(heartSprites, moneySprites, False, True, pygame.sprite.collide_circle) 
    for oneSprite in roleSprites:
        hits = pygame.sprite.spritecollide(oneSprite, roleSprites, False) 
        if len(hits) > 1:
            for hit in hits:
                if oneSprite.rect.x <= hit.rect.x:
                    oneSprite.rect.x -= 10
                    hit.rect.x += 10
                else:
                    oneSprite.rect.x += 10
                    hit.rect.x -= 10
                    
                
    
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
