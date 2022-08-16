import pygame
from sys import exit
import random

pygame.init()
W, H = 1200, 800
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60

class Present(pygame.sprite.Sprite):
    def __init__(self, speed, width, height, x, y):
        super().__init__()
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('images/goodPresent.png').convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def update(self):
        self.rect.y += self.speed

        if self.rect.y > H + 100:
            present_group.remove(self)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height, dx, dy, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('badPresent.png').convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy



present_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Import images 
BG = pygame.transform.scale(pygame.image.load('Images/bg.jpg').convert_alpha(), (WIN.get_width(), WIN.get_height()))

# Import fonts
font = pygame.font.Font('Fonts/game_over.ttf', 200)

# Texts
start_text = font.render('Press any button to start', True, (0,0,0))
start_text_rect = start_text.get_rect(center = (W/2, H/2))

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 100)


def game():
    score = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                exit()
            
            if event.type == timer:
                present_group.add(Present(12, 100, 100, random.randint(100, WIN.get_width() - 100), random.randint(-150, -100)))

        for present in present_group:
            if present.rect.collidepoint(pygame.mouse.get_pos()):
                present_group.remove(present)
                score += 10
        
        WIN.blit(BG, (0, 0))
        
        # Update sprites
        present_group.draw(WIN)
        present_group.update()

        # Update score
        score_text = font.render(f'score: {score}', True, (255, 255, 255))
        score_text_rect = score_text.get_rect(midleft = (W - 500, H - 75 ))
        WIN.blit(score_text, score_text_rect)

        pygame.display.update()
        clock.tick(FPS)


def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                exit()
            
            if event.type == pygame.KEYDOWN:
                game()

        WIN.fill((255, 255, 255))
        WIN.blit(start_text, start_text_rect)


        pygame.display.update()
        clock.tick(FPS)




main()