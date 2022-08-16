from sys import exit
import pygame
from termcolor import colored

def display_score(score, text_color):
    score_surf = font.render(f'{score}', False, (text_color))
    score_rect = score_surf.get_rect(center = (500, 100))
    WIN.blit(score_surf, score_rect)

def draw_text(text, size, col):
    font = 'font/Pixeltype.ttf'
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect(center = (500, 100))
    WIN.blit(text_surface, text_rect)

def col_change(col, dir):
    for i in range(3):
        col[i] += col_spd * dir[i]
        if col[i] >= maximum or col[i] <= minimum:
            dir[i] *= -1

def array_func(col, dir, size):
    for i in range(len(col)):
        draw_text(f'{score}', size, col[i])
        col_change(col[i], dir[i])

pygame.init()

W, H = 1000, 800

WIN = pygame.display.set_mode((W, H))
FOX = pygame.transform.scale(pygame.image.load('fox.png').convert_alpha(), (400, 300))
HEDGEHOG = pygame.transform.scale(pygame.image.load('hedgehog.png').convert_alpha(), (200, 150))
BG = pygame.transform.scale(pygame.image.load('bg2.jpg').convert_alpha(), (W, H))

score = 0
font = pygame.font.Font('zorque.otf', 200)
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)

col_spd = 1

def_col = [[120, 120, 240]]
col_dir = [[-1, 1, 1]]

minimum = 0
maximum = 255

class Button:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.button_surf = img
        self.button_rect = self.button_surf.get_rect(midbottom = (self.x, self.y))

    def draw_button(self, WIN):
        WIN.blit(self.button_surf, self.button_rect)

fox = Button(500, 550, FOX)
hedgehog = Button(150, H, HEDGEHOG)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if fox.button_rect.collidepoint(event.pos):
                score +=1
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hedgehog.button_rect.collidepoint(event.pos):
                score +=1
    
    WIN.fill('white')
    
    if score < 10:
        text_color = 'gray'
        display_score(score, text_color)
        #score += 1
    
    elif score >= 10 and score < 100:
        text_color = '#C46200'
        display_score(score, text_color)
        #score += 1
    
    elif score >= 100 and score < 1326:
        text_color = '#e01a3a'
        display_score(score, text_color)
        #score += 1
    
    elif score >= 1326 and score < 10000:
        text_color = '#E7BD34'
        display_score(score, text_color)
        #score += 1
    
    elif score == 10000:
        text_color = '#E7BD34'
        display_score(score, text_color)

    elif score >= 10001:
        array_func(def_col, col_dir, 200)
    
    fox.draw_button(WIN)
    hedgehog.draw_button(WIN)


    pygame.display.update()
    clock.tick()