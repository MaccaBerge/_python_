import pygame
from sys import exit
import random

pygame.init()
W, H = 1500, 800
WIN = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
FPS = 60

class Clouds(pygame.sprite.Sprite):
    def __init__(self, speed, width, height, x, y):
        super().__init__()
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.spawnCloud = True
        self.image = pygame.transform.scale(pygame.image.load('Images/sky.jpg').convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(midleft = (self.x, self.y))
    
    def update(self):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            cloud_group.remove(self)
        
        if self.rect.right < W + 10 and self.spawnCloud == True:
            cloud_group.add(Clouds(3, W, H, W, H/2))
            self.spawnCloud = False

class Text:
    def __init__(self, font_string, text, size, color, x, y):
        self.font_string = font_string
        self.text = text
        self.size = size
        self.only_size = size
        self.color = color
        self.x = x
        self.y = y
        self.font = pygame.font.Font(self.font_string, self.size)
        self.surf = self.font.render(self.text, True, self.color)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    
    def draw(self):
        WIN.blit(self.surf, self.rect)
    
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.font = pygame.font.Font(self.font_string, int(self.size * 1.2))
            self.surf = self.font.render(self.text, True, self.color)
            self.rect = self.surf.get_rect(center = (self.x, self.y))
        else:
            self.font = pygame.font.Font(self.font_string, self.only_size)
            self.surf = self.font.render(self.text, True, self.color)
            self.rect = self.surf.get_rect(center = (self.x, self.y))


class Player:
    def __init__(self, speed, width, height, x, y):
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('Images/plane.png').convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    def update(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.rect.top > 0:
            self.rect.y -= self.speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.rect.bottom < H:
            self.rect.y += self.speed
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.rect.left > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.rect.right < W:
            self.rect.x += self.speed
    
    def reset_pos(self):
        self.rect = self.image.get_rect(center = (self.x, self.y))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, width, height, x, y):
        super().__init__()
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('Images/missile.png').convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(midleft = (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        self.rect.x -= self.speed

        if self.rect.right < -self.speed:
            enemy_group.remove(self)

# Groups
cloud_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Objects
player = Player(6, 1660//5.5, 624//5.5, 200, H/2)
cloud_group.add(Clouds(3, W, H, W, H/2))

# Font 
font = pygame.font.Font('Fonts/SuperMario256.ttf', 100)

play_text = Text('Fonts/SuperMario256.ttf', 'PLAY', 100, (0,0,0), W/2, H/1.5)
quit_text = Text('Fonts/SuperMario256.ttf', 'QUIT', 100, (0,0,0), W/2, H-100)

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 100)

def game():
    score = 0
    ticks = 0
    game_speed = 2400
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == timer:
                ticks += 100

                # Spawning enemies
                if ticks % game_speed == 0:
                    enemy_group.add(Enemy(10, 2120//10, 900//10, W + 10, random.randint(50, H - 50)))
                
                if ticks % 15000 == 0 and game_speed > 300:
                    game_speed -= 200

        WIN.fill((142,219,250))

        # Updating clouds
        cloud_group.draw(WIN)
        cloud_group.update()

        # Updating enemies
        enemy_group.draw(WIN)
        enemy_group.update()

        # Updating player
        player.draw()
        player.update()

        # Updating text
        score_text = font.render(f'SCORE: {score}', True, (0,0,0))
        score_rect = score_text.get_rect(center = (W/2, 60))
        WIN.blit(score_text, score_rect)

        # Checking for collisions
        for enemy in enemy_group:
            if player.mask.overlap(enemy.mask, (enemy.rect.topleft[0] - player.rect.left, enemy.rect.topleft[1] - player.rect.top)):
                enemy_group.empty()
                player.reset_pos()
                run = False
                return score
            if enemy.rect.right <= 0:
                score += 10


        pygame.display.update()
        clock.tick(FPS)


def main():
    highscore = 0
    score = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_text.rect.collidepoint(event.pos):
                        score = game()
                        if score > highscore:
                            highscore = score
                    if quit_text.rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

        WIN.fill((144, 220, 250))

        # Update clouds
        cloud_group.draw(WIN)
        cloud_group.update()

        # Update text
        play_text.draw()
        play_text.update()
        quit_text.draw()
        quit_text.update()

        highscore_text = font.render(f'HIGHSCORE: {highscore}', True, (0,0,0))
        highscore_rect = highscore_text.get_rect(center = (W/2, 100))
        WIN.blit(highscore_text, highscore_rect)

        score_text = font.render(f'SCORE: {score}', True, (0,0,0))
        score_rect = score_text.get_rect(center = (W/2, 200))
        WIN.blit(score_text, score_rect)

        pygame.display.update()
        clock.tick(FPS)

main()