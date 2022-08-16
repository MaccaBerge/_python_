from msilib.schema import SelfReg
import pygame
from sys import exit

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

W, H = 1200, 800
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 120

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.motion = [0, 0]
        #print(self.motion)
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    def update(self):
        self.rect.x += self.motion[0] * 10
        self.rect.y += self.motion[1] * 10
    
    def deadzone(self):
        if abs(self.motion[0]) < 0.1:
            self.motion[0] = 0
        if abs(self.motion[1]) < 0.1:
            self.motion[1] = 0


player = Player(W / 2, H / 2)

while True:
    

    WIN.fill((255, 255, 255))
    player.draw()
    player.update()
    player.deadzone()
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.JOYAXISMOTION:
            if event.axis < 2:
               player.motion[event.axis] = event.value

    pygame.display.update()
    clock.tick(FPS)