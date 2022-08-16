
import pygame
from sys import exit
import random

pygame.init()
W, H = 1500, 1200
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 120
run = True

SOUND = pygame.mixer.Sound('scream.mp3')
IMAGE = pygame.transform.scale(pygame.image.load('anabell.jpeg').convert_alpha(), (W, H))

def scare():
    SOUND.play()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WIN.blit(IMAGE, (0, 0))

        pygame.display.update()
        clock.tick(FPS)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (x, y))
    
    def kill(self):
        enemy_group.remove(self)

enemy_group = pygame.sprite.Group()

number_enemy = 10
for i in range(number_enemy):
    enemy_group.add(Enemy(random.randint(100, 1400), random.randint(100, 1100)))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for enemy in enemy_group:
                if enemy.rect.collidepoint(event.pos):
                    enemy.kill()
    
    if len(enemy_group) == 0:
        scare()
    
    WIN.fill((0, 0, 0))
    
    enemy_group.draw(WIN)
    enemy_group.update()

    pygame.display.update()
    clock.tick(FPS)