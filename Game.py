from pygame import SRCALPHA
import pygame  as pg
import pymunk as pm
import sys
import GameMapSource


pg.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =   (255, 0, 0)
GREEN = (0, 255, 0)
BLUE =  (0, 0, 255)


## 顯示主要surface
def game_display():
    global screenwidth, screenheight, screen, screensize, screenscale,map_surface,bg_surface,map_positionX,\
        map_positionY,TILE
    
    screenscale = 1
    stagescale = 1
    STAGEHEIGHT = 704
    STAGEWIDGHT=1280
    TILE = 32
    stageheightscale= 2
    stageTileY = ((TILE*(len(GameMapSource.getMapStr(1))-1))//stageheightscale)
    screensize = screenwidth, screenheight = STAGEWIDGHT*screenscale, STAGEHEIGHT*screenscale
    screen = pg.display.set_mode(screensize)
    map_surface = pg.Surface((STAGEWIDGHT*stagescale,STAGEHEIGHT*stagescale*stageheightscale),pg.SRCALPHA)
    bg_surface = pg.Surface((STAGEWIDGHT*stagescale,STAGEHEIGHT*stagescale*stageheightscale),pg.SRCALPHA)
    map_positionX = 0
    map_positionY = 0
    print((TILE*(len(GameMapSource.getMapStr(1))-1)) //STAGEHEIGHT)

def draw_mapScroltriger():
    global ScrollTriger_rgiht,ScrollTriger_left,ScreenTriger_top,ScrollTriger_top
    ScrollTriger_left =  pg.Rect(0,0,250,720)
    # pygame.draw.rect(screen,RED,ScrollTriger_left)
    ScrollTriger_rgiht =  pg.Rect(1030,0,250,720)
    # pygame.draw.rect(screen,RED,ScrollTriger_rgiht)
    ScrollTriger_top =  pg.Rect(0,0,1280,225)
    # pygame.draw.rect(screen,RED,ScrollTriger_top)
    ScreenTriger_top =  pg.Rect(0,0,1280,2)
    # pygame.draw.rect(screen,RED,ScreenTriger_top)


game_display()
map_scrollspeed = 3
map_startposition =0
background = pg.image.load("BG.png").convert_alpha()
backgroundrect = background.get_rect()
tile_sky = pg.image.load("tile_sky.png").convert_alpha()
tile_dirt = pg.image.load("tile_dirt.png").convert_alpha()

## 牆壁tile
class wall(pg.sprite.Sprite):
    def __init__(self, width, height, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=(width, height))

    def display(self):
        screen.blit(self.image, self.rect)

## 非牆壁tile 
class tile(pg.sprite.Sprite):
    def __init__(self, width, height, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=(width, height))

    def display(self):
        screen.blit(self.image, self.rect)


tilegroup,wallgroup,wallrectLIst = pg.sprite.Group(),pg.sprite.Group(),[]


##　地圖製作
def Create_map(map_str):
    
    for y, line in enumerate(map_str[1:]):
        for x, c in enumerate(line):
            if c == "W":
                wallgroup.add(wall(x*32, y*32, tile_dirt))
                # print(x*32,y*32)
def Move_map(speed):
    # print(map_startposition)
    for w in wallrectLIst:
        w.x+=speed
    


## 玩家
class Player(pg.sprite.Sprite):

    def __init__(self, width, height):
        pg.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.pos = (self.width, self.height)
        self.image = pg.image.load("tile_player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(width, height))
        self.movespeed = 5
        self.gravityspeed = 5
        self.jumpforce = 200
        self.jumpspeed = 5
        self.isjump = False
        self.isground = False
        self.endposition =0
        self.nowposition =0

    # ## 重力
    # def gravity(self):
    #     if not self.isground and not self.isjump:  # how fast player falls
    #         self.rect.y += self.gravityspeed

    ## 移動
    def move(self):
        key = pg.key.get_pressed()
        global map_positionX

        self.jump()

        # 　鍵盤
        if key[pg.K_w]:
            print(self.isground)
            if self.isground :
                self.isjump = True
        # if key[pygame.K_j]: #debug 移動地圖
        #     for w in wallrectLIst:
        #         w.x-=1
        if key[pg.K_a]:
            self.rect.x -= self.movespeed
        if key[pg.K_d]:
            self.rect.x += self.movespeed
        # if key[pygame.K_SPACE]:  


                
        if key[pg.K_q]:  # debug
            sys.exit()
    ## 跳躍
    def jump(self):
        if  self.isjump:
            if self.rect.y > self.endposition and ( topleftBool and  topmidBool and  toprightBool) and not mapbounds_topBool:
                self.rect.y -= self.jumpspeed
                print('end',self.endposition,'now',self.rect.y)
            else:
                self.isjump = False
        else: 
            self.nowposition = self.rect.y
            self.endposition = self.rect.y - self.jumpforce
            print(self.endposition)
    ##  繪製碰撞點
    def cheakCollidePoint(self,rect,colbool):
        if  colbool:
            pg.draw.rect(screen, GREEN, rect)
        else:
            pg.draw.rect(screen, RED, rect)
    ## 使用函數 and 監測是否碰撞
    def drawCollidePosint(self):
        global topleft,midtop,topright,midleft,center,midright,bottomleft,midbottom,bottomright,\
        topleftBool,topmidBool,toprightBool,midleftBool,midcenterBool,midrightBool,bottomleftBool,\
        bottommidtBool,bottomrightBool,mapScroll_rightBool,mapScroll_leftBool,ScreenTriger_top,\
        mapbounds_topBool
        ## 碰撞點trigger
        topleft = pg.Rect((self.rect.topleft[0],self.rect.topleft[1]),(3,3))
        midtop = pg.Rect((self.rect.midtop[0]-20,self.rect.midtop[1]),(40,3))
        topright = pg.Rect((self.rect.topright[0]-3,self.rect.topright[1]),(3,3))

        midleft = pg.Rect((self.rect.midleft[0],self.rect.midleft[1]-45),(2,90))
        center = pg.Rect((self.rect.center[0]-5,self.rect.center[1]-5),(10,10))
        midright = pg.Rect((self.rect.midright[0]-2,self.rect.midright[1]-45),(2,90))

        bottomleft = pg.Rect((self.rect.bottomleft[0],self.rect.bottomleft[1]),(2,2))
        midbottom = pg.Rect((self.rect.midbottom[0]-20,self.rect.midbottom[1]),(40,2))
        bottomright = pg.Rect(self.rect.bottomright,(2,2))

        ## 碰撞點bool
        topleftBool = bool((pg.Rect.collidelist(topleft,wallrectLIst) == -1))
        topmidBool = bool((pg.Rect.collidelist(midtop,wallrectLIst) == -1))
        toprightBool = bool((pg.Rect.collidelist(topright,wallrectLIst) == -1))

        midleftBool = bool((pg.Rect.collidelist(midleft,wallrectLIst) == -1))
        midcenterBool = bool((pg.Rect.collidelist(center,wallrectLIst) == -1))
        midrightBool = bool((pg.Rect.collidelist(midright,wallrectLIst) == -1))

        bottomleftBool = bool((pg.Rect.collidelist(bottomleft,wallrectLIst) == -1))
        bottommidtBool = bool((pg.Rect.collidelist(midbottom,wallrectLIst) == -1))
        bottomrightBool = bool((pg.Rect.collidelist(bottomright,wallrectLIst) == -1))
        ## 視窗
        mapScroll_rightBool = pg.Rect.colliderect(self.rect,ScrollTriger_rgiht)
        mapScroll_leftBool = pg.Rect.colliderect(self.rect,ScrollTriger_left)
        ## 跳躍頂碰撞
        mapbounds_topBool = pg.Rect.colliderect(self.rect,ScreenTriger_top)
        

    ## 碰撞行為
    def collidbehevior(self):
        global map_startposition 
        # 檢查超出視窗
        if self.rect.right >= screenwidth:
            self.rect.x = screenwidth-64
        if self.rect.left <= 0:
            self.rect.x = 0
        # if self.rect.bottom >= screenheight:
        #     self.rect.y = screenheight
        if self.rect.top <= 0:
            self.rect.y = 0
        # 檢查移動地圖
        if mapScroll_leftBool:
            if map_startposition >0:
                Move_map(map_scrollspeed)
                map_startposition-=1
        if mapScroll_rightBool:
                Move_map(-map_scrollspeed)
                map_startposition+=1

        # 檢查平台碰撞
        if not topleftBool or not topmidBool or not toprightBool:#上
            # print('topcol')
            if not self.isground:
                self.rect.y +=self.movespeed
        if not topleftBool or not midleftBool : #左
            # print('leftcol')
            self.rect.x +=self.movespeed
        if not toprightBool or not midrightBool :#右
            # print('rightcol')
            self.rect.x -=self.movespeed
        if not bottomleftBool or not bottommidtBool or not bottomrightBool:#下
            # print('bottoncol')
            self.isground = True
        else:
            self.isground = False
        self.display()
    ## 玩家顯示
    def display(self):
        screen.blit(self.image, self.rect)
    ## 持續更新函數
    def update(self):
        # self.gravity()
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



player = Player(250, 150)
background = pg.transform.scale(background, (1280, 704))
Create_map(GameMapSource.getMapStr(1))
wallrectLIst = [i.rect for i in wallgroup]


while 1:

    # bg_surface.blit(background, backgroundrect)
    # screen.blit(bg_surface,(0,0))
    screen.blit(map_surface,(map_positionX,map_positionY))
    map_surface.blit(background, backgroundrect)
    wallgroup.draw(map_surface)
    draw_mapScroltriger()

    player.update()




    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    pg.display.update()
