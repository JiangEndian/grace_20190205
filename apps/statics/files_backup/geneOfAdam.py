#!/usr/bin/env python3

#安装库：pip3 install pygame numpy opencv-python 
###1.导入语言包##############################
import pygame
#sprite, 小精灵，游戏的所有元素
import random
import os
###1.导入语言包##############################

#亚当的所有基因
gene = {
        '亚当本以罗欣':['该隐,以诺,以拿,米户雅利,玛土撒利,拉麦', '亚伯', '塞特,以挪士,该南,玛勒列,雅列,以诺,玛土撒拉,拉麦,挪亚'], 
            
        #拉麦本玛土撒利分支
        '拉麦本玛土撒利':['雅八畜牧', '犹八乐器', '土八该隐铜铁利器'],

        #挪亚本拉麦主线
        '挪亚本拉麦':['闪本挪亚', '含本挪亚', '雅弗本挪亚'],

        #雅弗本挪亚分支
        '雅弗本挪亚':['歌篾本雅弗', '玛各', '玛代', '雅完本雅弗', '土巴', '米设', '提拉'], 
        '歌篾本雅弗':['亚实基拿', '利法', '陀迦玛'],
        '雅完本雅弗':['以利沙', '他施', '基提', '多单'],
        
        #含本挪亚分支
        '含本挪亚':['古实本含', '麦西本含', '弗', '迦南本含'],
        '古实本含':['西巴', '哈腓拉', '撒弗他', '拉玛本古实', '撒弗提迦', '宁录'], 
        '麦西本含':['路低人', '亚拿米人', '利哈比人', '拿弗土希人', '帕斯鲁细人', '迦斯路希人', '迦斐托人,非利士人'], 
        '迦南本含':['西顿', '赫', '耶布斯人', '亚摩利人', '革迦撒人', '希未人', '亚基人', '西尼人', '亚瓦底人', '洗玛利人', '哈马人'], 
        '拉玛本古实':['示巴', '底但'], 

        #闪本挪亚主线
        '闪本挪亚':['以拦', '亚述', '亚法撒,沙拉,希伯', '路德', '亚兰本闪',], 
        '亚兰本闪':['乌斯', '户勒', '基帖', '玛施'], 
        '希伯本沙拉':['法勒本希伯', '约坍本希伯'], 
        '约坍本希伯':['亚摩答', '沙列', '哈萨玛非', '耶拉', '哈多兰', '乌萨', '德拉', '俄巴路', '亚比玛利', '示巴', '阿斐', '哈腓拉', '约巴'], 
        '法勒本希伯':['拉吴,西鹿,拿鹤,他拉'], 

        #他拉本拿鹤分支
        '他拉本拿鹤':['亚伯拉罕', '拿鹤本他拉', '哈兰,罗得本哈兰'], 
        '拿鹤本他拉':['乌斯', '布斯', '基母利,亚兰', '基薛', '哈琐', '必达', '益拉', '彼土利', '提八', '迦含', '他辖', '玛迦'],
        '罗得本哈兰':['摩押,摩押人', '便亚米,亚扪人'],

        #亚伯拉罕主线
        '亚伯拉罕':['以实玛利本亚伯拉罕', '以撒本亚伯拉罕', '心兰', '约珊本亚伯拉罕', '米但', '米甸本亚伯拉罕', '伊施巴', '书亚'], 
        '约珊本亚伯拉罕':['示巴', '底但本约珊'], 
        '底但本约珊':['亚书利族', '利都是族', '利乌米族'], 
        '米甸本亚伯拉罕':['以法', '以弗', '哈诺', '亚比大', '以勒大'], 
        '以实玛利本亚伯拉罕':['尼拜约', '基达', '亚德别', '米比衫', '米施玛', '度玛', '玛撒', '哈大', '提玛', '伊突', '拿非施', '基底玛'], 
    
        #以撒本亚伯拉罕主线
        '以撒本亚伯拉罕':['以扫本以撒', '雅各本以撒'], 
        '以扫本以撒':['以利法本以扫', '流珥本以扫', '耶乌施', '雅兰', '可拉'], 
        '以利法本以扫':['提幔', '阿抹', '洗玻', '迦坦', '基纳斯', '亚玛力'], 
        '流珥本以扫':['拿哈', '谢拉', '沙玛', '米撒', ], 

        '雅各本以撒':['流便本雅各', '西缅本雅各', '利未本雅各', '犹大本雅各', '但', '拿弗他利', '迦得', '亚设', '以萨迦', '西布伦', '约瑟', '便雅悯'], 
        '流便本雅各':['哈诺', '法路', '希斯仑', '迦米'], 
        '西缅本雅各':['耶母利', '雅悯', '阿辖', '雅斤', '琐辖', '扫罗'], 
        '利未本雅各':['革顺本利未', '哥辖本利未', '米拉利本利未'], 
        '革顺本利未':['立尼', '示每'], 
        '哥辖本利未':['暗兰本哥辖', '以斯哈本哥辖', '希伯伦', '乌薛'], 
        '米拉利本利未':['抹利', '母示'], 
        '以斯哈本哥辖':['可拉本以斯哈', '尼斐', '细基利'], 
        '可拉本以斯哈':['亚惜', '以利加拿', '亚比亚撒'], 

        '暗兰本哥辖':['亚伦本暗兰', '摩西'], 
        '亚伦本暗兰':['拿答', '亚比户', '以利亚撒,非尼哈', '以他玛'], 

        '犹大本雅各':['珥', '俄南', '示拉', '法勒斯本犹大', '谢拉'], 
        '法勒斯本犹大':['希斯仑本法勒斯', '哈母勒'], 
        '希斯仑本法勒斯':['耶拉篾', '兰,亚米拿达,拿顺,撒门,波阿斯,俄备得,耶西', '基路拜'], 
        '耶西本俄备得':['以利押', '亚比拿达', '示米亚', '拿坦业', '拉代', '阿鲜', '大卫本耶西', '洗鲁雅,亚比筛、约押、亚撒黑', '亚比该和以实玛利人益帖,亚玛撒'], 
        '大卫本耶西':['暗嫩', '但以利', '押沙龙', '亚多尼雅', '示法提雅', '以特念', '以格拉', '示米亚', '朔罢', 
            '拿单,玛达他,买南,米利亚,以利亚敬,约南,约瑟,犹大,西缅,利未1,玛塔1,约令,以利以谢,约细,珥,以摩当,哥桑,亚底,麦基,尼利,撒拉铁1,所罗巴伯1,利撒,约亚拿,犹大,约瑟,西美,玛他提亚,玛押,拿该,以斯利,拿鸿,亚摩斯,玛他提亚,约瑟,雅拿,麦基,利未2,玛塔2,表哥希里,约瑟,耶稣本以罗欣', 
            '所罗门,罗波安,亚比雅,亚撒,约沙法,约兰,乌西亚,约坦,亚哈斯,希西家,玛拿西,亚们,约西亚,耶哥尼雅,撒拉铁,所罗巴伯,亚比玉,以利亚敬,亚所,撒督,亚金,以律,以利亚撒,马但,表弟雅各,约瑟,耶稣本以罗欣', 
            '益辖、以利沙玛、以利法列、挪迦、尼斐、雅非亚、以利沙玛、以利雅大、以利法列', '妃嫔的儿子不在其内'], 
            '耶稣本以罗欣':['各国', '各族', '各民', '各方'], 
    }
