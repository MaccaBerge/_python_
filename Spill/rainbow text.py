import pygame

W, H = 800, 600

display = pygame.Surface((W, H))
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('colored_text')
clock = pygame.time.Clock()
score = 0

black = (0, 0, 0)
white = (255, 255, 255)

col_spd = 1

def_col = [[120, 120, 240]]
col_dir = [[-1, 1, 1]]
#texts = [f'{score}']

minimum = 0
maximum = 255


def draw_text(text, size, col, x, y):
    font = 'font/Pixeltype.ttf'
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def col_change(col, dir):
    for i in range(3):
        col[i] += col_spd * dir[i]
        if col[i] >= maximum or col[i] <= minimum:
            dir[i] *= -1

def array_func(col, dir, size, x, y):
    for i in range(len(col)):
        draw_text(f'{score}', size, col[i], x, y + i * 50)
        col_change(col[i], dir[i])

pygame.init()

run = True 

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(black)
    array_func(def_col, col_dir, 100, W / 2, 200)
    score += 1


    
    clock.tick()

    display.blit(screen, (0, 0))
    pygame.display.update()

