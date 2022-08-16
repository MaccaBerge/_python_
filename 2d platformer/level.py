import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # Level setup
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level()
    
    def setup_level(self):
        for row_index,row in enumerate(LEVEL_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'X':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites])
                if col == 'P':
                    self.player = Player((x,y), [self.visible_sprites, self.active_sprites], self.collision_sprites)
                    start_possition = (x, y)

    def run(self):
        # Run the entire game
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100, 300)

        # Center camera setup
        #self.half_w = self.display_surface.get_size()[0] // 2
        #self.half_h = self.display_surface.get_size()[1] // 2

        # Camera
        cam_left = CAMERA_BOARDERS['left']
        cam_top = CAMERA_BOARDERS['top']
        cam_width = self.display_surface.get_size()[0] - (cam_left + CAMERA_BOARDERS['right'])
        cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_BOARDERS['bottom'])

        self.camera_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_height)
    
    def custom_draw(self, player):

        # Get the player offset
        #self.offset.x = player.rect.centerx - self.half_w
        #self.offset.y = player.rect.centery - self.half_h
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom
        

        # Camera offset
        self.offset = pygame.math.Vector2(
            self.camera_rect.left - CAMERA_BOARDERS['left'],
            self.camera_rect.top - CAMERA_BOARDERS['top'])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)