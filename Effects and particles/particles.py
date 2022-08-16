import pygame, sys, random

W, H = 1200, 800
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 120

particles = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    WIN.fill((0,0,0))

    particles.append([[pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 14)])

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(WIN, (255 ,255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)
    
    
    pygame.display.update()
    clock.tick(FPS)