#!/usr/bin/env python3

###1.导入语言包##############################
import pygame
#sprite, 小精灵，游戏的所有元素
import random
import os
###1.导入语言包##############################


###2.一些常数################################
FPS = 30
WIDTH = 500
HEIGHT = 600
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
###2.一些常数################################


###3.开始视觉和声音#######################################
pygame.init() #初始化
pygame.mixer.init() #初始化声音
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #窗口大小
pygame.display.set_caption('练习pygame')
###3.开始视觉和声音#######################################


###4.调入视觉和声音资源######################################
background_img = pygame.image.load(os.path.join('img', 'background.png')).convert()
player_img = pygame.image.load(os.path.join('img', 'player.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
pygame.display.set_icon(player_mini_img)
rock_img = pygame.image.load(os.path.join('img', 'rock.png')).convert()
bullet_img = pygame.image.load(os.path.join('img', 'bullet.png')).convert()

rock_imgs = []
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join('img', f'rock{i}.png')).convert()) #直接在字符串里加变量

font_name = pygame.font.match_font('arial') #导入字体
font_name = os.path.join(('font.ttf'))

explode_anim = {}
explode_anim['large'] = []
explode_anim['small'] = []
explode_anim['player'] = []
for i in range(9): #石头和玩家爆炸
    explode_img = pygame.image.load(os.path.join('img', f'expl{i}.png')).convert()
    explode_img.set_colorkey(BLACK)
    explode_anim['large'].append(pygame.transform.scale(explode_img, (75, 75)))
    explode_anim['small'].append(pygame.transform.scale(explode_img, (30, 30)))
    
    player_expl_img = pygame.image.load(os.path.join('img', f'player_expl{i}.png')).convert()
    player_expl_img.set_colorkey(BLACK)
    explode_anim['player'].append(player_expl_img)

power_imgs = {}
power_imgs['shield'] = pygame.image.load(os.path.join('img', 'shield.png')).convert()
power_imgs['gun'] = pygame.image.load(os.path.join('img', 'gun.png')).convert()

shoot_sound = pygame.mixer.Sound(os.path.join('sound', 'shoot.wav'))
die_sound = pygame.mixer.Sound(os.path.join('sound', 'rumble.ogg'))
explode_sounds = [
    pygame.mixer.Sound(os.path.join('sound', 'expl0.wav')),
    pygame.mixer.Sound(os.path.join('sound', 'expl1.wav'))
]

pygame.mixer.music.load(os.path.join('sound', 'background.ogg')) #背景音乐
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
        
shield_sound = pygame.mixer.Sound(os.path.join('sound', 'pow0.wav'))
gun_sound = pygame.mixer.Sound(os.path.join('sound', 'pow1.wav'))
###4.调入视觉和声音资源######################################


###5.必要用的函数和小精灵们，从了小精灵类####################
def draw_text(surf, text, size, x, y): #把文字写在画面上
    font = pygame.font.Font(font_name, size) #字体及大小
    text_surface = font.render(text, True, WHITE) #以字体设置渲染文字并开启抗锯齿
    text_rect = text_surface.get_rect() #获得这个的rect准备设定位置
    text_rect.centerx = x #这样好居中，不管多长
    text_rect.top = y #这样不用管多高
    surf.blit(text_surface, text_rect) #挂在传进来的平面上

def draw_health(surf, hp, x, y): #把文字写在画面上
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100) * BAR_LENGTH

    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT) #画矩形
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect) #画出来
    pygame.draw.rect(surf, WHITE, outline_rect, 2) #外框要有边线宽度

def draw_lives(surf, lives, img, x, y): #把文字写在画面上
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30*i #生命多一个就向右移一次，这逻辑，厉害
        img_rect.y = y
        surf.blit(img, img_rect)

