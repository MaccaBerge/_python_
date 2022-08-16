import pygame
import random
from sys import exit

pygame.init()
pygame.mixer.init()
W, H = 1300, 1200
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60

pygame.mixer.music.load('Musikk og lyd/music.ogg')
pygame.mixer.music.play(-1, 0.0, 10)


BG = pygame.transform.scale(pygame.image.load('Images/bg.webp').convert_alpha(), (W, H))

class Stars(pygame.sprite.Sprite):
    def __init__(self, speed, width, height, x, y):
        super().__init__()
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('Images/stars.png').convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def update(self):
        self.rect.y += self.speed

        if not self.rect.colliderect(WIN.get_rect()):
            star_group.remove(self)

class Player:
    def __init__(self, speed, width, height, x, y):
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('Images/superhero2.png').convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    def update(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.right < W:
            self.rect.x += self.speed
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left > 0: 
            self.rect.x -= self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_string, speed, width, height, x, y):
        super().__init__()
        self.image_string = image_string
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load(self.image_string).convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    def update(self):
        self.rect.y += self.speed

        if self.rect.top > H + 100:
            enemy_group.remove(self)

class Text():
    def __init__(self, font, text, size, color, x, y):
        self.text = text
        self.size = size
        self.big_size = int(self.size * 1.2)
        self.color = color
        self.x = x
        self.y = y
        self.font = pygame.font.Font(font, self.size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    def update(self):
        # Knapp blir feit
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.font = pygame.font.Font(font, self.big_size)
            self.image = self.font.render(self.text, True, self.color)
            self.rect = self.image.get_rect(center = (self.x, self.y))
        else:
            self.font = pygame.font.Font(font, self.size)
            self.image = self.font.render(self.text, True, self.color)
            self.rect = self.image.get_rect(center = (self.x, self.y))


# Groups
star_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Player
player = Player(20, 120, 160, W/2, H-(H/5))

# Fonts
font = 'Fonts/Organic Relief.ttf'

# Texts
play_text = Text(font, 'PLAY', 100, '#696969', W/2, H/2)
quit_text = Text(font, 'QUIT', 100, '#696969', W/2, H - (H/5))

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 100)

def remove_entities():
    star_group.empty()
    enemy_group.empty()

def progression_bar(seconds, size):
    delta_size = 300/seconds/60
    BG_RECT = pygame.Surface((310, 50))
    BG_RECT.fill('#696969')
    BG_RECT_RECT = BG_RECT.get_rect(midleft = (45, 50))
    WIN.blit(BG_RECT, BG_RECT_RECT)

    RECT = pygame.Surface((size, 40))
    RECT.fill((0,200,0))
    RECT_RECT = RECT.get_rect(midleft = (50, 50))
    WIN.blit(RECT, RECT_RECT)
    if size < 300:
        size += delta_size
        return size
    else:
        size = 0
        return size

def game():
    ticks = 0
    game_speed = 1
    bg_speed = 1
    spawning_time = 1
    level = 1
    size = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == timer:
                ticks += 100
                
                if ticks % 600 == 0:
                    star_group.add(Stars(7.5 * bg_speed, W, H, W/2, -H/2))
                
                # First lvl
                if ticks < 20000:
                    level = 1
                    if ticks % 2000 == 0:
                        enemy_group.add(Enemy('Images/slow_asteroid.webp',random.randint(3, 4) * game_speed, 151, 116, random.randint(50, W-50), -100))
                
                if ticks > 20000 and ticks < 40000:
                    level = 2
                    if ticks % 2000 == 0:
                        enemy_group.add(Enemy('Images/slow_asteroid.webp',random.randint(3, 4) * game_speed, 151, 116, random.randint(50, W-50), -100))
                    if ticks % 4000 == 0:
                        enemy_group.add(Enemy('Images/fast_asteroid.png',random.randint(5, 7) * game_speed, 151, 116, random.randint(50, W-50), -100))
                
                if ticks >= 40000:
                    if ticks % 20000 == 0:
                        game_speed += 0.25
                        bg_speed += 0.1
                        level += 1
                    if ticks % 1500 == 0:
                        enemy_group.add(Enemy('Images/slow_asteroid.webp',random.randint(4, 5) * game_speed, 151, 116, random.randint(50, W-50), -100))
                    if ticks % 3000 == 0:
                        enemy_group.add(Enemy('Images/fast_asteroid.png',random.randint(5, 7) * game_speed, 151, 116, random.randint(50, W-50), -100))
                    if ticks % 30000 == 0:
                        enemy_group.add(Enemy('Images/satelitt.png',1 * game_speed, 325, 337, random.randint(50, W-50), -100))
                
                if ticks >= 100000:
                    if ticks % 20000 == 0:
                        game_speed += 0.25
                        bg_speed += 0.1
                        level += 1
                    if ticks % 750 == 0:
                        enemy_group.add(Enemy('Images/slow_asteroid.webp',random.randint(4, 5) * game_speed, 151, 116, random.randint(50, W-50), -100))
                    if ticks % 2500 == 0:
                        enemy_group.add(Enemy('Images/fast_asteroid.png',random.randint(5, 7) * game_speed, 151, 116, random.randint(50, W-50), -100))
                    if ticks % 25000 == 0:
                        enemy_group.add(Enemy('Images/satelitt.png',1 * game_speed, 325, 337, random.randint(50, W-50), -100))


        WIN.blit(BG, (0,0))
        star_group.draw(WIN)
        star_group.update()
        enemy_group.draw(WIN)
        enemy_group.update()
        player.draw()
        player.update()
        size = progression_bar(20, size)

        level_text_font = pygame.font.Font('Fonts/Organic Relief.ttf', 20)
        level_text = level_text_font.render(f'LEVEL: {level}', True, '#696969')
        WIN.blit(level_text, (50, 110))

        for enemy in enemy_group:
            if player.mask.overlap(enemy.mask, (enemy.rect.topleft[0] - player.rect.left, enemy.rect.topleft[1] - player.rect.top)):
                remove_entities()
                run = False
                return level
        

        pygame.display.update()
        clock.tick(FPS)

def main():
    highscore = 0
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_text.rect.collidepoint(event.pos): 
                        score = game()
                        score -= 1
                        if score > highscore:
                            highscore = score

                    if quit_text.rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()
        
        WIN.blit(BG, (0,0))
        play_text.draw()
        play_text.update()
        quit_text.draw()
        quit_text.update()
        scoring_font = pygame.font.Font('Fonts/Organic Relief.ttf', 50)
        highscore_text = scoring_font.render(f'HIGHSCORE: {highscore}', True, '#696969')
        score_text = scoring_font.render(f'SCORE: {score}', True, '#696969')
        WIN.blit(highscore_text, (W/3, 100))
        WIN.blit(score_text, (W/3, 300))

        pygame.display.update()
        clock.tick(FPS)

main()