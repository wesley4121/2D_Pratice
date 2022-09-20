import pygame
import sys
import GameMapSource


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



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


class wall(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=(width, height))

    def display(self):
        screen.blit(self.image, self.rect)


class tile(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=(width, height))

    def display(self):
        screen.blit(self.image, self.rect)


tilegroup,wallgroup = pygame.sprite.Group(),pygame.sprite.Group()


def Create_map(map_str):
    for y, line in enumerate(map_str[1:]):
        for x, c in enumerate(line):
            if c == "W":
                wallgroup.add(wall(x*32, y*32, tile_dirt))
                
                

            if c == " ":
                tilegroup.add(tile(x*32, y*32, tile_sky))


collide_top ,collide_down ,collide_right,collide_left  =[],[],[],[] ##player_collidePointList
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
        self.isjump = False
        self.jumpforce = 1.1
        self.jumpspeed = 10
        self.collision = [False] * 9

    def draw_point(self, screen, pos, collision):
        if not collision:
            box = pygame.Rect(pos,(10,10))
            pygame.draw.rect(screen, GREEN, box)
        else:
            pygame.draw.rect(screen, RED, box)

    def draw(self, screen):

        pygame.draw.rect(screen, WHITE, self.rect, 1)
        self.draw_point(screen, (self.rect.topleft[0]-10,self.rect.topleft[1]-10), self.collision[0])
        self.draw_point(screen, (self.rect.midtop[0]-5,self.rect.midtop[1]-10), self.collision[1])
        self.draw_point(screen, (self.rect.topright[0],self.rect.topright[1]-10), self.collision[2])

        self.draw_point(screen, (self.rect.midleft[0]-10,self.rect.midleft[1]-5), self.collision[3])
        self.draw_point(screen, (self.rect.center[0]-5,self.rect.center[1]-5), self.collision[4])
        self.draw_point(screen, (self.rect.midright[0],self.rect.midright[1]-5), self.collision[5])

        self.draw_point(screen, (self.rect.bottomleft[0]-10,self.rect.bottomleft[1]), self.collision[6])
        self.draw_point(screen, (self.rect.midbottom[0]-5,self.rect.midbottom[1]), self.collision[7])
        self.draw_point(screen, self.rect.bottomright, self.collision[8])

    

    def gravity(self):

        self.rect.y += self.gravityspeed  # how fast player falls
        if pygame.sprite.spritecollide(player, wallgroup, 0, None): ## 碰撞
            self.gravityspeed = 0
        else:
            self.gravityspeed = 3.2

    def move(self):
        key = pygame.key.get_pressed()

        # 　鍵盤

        if key[pygame.K_w]:
            self.rect.y -= self.movespeed
        # if key[pygame.K_s]:
        #     self.rect.y+=self.movespeed
        if key[pygame.K_a]:
            self.rect.x -= self.movespeed
        if key[pygame.K_d]:
            self.rect.x += self.movespeed
        if key[pygame.K_SPACE]:  # debug
            print(isground)
        if key[pygame.K_q]:  # debug
            sys.exit()

    def jump(self):
        nowposition = self.rect.y
        endposition = self.rect.y * self.jumpforce
        if isground:
            while self.rect.y < endposition:
                pass
    
    def collidcheak(self):
        
        
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
    def display(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.collidcheak()
        self.display()
        self.gravity()
        self.move()


isground = False
player = Player(10, 10)
background = pygame.transform.scale(background, (1280, 704))
Create_map(GameMapSource.getMapStr(1))


while 1:

    screen.fill((0, 0, 0))
    screen.blit(background, backgroundrect)
    wallgroup.draw(screen)
    player.update()
    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
