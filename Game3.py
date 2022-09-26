import sys
import pygame as pg 
import pymunk as pm
pg.init()


clock =pg.time.Clock()


screen = pg.display.set_mode((1280,720))
space = pm.Space()
space.gravity=(0,900)

line_body = pm.Body(body_type=pm.Body.STATIC)
line = pm.Segment(line_body,(10,500),(1080,700),5)

box_body = pm.Body(1,100,body_type=pm.Body.DYNAMIC)
box_body.position =(100,100)
box_shape = pm.BB(1,5,20,10)

ball_body = pm.Body(1,100,body_type=pm.Body.DYNAMIC)
ball_body.position = (150,150)
ball_shape = pm.Circle(ball_body,50)

space.add(ball_body,ball_shape)
space.add(line_body,line)
space.add(box_body,box_shape)

run = 1
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:sys.exit()
    screen.fill((255,255,255))
    pg.draw.circle(screen,(0,0,0),ball_body.position,50)
    pg.draw.line(screen,(0,0,0),(10,500),(1080,700),5)
    pg.draw.rect(screen,(0,0,0),(10,20,20,10),1)
    space.step(1/50)
    pg.display.update()
    clock.tick(100)
    key = pg.key.get_pressed()
    if key[pg.K_SPACE]:
        print('SPACE')
