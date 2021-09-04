###1.导入语言包##############################
import pygame
import random
import os


###2.一些常数################################
YELLOW = (255, 255, 0) #一种设置颜色的方式


###3.开始视觉和声音#######################################
pygame.init() #初始化
pygame.mixer.init() #初始化声音
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #设置窗口大小
pygame.display.set_caption('练习pygame') #设置窗口标题


###4.调入视觉和声音资源######################################
player_img = pygame.image.load(os.path.join('img', 'player.png')).convert() #加载图片
player_mini_img = pygame.transform.scale(player_img, (25, 19)) #缩放图片
font_arial = pygame.font.match_font('arial') #两个导入字体的方式
font_font = os.path.join(('font.ttf'))
player_expl_img = pygame.image.load(os.path.join('img', f'player_expl{i}.png')).convert() #for循环中可以直接这样f字符串中{i}来加载变量
player_expl_img.set_colorkey(BLACK) #设置colorKey

shoot_sound = pygame.mixer.Sound(os.path.join('sound', 'shoot.wav')) #加载声音
shoot_sound.play() #可以在精灵类里调用这个来播放

pygame.mixer.music.load(os.path.join('sound', 'background.ogg')) #背景音乐
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


###5.必要用的函数和小精灵们，从了小精灵类####################
def draw_text(screen, text, size, x, y): #把文字写在画面上
    font = pygame.font.Font(font_arial, size) #字体及大小
    fontObj = pygame.font.SysFont('systemFontName', size=10, bold=True, italic=True) #字体及大小
    text_surface = font.render(text, True, WHITE) #以字体设置渲染文字并开启抗锯齿
    text_rect = text_surface.get_rect() #获得这个surface的rect准备设定位置
    text_rect.centerx = x #这样好居中，不管多长
    text_rect.top = y #这样不用管多高
    screen.blit(text_surface, text_rect) #把text_surface按text_rect的框来放置

def draw_health(screen, hp, x, y): #把框框面在画面上
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT) #按参数画Rect
    fill_rect = pygame.Rect(x, y, FILL, BAR_HEIGHT)
    pygame.draw.rect(screen, GREEN, fill_rect) #把Rect画出来
    pygame.draw.rect(screen, WHITE, outline_rect, 2) #外框线

def draw_lives(screen, lives, img, x, y): #把图片画在screen上
    for i in range(lives): #画多少次
        img_rect = img.get_rect() #得到图片的rect
        img_rect.x = x + 30*i #生命多一个就向右移一次，这逻辑，厉害
        img_rect.y = y
        screen.blit(img, img_rect) #图片挂在图片框里

def draw_init(): #把文字写在画面上，好像都是全局变量。用前生成就行
    screen.blit(background_img, (0,0)) #图片挂在(0, 0)位置
    pygame.display.update() #更新显示
    while waiting:
        clock.tick(FPS) #在一秒钟之内最多执行10次，快也没用
        for event in pygame.event.get(): #得到所有事件列表
            if event.type == pygame.QUIT:
                pygame.quit() #关闭后退出
                return True #这个来处理奇怪的不能退出的bug。。。
            elif event.type == pygame.KEYUP/KEYDOWN: #任意键松开就开始
                waiting = False 
                return False

class Player(pygame.sprite.Sprite): #继承自精灵
    def __init__(self, x, y): #必须要有的 #可以在生成时传入位置或其他参数
        pygame.sprite.Sprite.__init__(self) #必须有的
        self.add(allSprites) #必须加入总组来一起更新
        self.add(playerSprites) #加入特属组来供大世界判断碰撞
        self.remove(aliveSprites) #也可移除
        group.empty() #可以移除一个sprite，还可以直接清空group

        self.image = pygame.Surface((50, 40)) #必有的属性，可以这样来个面
        self.image.fill(GREEN) #上面的面的填充色

        self.font = pygame.font.SysFont('Arial', 20) #用字做图
        self.textSurf = self.font.render('text', 1, BLACK)
        self.image = pygame.Surface(50, 40)
        wText = self.textSurf.get_width()
        hText = self.textSurf.get_height()
        self.image.blit(self.textSurf, [50/2 - wText/2, 40/2 -  hText/2]) #中


        self.image = pygame.transform.scale(player_img, (50, 38)) #可以用图片
        self.image.set_colorkey(BLACK) #把黑色透明
        self.rect = self.image.get_rect() #给框起来，之后可以设定框的属性
        self.radius = 20 #画个圆，以进行圆形判断
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius) 
        #画个圆在image上，填充以RED，位置和半径
    
        self.rect.centerx/y, x/y, top/bottom, left/right, width/height
        #通过重新设置这些位置能更新小精灵的位置，直接调用为得到数据
        self.rect.collidepoint(event.pos) 
        #当event为pygame.MOUSEBUTTONDOWN时能判断是不是撞到鼠标了
        
        self.type = random.choice(['shield', 'gun']) #还可以这样随机选择
        
        self.image_ori = random.choice(rock_imgs) #还可以这样随机挑选。。。
        self.image = self.image_ori.copy() #复制图片
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        #自己的动画，自己转移角度生成个新的图片，设置为自己的图
        center = self.rect.center #上个图的框的中心
        self.rect = self.image.get_rect() #这个图的新框
        self.rect.center = center #把此框的中心设置为原来的中心，框中心的旋转

    def update(self): #allSprites会在每个循环调用其内的所有精灵的update函数
        key_pressed = pygame.key.get_pressed() #所有被按住的
        if key_pressed[pygame.K_SPACE]: #如果这个在被按住的里面
            pass #有K_LEFT/RIGHT/UP/DOWN/abcdefg
        
        now = pygame.time.get_ticks() #获得当前时间戳
        if self.gun > 1 and now -self.gun_time > 3000:
            pass #可以以某状态开始时间戳与现在时间戳来判断持续了多少时间
            self.kill() #可以以这个函数来在必要时结束掉不需要的小精灵，省内存
        #死亡后的处理方式1为爆炸新生2为隐藏到屏幕外再调出
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
        #以这种方式判断精灵已离开视野范围，如果能向上，还得加个bottom<0的
            self.rect.x = random.randrange(0, WIDTH - self.rect.width) 
            #重新设置位置，以randrange(a, b)的方式。b>结果>=a，整数，和range一样

