from pygame import SRCALPHA
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
    global screenwidth, screenheight, screen, screensize, screenscale,map_surface,bg_surface,map_positionX,\
        map_positionY
    
    screenscale = 1
    stagescale = 1
    screensize = screenwidth, screenheight = 1280*screenscale, 704*screenscale
    screen = pygame.display.set_mode(screensize)
    map_surface = pygame.Surface((1280*stagescale,704*stagescale),pygame.SRCALPHA)
    bg_surface = pygame.Surface(screensize,pygame.SRCALPHA)
    map_positionX = 0
    map_positionY = 0

def draw_mapScroltriger():
    global ScreenTriger_rgiht,ScreenTriger_left
    ScreenTriger_left =  pygame.Rect(0,0,200,720)
    # pygame.draw.rect(screen,RED,ScreenTriger_left)
    ScreenTriger_rgiht =  pygame.Rect(1080,0,200,720)
    # pygame.draw.rect(screen,RED,ScreenTriger_rgiht)


game_display()
map_scrollspeed = 5
map_startposition =0
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
                # print(x*32,y*32)
def Move_map(speed):
    # print(map_startposition)
    for w in wallrectLIst:
        w.x+=speed
    


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
        self.gravityspeed = 1
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
            self.gravityspeed = 1
    ## 移動
    def move(self):
        key = pygame.key.get_pressed()
        global nowposition,map_positionX
        nowposition = self.rect.y
        # 　鍵盤

        if key[pygame.K_w]:
            self.rect.y-=self.movespeed
        # if key[pygame.K_j]: #debug 移動地圖
        #     for w in wallrectLIst:
        #         w.x-=1
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
        bottommidtBool,bottomrightBool,mapScroll_rightBool,mapScroll_leftBool

        ## 碰撞點trigger
        topleft = pygame.Rect((self.rect.topleft[0],self.rect.topleft[1]),(3,3))
        midtop = pygame.Rect((self.rect.midtop[0]-20,self.rect.midtop[1]),(40,3))
        topright = pygame.Rect((self.rect.topright[0]-3,self.rect.topright[1]),(3,3))

        midleft = pygame.Rect((self.rect.midleft[0],self.rect.midleft[1]-45),(2,90))
        center = pygame.Rect((self.rect.center[0]-5,self.rect.center[1]-5),(10,10))
        midright = pygame.Rect((self.rect.midright[0]-2,self.rect.midright[1]-45),(2,90))

        bottomleft = pygame.Rect((self.rect.bottomleft[0],self.rect.bottomleft[1]),(2,2))
        midbottom = pygame.Rect((self.rect.midbottom[0]-20,self.rect.midbottom[1]),(40,2))
        bottomright = pygame.Rect(self.rect.bottomright,(2,2))

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

        mapScroll_rightBool = pygame.Rect.colliderect(self.rect,ScreenTriger_rgiht)
        mapScroll_leftBool = pygame.Rect.colliderect(self.rect,ScreenTriger_left)

    ## 碰撞行為
    def collidbehevior(self):
        global map_startposition 
        # 檢查超出視窗
        if self.rect.right >= screenwidth:
            self.rect.x = screenwidth-64
        if self.rect.left <= 0:
            self.rect.x = 0
        if self.rect.bottom >= screenheight:
            self.rect.y = screenheight
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



player = Player(250, 150)
background = pygame.transform.scale(background, (1280, 704))
Create_map(GameMapSource.getMapStr(1))
wallrectLIst = [i.rect for i in wallgroup]


    
while 1:

    screen.blit(map_surface,(map_positionX,map_positionY))
    map_surface.blit(background, backgroundrect)
    wallgroup.draw(map_surface)
    draw_mapScroltriger()

    player.update()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
