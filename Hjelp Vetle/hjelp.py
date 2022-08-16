import pygame
from sys import exit
import math
import random

W, H = 1200, 800
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 120

class Player:
    def __init__(self, width, height, color, dx, dy, x, y):
        self.width = width
        self.height = height
        self.color = color
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    def update(self):
        # Move the player (up, down, left, right)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.dy
        
        if keys[pygame.K_s] and self.rect.bottom < H:
            self.rect.y += self.dy

        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.dx
        
        if keys[pygame.K_d] and self.rect.right < W:
            self.rect.x += self.dx
    
    def create_bullet(self):
        bullet_group.add(Bullet(10, 10, (255,0,0), random.randint(1, 10), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.rect.centerx, self.rect.centery))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, width, height, color, speed, targetx, targety, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.targetx = targetx
        self.targety = targety
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.angle = math.atan2(self.targety - self.y, self.targetx - self.x)
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

        if not self.rect.colliderect(WIN.get_rect()):
            bullet_group.remove(self)



bullet_group = pygame.sprite.Group()
player = Player(50, 50, (0,0,0), 10, 10, W/2, H/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if event.button == 1:
            player.create_bullet()
    
    WIN.fill((255,255,255))

    # Update sprites
    bullet_group.draw(WIN)
    bullet_group.update()
    player.draw()
    player.update()
    player.create_bullet()

    pygame.display.update()
    clock.tick(FPS)