def draw_init(): #把文字写在画面上，好像都是全局变量。用前生成就行
    screen.blit(background_img, (0,0)) #把这图片画上去
    draw_text(screen, 'practice', 64, WIDTH/2, HEIGHT/4)
    draw_text(screen, '左右键移动，空格攻击', 22, WIDTH/2, HEIGHT/2)
    draw_text(screen, '任意键开始游戏', 18, WIDTH/2, HEIGHT*3/4)
    pygame.display.update()
        
    waiting = True
    while waiting:
        clock.tick(FPS) #在一秒钟之内最多执行10次，快也没用
        #取得输入
        for event in pygame.event.get(): #得到所有事件列表
            if event.type == pygame.QUIT:
                pygame.quit() #关闭后后面也继续，所以，返回个值来判断
                return True
            #elif event.type == pygame.KEYDOWN: #这个不返回也没错
            elif event.type == pygame.KEYUP: #松开开始比较好
                waiting = False
                return False

def new_rock():
    r = Rock() #有碰撞的话，补充石头
    all_sprites.add(r)
    rocks.add(r)

class Player(pygame.sprite.Sprite):
    def __init__(self): #必须要有的
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 40))
        #self.image.fill(GREEN) #要显示的图片
        self.image = pygame.transform.scale(player_img, (50, 38)) #调整大小
        self.image.set_colorkey(BLACK) #把黑色透明
        self.rect = self.image.get_rect() #给框起来，之后可以设定框的属性

        self.radius = 20 #画个圆，以进行圆形判断
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.rect.centerx = WIDTH/2 #也可以设定中心点
        self.rect.bottom = HEIGHT-10
        self.speedx = 8
        self.health = 100
        self.lives = 1
        self.hidden = False
        self.hide_time = 0
        self.gun = 1
        self.gun_time = 0

    def update(self): #更新sprite的
        if self.lives <= 0 and not death_expl.alive(): #并且die动画不存在，放完了
            show_init = True
        
        key_pressed = pygame.key.get_pressed() #这是按住就行的 
        #在这里可以非常顺，但在总循环里不行。这也是总循环一次update一次的啊
        if key_pressed[pygame.K_SPACE]: #玩家输入的在这里控制小精灵，否则自己玩
            player.shoot()
        if key_pressed[pygame.K_LEFT]: #玩家输入的在这里控制小精灵，否则自己玩
            player.rect.x -= player.speedx
        if key_pressed[pygame.K_RIGHT]: #玩家输入的在这里控制小精灵，否则自己玩
            player.rect.x += player.speedx

        now = pygame.time.get_ticks()
        if self.gun > 1 and now -self.gun_time > 3000:
            self.gun = 1

        if self.hidden and now - self.hide_time > 1000: #死亡后隐藏的显示
            self.hidden = False
            self.rect.centerx = WIDTH/2 #也可以设定中心点
            self.rect.bottom = HEIGHT-10
    
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
    def shoot(self):
        if not self.hidden:
            if self.gun == 1:
                shoot_sound.play()
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
            if self.gun >= 2:
                shoot_sound.play()
                bullet1 = Bullet(self.rect.left, self.rect.centery) #子弹位置得调整
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT + 500)
    def gunup(self):
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()
        
class Power(pygame.sprite.Sprite):
    def __init__(self, center): #必须要有的
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 40))
        #self.image.fill(GREEN) #要显示的图片
        self.type = random.choice(['shield', 'gun'])
        self.image = power_imgs[self.type]

        self.image.set_colorkey(BLACK) #把黑色透明
        self.rect = self.image.get_rect() #给框起来，之后可以设定框的属性
        self.rect.center = center #也可以设定中心点
        self.speedy = 3
    
    def update(self): #更新sprite的
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

