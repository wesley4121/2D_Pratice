
import pygame
import sys,GameMapSource


pygame.init()
size = width,height = 1280,704
screen = pygame.display.set_mode(size)



class wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tile_dirt.png").convert_alpha()
        self.rect = self.image.get_rect()
        
tile_dirt = wall()
tile_sky = pygame.image.load("tile_sky.png").convert_alpha()

class Maptool:

    @staticmethod
    def Create_map(map_str,screen,dirt,sky):
        for y,line in enumerate(map_str[1:]):
            for x,c in enumerate(line):
                if c == "W":
                    screen.blit(dirt.image,(x*32,y*32))
                if c == " ":
                    screen.blit(sky,(x*32,y*32))


class whiteCube(pygame.sprite.Sprite):
        
    def __init__(self,width,height ):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.pos = (self.width,self.height)
        self.image = pygame.image.load("whiteCube.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.movespeed = 5
        
    def gravity(self):
        self.height += 3.2 # how fast player falls

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.height-=self.movespeed
        if key[pygame.K_s]:
            self.height+=self.movespeed
        if key[pygame.K_a]:
            self.width-=self.movespeed
        if key[pygame.K_d]:
            self.width+=self.movespeed
    def display(self,*move):
        if move[0] >= 1:
            screen.blit(self.image,(self.width,self.height))
        else:
            screen.blit(self.image,self.rect)


cubeA = whiteCube(0,0)
cubeb = whiteCube(500,500)



while 1:
    screen.fill((0,0,0))
    Maptool.Create_map(GameMapSource.getMapStr(1),screen,tile_dirt,tile_sky)
    cubeA.display(1)
    cubeA.gravity()
    cubeA.move()
    if pygame.sprite.collide_rect(cubeA,cubeb):
        print('yes')

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    pygame.display.update()
