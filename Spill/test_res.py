import pygame
import sys

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game bade')
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

fullscreen = False

while True:

    screen.fill((0, 0, 50))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width() - 5 - (screen.get_width() / 5), 50, screen.get_width() / 5, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
    
    pygame.display.update()
    clock.tick(60)