import pygame
from sys import exit
import math
import random

W, H = 1600, 1200
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 120

class Player:
    def __init__(self, width, height, color, x, y):
        self.width = width
        self.height = height
        self.color = color
        self.speed = [0,0,0,0]
        self.topSpeed = 7
        self.lowestSpeed = 0
        self.acceleration = 0.1
        self.accelerationDown = 0.1
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

        if keys[pygame.K_w]:
            self.speed[3] += self.acceleration
            if self.speed[3] >= self.topSpeed:
                self.speed[3] = self.topSpeed
        else:
            self.speed[3] -= self.accelerationDown
            if self.speed[3] <= self.lowestSpeed:
                self.speed[3] = self.lowestSpeed
        
        if keys[pygame.K_s]:
            self.speed[2] += self.acceleration
            if self.speed[2] >= self.topSpeed:
                self.speed[2] = self.topSpeed
        else:
            self.speed[2] -= self.accelerationDown
            if self.speed[2] <= self.lowestSpeed:
                self.speed[2] = self.lowestSpeed

        if keys[pygame.K_a]:
            self.speed[1] += self.acceleration
            if self.speed[1] >= self.topSpeed:
                self.speed[1] = self.topSpeed
        else:
            self.speed[1] -= self.accelerationDown
            if self.speed[1] <= self.lowestSpeed:
                self.speed[1] = self.lowestSpeed
        
        if keys[pygame.K_d]:
            self.speed[0] += self.acceleration
            if self.speed[0] >= self.topSpeed:
                self.speed[0] = self.topSpeed
        else:
            self.speed[0] -= self.accelerationDown
            if self.speed[0] <= self.lowestSpeed:
                self.speed[0] = self.lowestSpeed
        
        self.rect.y -= self.speed[3]
        self.rect.y += self.speed[2]
        self.rect.x -= self.speed[1]
        self.rect.x += self.speed[0]

        if self.rect.right >= W:
            self.rect.right = W
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= H:
            self.rect.bottom = H

    
    def create_bullet(self):
        bullet_group.add(Bullet(10, 10, (255,0,0), 10, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.rect.centerx, self.rect.centery))


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

class Astroid(pygame.sprite.Sprite):
    def __init__(self, width, height, color, dx, dy, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.top > H:
            astroid_group.remove(self)

bullet_group = pygame.sprite.Group()
player = Player(50, 50, (0,0,0), W/2, H/2)

astroid_group = pygame.sprite.Group()

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == timer:
            astroid_group.add(Astroid(100, 100, (255, 0, 0), random.randint(-5, 5), random.randint(3, 5), random.randint(0, W), -100))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if event.button == 1:
            player.create_bullet()
    
    WIN.fill((255,255,255))

    # Update sprites
    bullet_group.draw(WIN)
    bullet_group.update()
    player.draw()
    player.update()
    astroid_group.draw(WIN)
    astroid_group.update()

    pygame.display.update()
    clock.tick(FPS)
