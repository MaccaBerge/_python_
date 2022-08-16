import pygame
from sys import exit

WIN = pygame.display.set_mode((1000, 800))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (500, 400))

player_gravity = 0

OBSTACLE_IMG = pygame.image.load('graphics/R.png').convert_alpha()

bg_surf = pygame.transform.scale(pygame.image.load('graphics/ground.png').convert(), (1000, 800))


class Obstacles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.obstacle_surf = OBSTACLE_IMG
        self.obstacle_rect = self.obstacle_surf.get_rect(topleft = (self.x, self.y))

    def draw(self, WIN):
        #WIN.blit(self.obstacle_surf, (self.x, self.y))
        WIN.blit(self.obstacle_surf, self.obstacle_rect)
    
    def collition(self):
         if player_rect.colliderect(self.obstacle_rect):
             player_rect.bottom = self.obstacle_rect.top


obstacle = Obstacles(250, 400)



pygame.init()
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()
            
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE and (player_rect.bottom >= 800 or player_rect.bottom == obstacle.obstacle_rect.top):
                   player_gravity = -30

    # Vis bakgrunn
    WIN.blit(bg_surf, (0, 0))

    # Vis obstacle
    obstacle.draw(WIN)

    # Player
    player_gravity += 1 
    player_rect.y += player_gravity

    # Mooving player right/left
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_d] and player_rect.right < 1000:
        player_rect.x   = 5


    if player_rect.bottom >= 800:
        player_rect.bottom = 800
    
    # Colides with obstacle
    obstacle.collition()
    
    WIN.blit(player_surf, player_rect)


    pygame.display.update()
    clock.tick(60)
    