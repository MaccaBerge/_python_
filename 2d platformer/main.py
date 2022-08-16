import pygame, sys
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()
FPS = 60

level = Level()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(BG_COLOR)
    level.run()
    
    pygame.display.update()
    clock.tick(FPS)