global FatherSon
FatherSon = []
for oneFather in gene: #{'':[], }
    for son in gene[oneFather]: #['', ] 
        geneLine = son.split(',') #['', '']
        if len(geneLine)>1:
            thisFather = oneFather
            lastFather = None
            for oneGene in geneLine:
                if lastFather:
                    if oneGene == '耶稣本以罗欣':
                        father_son = (thisFather + '本'+lastFather, '耶稣本以罗欣')
                        #print(father_son)
                        FatherSon.append(father_son)
                    else:
                        father_son = (thisFather+'本'+lastFather, oneGene + '本' + thisFather)
                        #print(father_son)
                        FatherSon.append(father_son)
                        #print(thisFather+'本'+lastFather, oneGene + '本' + thisFather)
                        lastFather = thisFather
                        thisFather = oneGene 
                else:
                    father_son = (thisFather, oneGene+'本'+thisFather)
                    #print(father_son)
                    FatherSon.append(father_son)
                    #print(thisFather, oneGene)
                    lastFather = thisFather
                    thisFather = oneGene
        else:
            father_son = (oneFather, son)
            #print(father_son)
            FatherSon.append(father_son)
            #print(oneFather, son)

#for fatherSon in FatherSon:
    #print(fatherSon)
#exit(0)

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
    def __init__(self, name, x, y, geneNum=1):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里
        self.add(roleSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        global FatherSon

        self.name = name
        self.geneNum = geneNum
        print(name, geneNum)
        self.image = text2Img(self.name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.radius = self.rect.width * 0.5 / 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        
        self.haveSon = False
        self.sons = []
        self.producedSons = []

        for fatherSon in FatherSon:
            if self.name == fatherSon[0]:
                self.haveSon = True
                self.sons.append(fatherSon[1])

        if self.haveSon:
            produceRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GOLD, produceRect, 3)
        else:
            GeneLine(self)

        
        self.speedx = 3
        self.speedy = 3
    
        self.lifetime = 0
        self.born = pygame.time.get_ticks()
        self.alive = True
    
        self.elected = False

    def update(self):
        if self.elected:
            electedRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GREEN, electedRect, 3) #不加框线为填充
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
            pygame.draw.rect(screen, GRAY, unelectedRect, 3) #不加框线为填充
        if self.haveSon:
            produceRect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, GOLD, produceRect, 3)

    def produce(self):
        if self.haveSon:
            self.haveSon = False
            lastSon = None
            firstSon = True
            for one in self.sons:
                if firstSon:
                    lastSon = RoleOfImg(one, self.rect.x, self.rect.y+self.rect.height+30, self.geneNum +1)
                    firstSon = False
                    LinkFatherSon(self, lastSon)
                    self.producedSons.append(lastSon)
                else:
                    lastSon = RoleOfImg(one, lastSon.rect.x + lastSon.rect.width+30, lastSon.rect.y, self.geneNum +1)
                    LinkFatherSon(self, lastSon)
                    self.producedSons.append(lastSon)
    
    def moveSelfAndSons(self, direction):
        if direction == 'LEFT':
            self.rect.x -= self.speedx
        elif direction == 'RIGHT':
            self.rect.x += self.speedx
        elif direction == 'DOWN':
            self.rect.y += self.speedx
        elif direction == 'UP':
            self.rect.y -= self.speedx
        for son in self.producedSons:
            son.moveSelfAndSons(direction)
        
        
