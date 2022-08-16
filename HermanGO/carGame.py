# Importerer moduler (ekstrapakker)
import pygame
from sys import exit
import random

# Aktiverer funksjoner i pygame
pygame.init()
pygame.mixer.init()

# Oprett en skjerm
W, H = 1200, 800
WIN = pygame.display.set_mode((W, H))

# Oprett en klokke og FPS
clock = pygame.time.Clock()
FPS = 60

# Spill musikk
pygame.mixer.music.load('Music and sound/Chiptronical.ogg')
pygame.mixer.music.play(-1, 0.0, 4)

class Backround(pygame.sprite.Sprite):
    def __init__(self, image_string, speed, x, y):
        # Importerer funksjoner fra pygame.sprite.Sprite
        super().__init__()
        # Objektene sine atributter (egenskaper)
        self.image_string = image_string
        self.speed = speed
        self.x = x
        self.y = y
        self.spawn_state = True
        # Lager et bilde for objektet
        self.image = pygame.transform.scale(pygame.image.load(self.image_string).convert_alpha(), (W, H))
        # Hitbox
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
    
    # Methodes (klassefunksjoner)
    def draw(self):
        # Tegner objektets bilde på skjermen
        WIN.blit(self.image, self.rect)
    
    def update(self):
        # Bevegelse og utplasering av et annet objekt
        self.rect.y += self.speed
        if self.rect.top > -100 and self.spawn_state == True:
            bg_group.add(Backround('Images/highway.png', 10, W/2, self.rect.top))
            self.spawn_state = False

class Text:
    def __init__(self, font_string, text, size, color, x, y):
        # Objektenes atributter (egenskaper)
        self.font_string = font_string
        self.text = text
        self.size = size
        self.only_size = size
        self.color = color
        self.x = x
        self.y = y
        # Lager tekst og hitbox
        self.font = pygame.font.Font(self.font_string, self.size)
        self.surf = self.font.render(self.text, True, self.color)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    
    def draw(self):
        # Tegner objektets bilde på skjermen
        WIN.blit(self.surf, self.rect)
    
    def update(self, value = None):
        # Uthever teksten hvis musa er over teksten
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.font = pygame.font.Font(self.font_string, int(self.size * 1.2))
            self.surf = self.font.render(self.text, True, self.color)
            self.rect = self.surf.get_rect(center = (self.x, self.y))
        # Uthever ikke hvis musa er over teksten
        else:
            self.font = pygame.font.Font(self.font_string, self.only_size)
            self.surf = self.font.render(self.text, True, self.color)
            self.rect = self.surf.get_rect(center = (self.x, self.y))


class Player: 
    def __init__(self, width, height, color, x, y):
        # Atributtene til obektet (egenskaper)
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Images/playerCar.png').convert_alpha(), (self.width, self.height)), -90) 
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def draw(self):
        # Tegner objektets bilde på skjermen
        WIN.blit(self.image, self.rect)
    
    def update(self):
        # Bevegelse etter trykk på tastatur
        keys = pygame.key.get_pressed()
        
        # Hvis knapp a blir trykket - beveg spiller 10 pixler til venstre
        if keys[pygame.K_a] and player.rect.left > 200:
            self.rect.x -= 10
        # Hvis knapp d blir trykket - beveg spiller 10 pixler til høyre
        if keys[pygame.K_d] and player.rect.right < W - 190:
            self.rect.x += 10

class Enemys(pygame.sprite.Sprite):
    def __init__(self, image_string, speed, width, height, color, x, y):
        # Importerer funksjoner fra pygame.sprite.Sprite
        super().__init__()
        # Objektenes atributter (egenskaper)
        self.image_string = image_string
        self.speed = speed
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        # Lager bilde og hitbox
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.image_string).convert_alpha(), (self.width, self.height)), 90) # 256 × 127
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def update(self):
        # Bevegelse nedover på skjermen med self.speed pixler hver frame
        self.rect.y += self.speed
        # Sletting av objektet når det er utenfor skjermen 
        if self.rect.top > H + self.speed:
            enemy_group.remove(self)

# Fonter
font = 'Fonts/MilkyNice-Clean.ttf'
font1 = pygame.font.Font('Fonts/MilkyNice-Clean.ttf', 100)

# Tekst objekter
play_button = Text(font, 'PLAY', 100, (0,0,0), W/2, H/1.7)
quit_button = Text(font, 'QUIT', 100, (0,0,0), W/2, H/1.2)

# Bakgrunn gruppe + objekt
bg_group = pygame.sprite.Group()
bg_group.add(Backround('Images/highway.png', 10, W/2, H))
bg_blur = Backround('Images/highway_blur.jpg', 0, W/2, H)

# Fiende gruppe + objekt
enemy_group = pygame.sprite.Group()
player = Player(3265 // 17, 1656 // 17, (0,0,0), W/2, H - 120)

# Fiende timer (hvor ofte skal fiendene spawne)
obstacles_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacles_timer, 1000) # 1000 står for antall millisekunder

# Spillet (funksjon)
def game():
    score = 0
    run = True
    # Spillets evige loop
    while run:
        # Går gjennom event loopen hver frame og sjekker for eventer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # Spawner fiender hvert 1000 millisekund
            if event.type == obstacles_timer:
                enemy_group.add(Enemys(random.choice(('Images/enemyCar3.png', 'Images/enemyCar2.png')), 5, 256 / 1.2, 127 / 1.2, (0,0,0), random.choice((330, 510, 695, 875)), -100))
        
        # Kollisjon mellom fiende og spiller
        for enemy in enemy_group:
            if enemy.rect.colliderect(player.rect):
                enemy_group.empty()
                return score
            
            # Adderer score med 10 hvis fiende har passert bunnen av skjermen 
            if enemy.rect.top > H:
                score += 10
        
        # Tegne bakgrunnen
        bg_group.draw(WIN)
        bg_group.update()

        # Tegn spilleren
        player.draw()
        player.update()
        
        # Tegne fiender
        enemy_group.draw(WIN)
        enemy_group.update()
        
        # Oppdatterer tekst (score)
        score_text = font1.render(f'SCORE: {score}', True, (0,0,0))
        score_rect = score_text.get_rect(midleft = (W/3.1, 60))
        WIN.blit(score_text, score_rect)
        
        # Oppdaterer skjermen med FPS
        pygame.display.update()
        clock.tick(FPS)

# Hovedemeny (Funksjon)
def main():
    score = 0
    highscore = 0
    run = True
    # Hovedmenyens evige loop
    while run:
        # Går gjennom event loopen hver frame og sjekker for eventer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Sjekker etter museklikk
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Kollisjon med play knappen (starter spillet)
                if play_button.rect.collidepoint(event.pos):
                    score = game()
                    if score > highscore:
                        highscore = score
                # Kollisjon med quit knappen (lukker programmet og vinduet)
                if quit_button.rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
        
        # Tegner bakgrunnen
        bg_blur.draw()

        # Oppdater all teksten
        play_button.draw()
        play_button.update()
        quit_button.draw()
        quit_button.update()
        highscore_text = font1.render(f'HIGHSCORE: {highscore}', True, (0,0,0))
        highscore_rect = highscore_text.get_rect(center = (W/2, 100))
        WIN.blit(highscore_text, highscore_rect)
        score_text = font1.render(f'SCORE: {score}', True, (0,0,0))
        score_rect = score_text.get_rect(center = (W/2, 220))
        WIN.blit(score_text, score_rect)
        
        # Oppdaterer skjermen og FPS
        pygame.display.update()
        clock.tick(FPS)

# Kjører hovedmenyen 
main()