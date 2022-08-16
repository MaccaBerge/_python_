import pygame
from sys import exit
import random

# url for the game https://www.icone-png.com/theme-vacance-noel.php

# Start all functions
pygame.init()
pygame.mixer.init()

# Make the pygame window 
W, H = 1200, 800
WIN = pygame.display.set_mode((W, H))

# Make a clock and FPS
clock = pygame.time.Clock()
FPS = 60
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

pygame.mixer.music.load('Sounds/bg_music.wav')
pygame.mixer.music.play(-1, 0.0, 3)

class Cursor:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('Images/cursor.png').convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Presents(pygame.sprite.Sprite):
    def __init__(self, surface, value, speed, width, height, x, y):
        super().__init__()
        self.surface = surface
        self.value = value
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load(self.surface).convert_alpha(), (self.width, self.height))
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
        self.gravity = 2
        self.image = pygame.transform.scale(pygame.image.load('Images/badPresent.png').convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.rect.y += self.gravity
        self.gravity += 0.1
        if self.rect.y > H + 100:
            enemy_group.remove(self)

class Points(pygame.sprite.Sprite):
    def __init__(self, size, point, x, y):
        super().__init__()
        self.size = size 
        self.point = point
        self.x = x
        self.y = y
        self.start_time = pygame.time.get_ticks()
        self.current_time = 0
        self.font = pygame.font.Font('Fonts/game_over.ttf', self.size)
        self.image = self.font.render(f'+{point}', True, (255, 255, 255))
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def update(self):
        self.current_time = pygame.time.get_ticks()
        
        if self.current_time - self.start_time > 750:
            point_group.remove(self)


present_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
point_group = pygame.sprite.Group()

cursor = Cursor(80, 80, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

# Import images 
BG = pygame.transform.scale(pygame.image.load('Images/bg2.jpg').convert_alpha(), (WIN.get_width(), WIN.get_height()))

# Import fonts
font = pygame.font.Font('Fonts/game_over.ttf', 200)
font2 = pygame.font.Font('Fonts/game_over.ttf', 150)
font3 = pygame.font.Font('Fonts/game_over.ttf', 100)
# Texts
start_text = font.render('Press any button to start', True, (0,0,0))
start_text_rect = start_text.get_rect(center = (W/2, H/2))
secret_text = font3.render('Sigurd (10F) vil vippse deg 500kr hvis du faar 2500 poeng', True, (0, 0, 0))
secret_text_rect = secret_text.get_rect(center = (W/2, H - 70))

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 100)

def empty_groups():
    enemy_group.empty()
    present_group.empty()
    point_group.empty()


def game():
    score = 0
    ticks = 0
    time = 20
    pygame.mouse.set_pos(W/2, H/2)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                exit()
            
            if event.type == timer:
                ticks += 100

                if ticks % 100 == 0:
                    present_group.add(Presents('Images/goodPresent.png', 10, 12, 100, 100, random.randint(100, WIN.get_width() - 100), random.randint(-150, -100)))
                
                if ticks % 1000 == 0:
                    enemy_group.add(Enemy(100, 100, random.randint(-7, -2), random.randint(-12, -8), W + 50, H/random.randint(1, 4)))
                    enemy_group.add(Enemy(100, 100, random.randint(2, 7), random.randint(-12, -8), -50 , H/random.randint(1, 4)))
                    random_number = random.randint(1, 100)
                    if random_number < 8:
                        present_group.add(Presents('Images/veryGoodPresent.png',200, 12, 100, 100, random.randint(100, WIN.get_width() - 100), random.randint(-150, -100)))
                    time -= 1
                
                if ticks % 20000 == 0:
                    empty_groups()
                    run = False
                    return score, "Tick tack tick tack you're fucked"
        
        # Check if cursor collides with good presents
        for present in present_group:
            if present.rect.colliderect(cursor.rect):
                score += present.value
                present_group.remove(present)
                point_group.add(Points(100, present.value, present.rect.centerx, present.rect.centery))
        
        # Check if cursor collides with bad present
        for enemy in enemy_group:
            if enemy.rect.colliderect(cursor.rect):
                empty_groups()
                run = False
                return score, 'I think santa put a bomb in the red present'
        
        WIN.blit(BG, (0, 0))
        
        # Update presents
        present_group.draw(WIN)
        present_group.update()
        enemy_group.draw(WIN)
        enemy_group.update()

        # Update texts
        # Update score
        score_text = font.render(f'score: {score}', True, (200, 0, 0))
        score_text_rect = score_text.get_rect(midleft = (W/1.6, H - 75 ))
        WIN.blit(score_text, score_text_rect)


        # Update timer
        time_text = font.render(f'time: {time}', True, (200, 0, 0))
        time_text_rect = time_text.get_rect(midleft = (60, H - 75))
        WIN.blit(time_text, time_text_rect)

        # Update points 
        point_group.draw(WIN)
        point_group.update()

        # Update cursor
        cursor.update()
        cursor.draw()

        pygame.display.update()
        clock.tick(FPS)


def main():
    highscore = 0
    game_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit() 
                events = game()
                game_count += 1
                score = events[0]
                deathType = events[1]
                if score > highscore:
                    highscore = score
        
        # Update texts

        # Start text
        WIN.fill((255, 255, 255)) #79c5e7
        WIN.blit(start_text, start_text_rect)
        # Highscore text
        higscore_text = font.render(f'Highscore: {highscore}', True, (0,0,0))
        higscore_text_rect = higscore_text.get_rect(center = (W/2, H/4))
        WIN.blit(higscore_text, higscore_text_rect)
        # Secret text
        WIN.blit(secret_text, secret_text_rect)
        # Type of death
        if game_count > 0:
            deathType_text = font2.render(deathType, True, (200,0,0))
            deathType_text_rect = deathType_text.get_rect(center = (W/2, H - H/4))
            WIN.blit(deathType_text, deathType_text_rect)

        pygame.display.update()
        clock.tick(FPS)


main()