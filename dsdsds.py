import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True
spriteVY = 3
clock = pygame.time.Clock()

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.vel = (0, 0)
        self.image = pygame.Surface((100, 200))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = (x, y))

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((200, 10))
        self.image.fill((142, 212, 25))
        self.rect = self.image.get_rect(topleft = (x, y))

sprite = MySprite(100, 100)
platform = Platform(50, 20)
group = pygame.sprite.Group([sprite, platform])

on_ground = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_SPACE]: sprite.rect.y -= 10
    if pygame.key.get_pressed()[pygame.K_d]: sprite.rect.x += 10
    if pygame.key.get_pressed()[pygame.K_a]: sprite.rect.x -= 10

    if platform.rect.colliderect(sprite.rect):
        print("hit")

    if sprite.rect.x >= 300:
        sprite.rect.x = 300
    if sprite.rect.x <= 0:
        sprite.rect.x = 0
    if not on_ground:
        sprite.rect.y += spriteVY
        spriteVY -= 3

    screen.fill((0, 0, 0))
    group.draw(screen)
    pygame.display.flip()
    clock.tick(24)