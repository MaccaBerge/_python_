import pygame
from sys import exit
import random

pygame.init()
W, H = 1200, 800
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60

class Player: 
    def __init__(self, width, height, color, x, y):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and player.rect.left > 0:
            self.rect.x -= 10
        if keys[pygame.K_d] and player.rect.right < W:
            self.rect.x += 10

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def update(self):
        self.rect.y += 5
        
        if self.rect.y > W + 200:
            obstacles_group.remove(self)
                  
obstacles_group = pygame.sprite.Group()
player = Player(50, 100, (0,0,0), W/2, H/1.3)

obstacles_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacles_timer, 3000)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == obstacles_timer:
            obstacles_group.add(Obstacles(W/3, 100, (0,0,0), random.choice((200, W/2, W-200)), -100))
            
    WIN.fill((255,255,255))
    
    # Draw the player
    player.draw()
    player.update()
    
    # Drawing the obstacles
    obstacles_group.draw(WIN)
    obstacles_group.update()
    
    pygame.display.update()
    clock.tick(FPS)