class Explosion(pygame.sprite.Sprite): 
    #只是动画效果，一个不断换自己的image的精灵
    def __init__(self, center, size): #动画的中心点和动画种类
        pygame.sprite.Sprite.__init__(self)
        self.add(all_sprites) #尝试生成时自己加入组，后期也可被加入。拣选呢？
        self.size = size
        self.image = explode_anim[self.size][0]
        
        self.frame = 0 #记录当前的帧数，第0帧，要记得总帧数来结束动画
        self.last_update = pygame.time.get_ticks() 
        #记录最近一次换图片时间，不能按update更新，会太快
        self.frame_rate = 50 #1000/50=20，一秒可以运行20次最多
    
    def update(self): #更新sprite的
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate: #时间已经满足了rate了
            self.last_update = now #更新最近一次换图片的时间为现在要换
            self.frame += 1 #换下一帧
            if self.frame > (len(explode_anim[self.size])-1): 
                #如果过了最后一帧了就要销毁动画
                self.kill()
            else: #如果没过最后一帧，就可以继续换图片，直到下次要换时发现过了
                self.image = explode_anim[self.size][self.frame] #换下一帧图
                center = self.rect.center #得到上次图的rect的中心
                self.rect = self.image.get_rect() #得到新图的rect
                self.rect.center = center #新图的rect的中心不变
    

###6.游戏循环，开始前要建组放各类精灵以判断相撞#############
running = True #如果某些时候结束了可以设置这个为False结束游戏
clock = pygame.time.Clock() #控制整个游戏的速度恒定，不要太快主要是
show_init = True #如果是刚开始，要给反应的时间

while running: #游戏开始循环了
    ###游戏开始的等待/游戏重置时的等待，初始化数据以便开始或重复游戏
    if show_init:
        close = draw_init() #初始画面结束，或进入游戏，或关闭游戏
        if close: #这样有个关闭的值，避免一些奇怪的关闭不退出错误
            break
        show_init = False

        #开始的话就要生成各种sprites的组，以更新，以判断
        all_sprites = pygame.sprite.Group() #可以放很多sprite
        rocks = pygame.sprite.Group() #一个单独的群组放石头

        player = Player()
        Rock() #生成各种需要的小精灵开始游戏

        score = 0 #在开始的时候设置分数
    
    
    ###判断输入，退出，或是别的一次按键的事件来放技能，也可以放到精灵里
    #这只能在一个循环中用一次，之后就不行了
    #更新精灵中也只有第一个精灵能获得
    for event in pygame.event.get(): #来判断运行中，有没有退出的事件
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN: #按下了，不是按住，是一次的按下
            if event.key == pygame.K_SPACE
                player.shoot() #按住一直生效的适合移动，不适合技能
    
    
    ###大世界交互规则#################################
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True, pygame.sprite.collide_circle) #两个组碰撞，删除撞到的精灵True or False，圆形碰撞,radius
    #两个组的精灵碰撞，被删除收集为字典[{rock1, [bullets]}，***]
    #第一组碰撞到精灵构成的字典key，其碰撞到的第二组精灵列表们，比较rect判断

    hits = pygame.sprite.spritecollide(player, rocks, True, pygame.sprite.collide_circle) #sprite和组碰撞，默认矩形碰撞要主动改, 把石头删掉，之后要重新生成
    #撞了那个精灵的组里的精灵们被删除收集为列表[rocks]，通过比较rect属性判断的

    for hit in hits: #遍历碰撞到的，有值代表撞了，撞了那个精灵的都在这列表里
        hit.rect/radius #碰到到的第一组的一个rock，或组的一个rock
        pass #然后可以对碰撞进行处理，如加分减分，加血减血，死亡复活等等
        #游戏结束的判断，可以在这里进行，也可以在主角精灵内部进行


    ###刷新显示画面##################################
    clock.tick(FPS) #在一秒钟之内最多执行次数
    screen.fill(BLACK) #把屏幕填充上颜色，或挂上图片也可
    screen.blit(background_img, (0,0)) #把这图片画上去
    all_sprites.update() #所有sprite的组update，因此要在sprite里写这个函数
    all_sprites.draw(screen) #把更新后的所有sprite画到screen上
    draw_text(screen, str(score), 18, WIDTH/2, 10) #再画些别的需要的到screen上
    draw_health(screen, player.health, 5, 15)
    draw_lives(screen, player.lives, player_mini_img, WIDTH - 150, 15)
    pygame.display.update() #把刚刚画上的全部更新显示出来

pygame.quit() #不再进行游戏循环了，再见







