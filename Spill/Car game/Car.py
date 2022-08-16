import pygame
import os

WIDTH, HEIGHT = 1500, 1200
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car game')

# importere bil
CAR = pygame.transform.scale(pygame.image.load(os.path.join('bilder', 'race-car-top-down-clipart-19.png')), (363, 184))
CAR = pygame.transform.rotate(CAR, -90)

# importere bakgrunn
BG = pygame.transform.scale(pygame.image.load(os.path.join('bilder', 'R (1).png')), (WIDTH, HEIGHT))

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.car_img = None
        
    def draw(self, window):
        window.blit(self.car_img, (self.x, self.y))


class Player(Car):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.car_img = CAR
        self.mask = pygame.mask.from_surface(self.car_img)
        self.car_img_rect = self.car_img.get_rect(center = (182, 92))

    def rotate_car(self, angle):
        rotated_surface = pygame.transform.rotozoom(self.car_img, angle, 1)
        player = rotated_surface

        rotated_rect = rotated_surface.get_rect(center = (750, 600))
        self.car_img_rect = rotated_rect

        return player, self.car_img

        



def main():

    run = True
    FPS = 60
    
    player = Player(652, 419)

    angle = 0

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        
        player.draw(WIN) 


        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.y -= 10
        if keys[pygame.K_s]:
            player.y += 10
        if keys[pygame.K_a]:
            player.x -= 10
        if keys[pygame.K_d]:
            angle -= 5
            Player.rotate_car(player, angle)

            #player.x += 10
        


main()