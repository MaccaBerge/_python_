import pygame
from sys import exit

pygame.init()
W, H = 1200, 800
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 120

class Firkant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.gravity = 1
    
    def apply_gravity(self):
        self.rect.y += self.gravity

firkant_gruppe = pygame.sprite.Group()

firkant = Firkant(100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            firkant_gruppe.add(Firkant(event.pos[0], event.pos[1]))
    
    WIN.fill((255, 255, 255))

    for i in firkant_gruppe:
       i.apply_gravity()
    
    firkant_gruppe.draw(WIN)
    firkant_gruppe.update()


    pygame.display.update()
    clock.tick(FPS)