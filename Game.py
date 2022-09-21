from cmath import rect
import re
from time import process_time_ns
from tkinter import Toplevel
import pygame
import sys
import GameMapSource


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =   (255, 0, 0)
GREEN = (0, 255, 0)
BLUE =  (0, 0, 255)


## 顯示主要surface
def game_display():
    global screenwidth, screenheight, screen, screensize, screenscale
    screenscale = 1
    screensize = screenwidth, screenheight = 1280*screenscale, 704*screenscale
    screen = pygame.display.set_mode(screensize)


game_display()

background = pygame.image.load("BG.png").convert_alpha()
backgroundrect = background.get_rect()
tile_sky = pygame.image.load("tile_sky.png").convert_alpha()
tile_dirt = pygame.image.load("tile_dirt.png").convert_alpha()

## 牆壁tile
class wall(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=(width, height))

    def display(self):
        screen.blit(self.image, self.rect)

## 非牆壁tile 
class tile(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=(width, height))

    def display(self):
        screen.blit(self.image, self.rect)


tilegroup,wallgroup,wallrectLIst = pygame.sprite.Group(),pygame.sprite.Group(),[]


##　地圖製作
def Create_map(map_str):
    for y, line in enumerate(map_str[1:]):
        for x, c in enumerate(line):
            if c == "W":
                wallgroup.add(wall(x*32, y*32, tile_dirt))
                print(x*32,y*32)



