import sys
import pygame as pg 
import  pymunk as pm






def create_mob(space):
    body = pm.Body(1,200,body_type=pm.Body.DYNAMIC)
    body.position=(150,150)
    shape = pm.Circle(body,50)
    space.add(body,shape)
    return shape
def draw_mob(mobs):
    for mob in mobs:
        pg.draw.circle(screen,(0,0,0),mob.body.position,50)
    
def static_mob(space):
    body = pm.Body(body_type=pm.Body.STATIC)
    body.position=(140,500)
    shape = pm.Circle(body,50)
    space.add(body,shape)
    return shape
pg.init()
screen = pg.display.set_mode((600,600))
clock = pg.time.Clock()
space = pm.Space()
space.gravity = (0,100)
mobs = []

mobs.append(create_mob(space))
mobs.append(static_mob(space))

run = 1
while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:sys.exit()
    screen.fill((255,255,255))
    draw_mob(mobs)
    space.step(1/50)
    pg.display.update()
    clock.tick(120)