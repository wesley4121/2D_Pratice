
import pygame
import sys,GameMapSource


pygame.init()
size = width,height = 1280,704
screen = pygame.display.set_mode(size)

tile_sky = pygame.image.load("tile_sky.png").convert_alpha()
tile_dirt = pygame.image.load("tile_dirt.png").convert_alpha()

class wall(pygame.sprite.Sprite):
    def __init__(self,width,height,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft = (width,height))
    def display(self):
        pass
        


class tile(pygame.sprite.Sprite):
    def __init__(self,width,height,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft = (width,height))

group = pygame.sprite.Group()
def Create_map(map_str):
    for y,line in enumerate(map_str[1:]):
        for x,c in enumerate(line):
            if c == "W":
                group.add(wall(x*32,y*32,tile_dirt))
            if c == " ":
                group.add(tile(x*32,y*32,tile_sky))


class whiteCube(pygame.sprite.Sprite):
        
    def __init__(self,width,height ):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.pos = (self.width,self.height)
        self.image = pygame.image.load("whiteCube.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (width,height))
        self.movespeed = 5
        
    def gravity(self):
        self.rect.y += 3.2 # how fast player falls

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.rect.y-=self.movespeed
        if key[pygame.K_s]:
            self.rect.y+=self.movespeed
        if key[pygame.K_a]:
            self.rect.x-=self.movespeed
        if key[pygame.K_d]:
            self.rect.x+=self.movespeed
    def display(self,*move):
        if move[0] >= 1:
            screen.blit(self.image,self.rect)



cubeA = whiteCube(0,0)
cubeb = whiteCube(500,500)

Create_map(GameMapSource.getMapStr(1))
while 1:
    screen.fill((0,0,0))

    for t in group.sprites():
        screen.blit(t.image,t.rect)
    for w in group.sprites(): ##碰撞
        if w 
            pygame.sprite.collide_rect(cubeA,w.rect)
    cubeA.display(1)
    cubeA.gravity()
    cubeA.move()
    cubeb.display(1)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    pygame.display.update()
