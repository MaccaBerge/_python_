import pygame
from sys import exit

W, H = 1300, 1200
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60

size = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    WIN.fill((255,255,255))
    BG_RECT = pygame.Surface((310, 60))
    BG_RECT.fill('#696969')
    BG_RECT_RECT = BG_RECT.get_rect(midleft = (W/2 - 5, H/2))
    WIN.blit(BG_RECT, BG_RECT_RECT)

    RECT = pygame.Surface((size, 50))
    RECT.fill((0,200,0))
    RECT_RECT = RECT.get_rect(midleft = (W/2, H/2))
    WIN.blit(RECT, RECT_RECT)
    if size < 300:
        size += 1
    else:
        size = 0

        

    pygame.display.update()
    clock.tick(FPS)