class Rock(pygame.sprite.Sprite):
    def __init__(self): #必须要有的
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((30, 40))
        #self.image.fill(RED) #要显示的图片
        #self.image_ori = rock_img
        self.image_ori = random.choice(rock_imgs) #还可以这样随机挑选。。。
        self.image_ori.set_colorkey(BLACK)
        #self.image = rock_img
        self.image = self.image_ori.copy() #复制过来这个图片
        #self.image.set_colorkey(BLACK) #设定colorkey透明
        self.rect = self.image.get_rect() #给框起来，之后可以设定框的属性
        
        self.radius = int(self.rect.width * 0.85 / 2) #画个圆，以进行圆形判断
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        
        self.rect.x = random.randrange(0, WIDTH - self.rect.width) #也可以设定中心点
        self.rect.y = random.randrange(-180, -100) #也可以设定中心点
        #self.rect.y = random.randrange(1, 10) #也可以设定中心点
        self.speedy = random.randrange(2, 10)
        #self.speedy = random.randrange(1, 2)
        self.speedx = random.randrange(-3, 3)

        self.total_degree = 0
        self.rot_degree = random.randrange(-3, 3)
        
        #self.image = pygame.transform.rotate(self.image_ori, self.rot_degree) #换图片，换为rotate之后的，但会失真
        #self.rect = self.image.get_rect() #给框起来，之后可以设定框的属性
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        #转动之后是新图片，需要新get_rect
    
    def rotate(self): #用来在更新的时候旋转，功能提取出来了，也可以update里写
        self.total_degree += self.rot_degree
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree) #换图片，换为rotate之后的，但会失真
        

        center = self.rect.center #以中心点来转动，记录原来rect的中心点
        self.rect = self.image.get_rect() #这需要重新获取下rect，image是转动过的新image，新rect,新center
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius) #直接画在图片上，画完再转中心
        #转动之后是新图片，需要新get_rect
        self.rect.center = center 
        #重新设定了中心之后，图片不在图片中心了。所以改变中心位置之前画图
        #但问题是，又有点位置不同了。所以，重新get_rect
        #转完中心再获取rect，相当于再生成。。。应该是以图片为准，因为是sprite必须因素，rect是从图片获取的，然后又重新定位的
        
        #self.radius = self.rect.width * 0.85 / 2 #画个圆，以进行圆形判断
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)


    def update(self): #更新sprite的
        self.rotate() #之后换新Image了，原地转动之后，再平移的

        self.rect.y += self.speedy
        self.rect.x += self.speedx
    
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width) #也可以设定中心点
            self.rect.y = random.randrange(-100, -40) #也可以设定中心点
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y): #子弹需要根据飞船xy确定
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((10, 20))
        #self.image.fill(YELLOW) #要显示的图片
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #给框起来，之后可以设定框的属性

        self.rect.centerx = x
        self.rect.bottom = y 
        self.speedy = -10

    def update(self): #更新sprite的
        self.rect.y += self.speedy
    
        if self.rect.bottom < 0:
            self.kill() #移除sprite组中的子弹

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size): #爆炸图片的中心点和尺寸
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((10, 20))
        #self.image.fill(YELLOW) #要显示的图片
        self.size = size
        self.image = explode_anim[self.size][0]
        self.rect = self.image.get_rect() #给框起来，之后可以设定框的属性
        self.rect.center = center
        self.frame = 0 #图片的每一帧

        self.last_update = pygame.time.get_ticks() #记录最后一次更新时间，不能用update更新，会太快
        self.frame_rate = 50
        self.add(all_sprites) #尝试生成时自己加入组，后期也可被加入。拣选呢？
        #确实可以通过。所以，两都都可以。但无论是自己加入，还是被动，都在作者

    def update(self): #更新sprite的
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame > (len(explode_anim[self.size])-1):
                self.kill()
                #print(self.size)
                #print(self.alive())
            else:
                self.image = explode_anim[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
###5.必要用的函数和小精灵们，从了小精灵类####################


###sprites game游戏流程：0小精灵主/被动1大世界交互规则2按fps更新显示画面，经过一定时间，继续123123
running = True
#控制游戏速度，不能电脑多快就跑多快
clock = pygame.time.Clock()
#初始画面
show_init = True
while running:
    if show_init:
        close = draw_init()
        if close: #这样有个关闭的值，省得以关闭窗口来退出后继续运行后面的
            break
        show_init = False
        ###各种sprites的组，好能判断他们相撞与否############
        all_sprites = pygame.sprite.Group() #可以放很多sprite
        rocks = pygame.sprite.Group() #一个单独的群组放石头
        bullets = pygame.sprite.Group() #单独放子弹，好有方法判断精灵重合
        powers = pygame.sprite.Group() #单独放子弹，好有方法判断精灵重合
        ###各种sprites的组，好能判断他们相撞与否############
        
        ###生成sprite，并加入组##############################
        player = Player()
        all_sprites.add(player) #然后在更新画面中把所有sprite画到screen上即可
            
        for i in range(8):
            new_rock()
        score = 0
        ###生成sprite，并加入组##############################



    for event in pygame.event.get(): #得到所有事件列表
        if event.type == pygame.QUIT: #关掉窗口
            running = False
        #elif event.type == pygame.KEYDOWN: #这是按下一次的
        #if event.key == pygame.K_LEFT: #右方向键按下了吗，单次的，得反复按
        #key_pressed = pygame.key.get_pressed() #这是按住就行的，在这里只有子弹行，同样的代码。。。算了，知道就行了
        #if key_pressed[pygame.K_SPACE]: #玩家输入的在这里控制小精灵，否则自己玩
            #player.shoot()
        #if key_pressed[pygame.K_LEFT]: #玩家输入的在这里控制小精灵，否则自己玩
            #player.rect.x -= player.speedx
        #if key_pressed[pygame.K_RIGHT]: #玩家输入的在这里控制小精灵，否则自己玩
            #player.rect.x += player.speedx



    ###大世界交互规则#################################
    ###石头子弹相撞###
    #hits = pygame.sprite.groupcollide(rocks, bullets, True, True) #两个组中，碰撞的sprite删除True or False
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True, pygame.sprite.collide_circle) #两个组中，碰撞的sprite删除True or False，圆形碰撞,radius
    for hit in hits: #有碰撞生成新石头，并计分
        if random.random() > 0.9: #石头爆炸，概率掉宝
            power = Power(hit.rect.center)
            all_sprites.add(power)
            powers.add(power)
        new_rock()
        random.choice(explode_sounds).play() #爆炸声音
        score += hit.radius #hits是个字典列表，{rock, bullet}，直接rock的半径

        expl = Explosion(hit.rect.center, 'large')
        all_sprites.add(expl)
    ###石头子弹相撞###
    
    ###石头飞船相撞###
    hits = pygame.sprite.spritecollide(player, rocks, True) #sprite碰撞，默认矩形碰撞, 把石头删掉，之后要加回来
    for hit in hits: #有值就代表碰撞了
        
        new_rock()
        
        Explosion(hit.rect.center, 'small') #石头撞到飞船是小爆炸对象
        #all_sprites.add(expl) #这个小精灵要被更新，就要加入组里，被加入。。。
        #expl.add(all_sprites) #但小精灵也可以把自己加入组中，小精灵自己有个add方法
        #能不能自动生成之时就加入呢？看看在init里直接调用下add
        
        player.health -= hit.radius #hits= {rock1, rock2}碰撞到的
        if player.health <= 0:
            death_expl = Explosion(player.rect.center, 'player')
            all_sprites.add(death_expl)
            die_sound.play()
            player.lives -= 1
            player.health = 100
            player.hide()
    ###石头飞船相撞###
    
    ###宝物飞船相撞###
    hits = pygame.sprite.spritecollide(player, powers, True) #sprite碰撞，默认矩形碰撞, 把石头删掉，之后要加回来
    for hit in hits:
        if hit.type == 'shield':
            shield_sound.play()
            player.health += 20
            if player.health > 100:
                player.health = 100
        if hit.type == 'gun':
            gun_sound.play()
            player.gunup() #在这里加倍子弹
    ###宝物飞船相撞###

    #这种不属于大世界的交互，主角可以自己判断自己死了，并且埋葬了，就完成了
    #大世界的交互是属于两个精灵之间的碰撞，都是神，都要结束对方可不行，
    #大世界的交互，只能由外界来判断两者，不能内部判断对方。不准。
    #if player.lives <= 0 and not death_expl.alive(): #并且die动画不存在，放完了
    #if player.lives <= 0 : #并且die动画不存在，放完了
        #print(player.lives)
        #print(death_expl.alive())
        #running = False
        #show_init = True 
    ###大世界交互规则#################################

    #显示画面
    clock.tick(FPS) #在一秒钟之内最多执行次数，快和更快电脑一样
    all_sprites.update() #所有sprite的组update，因此要在sprite里写这个函数
    screen.fill(BLACK)
    screen.blit(background_img, (0,0)) #把这图片画上去built-in
    all_sprites.draw(screen) #把所有sprite画到screen上
    draw_text(screen, str(score), 18, WIDTH/2, 10)
    draw_health(screen, player.health, 5, 15)
    draw_lives(screen, player.lives, player_mini_img, WIDTH - 150, 15)
    pygame.display.update() #更新画面

pygame.quit()

