#!/usr/bin/env python3

###1.导入语言包##############################
import pygame
import cv2
#sprite, 小精灵，游戏的所有元素
import random
import os
import numpy as np


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
fireSprites = pygame.sprite.Group()
goldSprites = pygame.sprite.Group()
WIDTH = 200
HEIGHT = 300

#pygame的开始及设置
def startPygame(width, height, title='title'):
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen
screen = startPygame(WIDTH, HEIGHT, 'HideFire')

def loadFont(fontName = 'arial'):
    if fontName != 'arial':
        return os.path.join((fontName))
    else:
        return pygame.font.match_font(fontName)
defaultFont = loadFont()

#画文字，画矩形，画开始
def draw_text(surface, text, size, centerx, y, font=defaultFont, color=WHITE): #任意位置画字
    textSurf = pygame.font.Font(font, size).render(text, True, color)
    text_rect = textSurf.get_rect() #可以这样直接得到rect,也可以直接高宽
    text_rect.centerx = centerx #x居中，不用管多长
    text_rect.top = y #不用管多高，置顶，就向下排就行
    #text_rect.center = center #直接中心不方便调控
    #print(center) #(centerx, centery)
    surface.blit(textSurf, text_rect)


class Fire(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)
        self.add(fireSprites)
    
        self.image = pygame.Surface((7, 7))
        self.image.fill(WHITE)
    
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -30)
        self.speedy = random.randrange(2, 5)
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            Fire()
            self.kill()

class Gold(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)
        self.add(goldSprites)
    
        self.image = pygame.Surface((14, 14))
        self.image.fill(GOLD)
    
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = random.randrange(4, 6)
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            Gold()
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.add(allSprites)

        self.image = pygame.Surface((30, 5))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.y = HEIGHT - 2
        self.rect.bottom = HEIGHT

        self.score = 0
        self.speedx = 7
    
    def update(self):
        pass

class GameState():
    def __init__(self):
        for i in allSprites:
            i.kill()
        for i in range(7):
            Fire()
        for i in range(8):
            Gold()
        self.player = Player()

    def frame_step(self, input_actions=[0, 1, 0]):
        clock.tick(60)
        pygame.event.pump() #这个是用来内部处理event的，要注释掉来搞

        #在这里，用pygame获取键盘输入来获得input_actions，自动时要注释掉
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #exit(0)
        #key_pressed = pygame.key.get_pressed()
        #if key_pressed[pygame.K_LEFT]:
            #input_actions = [1, 0, 0]
        #elif key_pressed[pygame.K_RIGHT]:
            #input_actions = [0, 0, 1]
        #else:
            #input_actions = [0, 1, 0]
        #print(input_actions)

        reward = 0.1
        terminal = False

        if sum(input_actions) != 1:
            raise ValueError('Multiple input actions!')
        
        #根据动作来判断player移动
        allSprites.update() #player里没有update，手动update后检查
        if self.player.rect.x < 0:
            self.player.rect.x = 0
        elif self.player.rect.right > WIDTH:
            self.player.rect.right = WIDTH
        else:
            if input_actions[0] == 1:
                self.player.rect.x -= self.player.speedx
            elif input_actions[2] == 1:
                self.player.rect.x += self.player.speedx

        #检查相撞确认分数
        hits = pygame.sprite.spritecollide(self.player, fireSprites, True)
        for hit in hits:
            self.player.score += 1
            Fire()
            reward = 1
        hits = pygame.sprite.spritecollide(self.player, goldSprites, True)
        for hit in hits:
            terminal = True
            self.__init__()
            reward = -1
        
        #更新显示#处理返回
        screen.fill(BLACK)
        allSprites.draw(screen)
        draw_text(screen, str(self.player.score), 20, WIDTH/2, 20, color=RED)
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.update()

        return image_data, reward, terminal

#game_state = GameState()
#while True:
    #game_state.frame_step()

