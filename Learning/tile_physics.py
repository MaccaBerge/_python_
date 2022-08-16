import pygame, sys, random

W, H = 500, 500
WIN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 120

player = pygame.Rect(100, 100, 50, 80)
tiles = [pygame.Rect(200, 350, 50, 50), pygame.Rect(260, 350, 50, 50)]

def collision_test(rect, tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions

def move(rect, movement, tiles):
    rect.x += movement[0]
    collision = collision_test(rect, tiles)
    for tile in collision:
        if movement[0] > 0:
            rect.right = tile.left
        if movement[0] < 0:
            rect.left = tile.right
    rect.y += movement[1]
    collision = collision_test(rect, tiles)
    for tile in collision:
        if movement[1] > 0:
            rect.bottom = tile.top
        if movement[1] < 0:
            rect.top = tile.bottom
    return rect

right = False
left = False
up = False
down = False
        

while True:
    
    WIN.fill((0,0,0))

    movement = [0,0]
    if right == True:
        movement[0] += 5
    if left == True:
        movement[0] -= 5
    if up == True:
        movement[1] -= 5
    if down == True:
        movement[1] += 5
    
    player = move(player, movement, tiles)

    pygame.draw.rect(WIN, (255,255,255), player)

    for tile in tiles:
        pygame.draw.rect(WIN, (255,0,0), tile)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
    
    
    pygame.display.update()
    clock.tick(FPS)