class LinkFatherSon(pygame.sprite.Sprite): #
    def __init__(self, father, son):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect()

        self.father = father
        self.son = son

        self.speedx = 0
        self.speedy = 0
        
    def update(self):
        pygame.draw.line(screen, CLAY, self.father.rect.bottomleft, self.son.rect.topleft,3)

    def produce(self):
        pass
    

class GeneLine(pygame.sprite.Sprite): #
    def __init__(self, followedSprite):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites) #这些没有传进来就直接引用的变量，需要在一个文件里

        self.image = pygame.Surface((3, 70))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        
        self.followedSprite = followedSprite
        self.rect.centerx = self.followedSprite.rect.centerx
        self.rect.y = self.followedSprite.rect.bottom
        
        self.speedx = 3
        self.speedy = 3
    
    def update(self):
        self.rect.centerx = self.followedSprite.rect.centerx
        self.rect.y = self.followedSprite.rect.bottom

    def produce(self):
        pass
    

###3.必要用的函数和类########################


###4.开始游戏设定与循环########################
width = 1280
height = 720
screen = startPygame(width, height)

RoleOfImg('亚当本以罗欣', 3, 3)


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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN:
            noOneElected = True
            for role in roleSprites:
                role.elected = False
                if role.rect.collidepoint(event.pos):
                    role.elected = True
                    noOneElected = False
                    if event.button == 1: #1/2/3
                        role.produce()
    #全体的wsad
    if noOneElected:
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