collide_top ,collide_down ,collide_right,collide_left  =[],[],[],[] ## 玩家碰撞列表
## 玩家
class Player(pygame.sprite.Sprite):

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.pos = (self.width, self.height)
        self.image = pygame.image.load("tile_player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(width, height))
        self.movespeed = 5
        self.gravityspeed = 3.2
        self.jumpforce = 100
        self.jumpspeed = 10
        self.isjump = False
        self.isground = False

    ## 重力
    def gravity(self):

        self.rect.y += self.gravityspeed  # how fast player falls
        if pygame.sprite.spritecollide(player, wallgroup, 0, None): ## 碰撞
            self.gravityspeed = 0

        else:
            self.gravityspeed = 3.2
    ## 移動
    def move(self):
        key = pygame.key.get_pressed()
        global nowposition
        nowposition = self.rect.y
        # 　鍵盤

        if key[pygame.K_w]:
            self.rect.y-=self.movespeed
        if key[pygame.K_w]:
            self.rect.y-=self.movespeed

        # if key[pygame.K_s]:
        #     self.rect.y+=self.movespeed
        if key[pygame.K_a]:
            self.rect.x -= self.movespeed
        if key[pygame.K_d]:
            self.rect.x += self.movespeed
        if key[pygame.K_SPACE]:  # debug
            print(self.isground)
        if key[pygame.K_q]:  # debug
            sys.exit()
    ## 跳躍
    def jump(self):

        self.isjump = True
        endposition = self.rect.y + self.jumpforce
        if self.isground and self.isjump:
            while self.rect.y < endposition:
                self.rect.y += self.movespeed
    ##  繪製碰撞點
    def cheakCollidePoint(self,rect,colbool):
        if  colbool:
            pygame.draw.rect(screen, GREEN, rect)
        else:
            pygame.draw.rect(screen, RED, rect)
    ## 使用函數 and 監測是否碰撞
    def drawCollidePosint(self):
        global topleft,midtop,topright,midleft,center,midright,bottomleft,midbottom,bottomright,\
        topleftBool,topmidBool,toprightBool,midleftBool,midcenterBool,midrightBool,bottomleftBool,\
        bottommidtBool,bottomrightBool

        ## 碰撞點trigger
        topleft = pygame.Rect((self.rect.topleft[0]-10,self.rect.topleft[1]-10),(10,10))
        midtop = pygame.Rect((self.rect.midtop[0]-5,self.rect.midtop[1]-10),(10,10))
        topright = pygame.Rect((self.rect.topright[0],self.rect.topright[1]-10),(10,10))

        midleft = pygame.Rect((self.rect.midleft[0]-10,self.rect.midleft[1]-5),(10,10))
        center = pygame.Rect((self.rect.center[0]-5,self.rect.center[1]-5),(10,10))
        midright = pygame.Rect((self.rect.midright[0],self.rect.midright[1]-5),(10,10))

        bottomleft = pygame.Rect((self.rect.bottomleft[0]-10,self.rect.bottomleft[1]),(10,10))
        midbottom = pygame.Rect((self.rect.midbottom[0]-5,self.rect.midbottom[1]),(10,10))
        bottomright = pygame.Rect(self.rect.bottomright,(10,10))

        ## 碰撞點bool
        topleftBool = bool((pygame.Rect.collidelist(topleft,wallrectLIst) == -1))
        topmidBool = bool((pygame.Rect.collidelist(midtop,wallrectLIst) == -1))
        toprightBool = bool((pygame.Rect.collidelist(topright,wallrectLIst) == -1))

        midleftBool = bool((pygame.Rect.collidelist(midleft,wallrectLIst) == -1))
        midcenterBool = bool((pygame.Rect.collidelist(center,wallrectLIst) == -1))
        midrightBool = bool((pygame.Rect.collidelist(midright,wallrectLIst) == -1))

        bottomleftBool = bool((pygame.Rect.collidelist(bottomleft,wallrectLIst) == -1))
        bottommidtBool = bool((pygame.Rect.collidelist(midbottom,wallrectLIst) == -1))
        bottomrightBool = bool((pygame.Rect.collidelist(bottomright,wallrectLIst) == -1))

    ## 碰撞行為
    def collidbehevior(self):

        # 檢查超出視窗
        if self.rect.right >= screenwidth:
            self.rect.x = screenwidth-64
        if self.rect.left <= 0:
            self.rect.x = 0
        if self.rect.bottom >= screenheight:
            self.rect.y = screenheight
        if self.rect.top <= 0:
            self.rect.y = 0
        # 檢查平台碰撞
        if not topleftBool or not topmidBool or not toprightBool:
            print('topcol')
            if not self.isground:
                self.rect.y +=10
        if not topleftBool or not midleftBool or not bottomleftBool:
            print('leftcol')
            if not self.isground:
                self.rect.x +=30
        if not toprightBool or not midrightBool or not bottomrightBool:
            print('rightcol')
            if not self.isground:
                self.rect.x -=30
        if not bottomleftBool or not bottommidtBool or not bottomrightBool:
            print('bottoncol')
            self.isground = True
        else:
            self.isground = False
    ## 玩家顯示
    def display(self):
        screen.blit(self.image, self.rect)
    ## 持續更新函數
    def update(self):
        self.display()
        self.gravity()
        self.move()
        self.drawCollidePosint()
        self.collidbehevior()

    ## 顯示碰撞格 dubug

        self.cheakCollidePoint(topleft,topleftBool)
        self.cheakCollidePoint(midtop,topmidBool)
        self.cheakCollidePoint(topright,toprightBool)
        self.cheakCollidePoint(midleft,midleftBool)
        self.cheakCollidePoint(center,midcenterBool)
        self.cheakCollidePoint(midright,midrightBool)
        self.cheakCollidePoint(bottomleft,bottomleftBool)
        self.cheakCollidePoint(midbottom,bottommidtBool)
        self.cheakCollidePoint(bottomright,bottomrightBool)



player = Player(10, 10)
background = pygame.transform.scale(background, (1280, 704))
Create_map(GameMapSource.getMapStr(1))
wallrectLIst = [i.rect for i in wallgroup]


while 1:


    screen.fill((0, 0, 0))
    screen.blit(background, backgroundrect)
    wallgroup.draw(screen)

    player.update()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
