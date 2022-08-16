import math
import pygame
from sys import exit
import random


cursor_group = pygame.sprite.Group()
class Cursor(pygame.sprite.Sprite):
    def __init__(self, image, width, height, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.x = WIN.get_width() // x
        self.y = WIN.get_height() //  y
        self.only_x = x
        self.only_y = y
        self.image = pygame.transform.scale(image, (WIN.get_width() // self.width, WIN.get_width() // self.height))
        self.only_image = image
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def draw(self):
        WIN.blit(self.image, self.rect)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    
    def reset(self):
        # Reseting the size and possition after the screensize has been changed
        self.x = WIN.get_width() // self.only_x
        self.y = WIN.get_height() // self.only_y
        self.image = pygame.transform.scale(self.only_image, (WIN.get_width() // self.width, WIN.get_width() // self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))


button_group = pygame.sprite.Group()
class Buttons(pygame.sprite.Sprite):
    def __init__(self, image_string, shade_string, width, height, x, y):
        super().__init__()
        self.image_string = image_string
        self.shade_string = shade_string
        self.x = WIN.get_width() // x
        self.y = WIN.get_height() // y
        self.only_x = x
        self.only_y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image_string, (WIN.get_width() // self.width, WIN.get_width() // self.height))
        self.original_image = pygame.transform.scale(self.image_string, (WIN.get_width() // self.width, WIN.get_width() // self.height))
        self.only_image = self.image_string
        self.shade = pygame.transform.scale(shade_string, (WIN.get_width() // self.width, WIN.get_width() // self.height))
        self.only_shade = shade_string
        self.rect = self.image.get_rect(center = (self.x, self.y))
        button_group.add(self)

    def update(self):
        WIN.blit(self.image, self.rect)
    
    def hoverColor(self):
        self.image = self.shade
    
    def normalColor(self):
       self.image = self.original_image
    
    def hoverSize(self):
        if self.rect.colliderect(cursor.rect):
            self.image = pygame.transform.scale(self.image_string, ((WIN.get_width() // self.width) * 1.2, (WIN.get_width() // self.height) * 1.2))
            self.rect = self.image.get_rect(center = (self.x, self.y))
        else:
            self.image = pygame.transform.scale(self.image_string, (WIN.get_width() // self.width, WIN.get_width() // self.height))
            self.shade = pygame.transform.scale(self.shade_string, ((WIN.get_width() // self.width) * 1.2, (WIN.get_width() // self.height) * 1.2))
            self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def reset(self):
        # Reseting the size and possition after the screensize has been changed
        self.x = WIN.get_width() // self.only_x
        self.y = WIN.get_height() // self.only_y
        self.image = pygame.transform.scale(self.only_image, (WIN.get_width() // self.width, WIN.get_width() // self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.original_image = pygame.transform.scale(self.only_image, (WIN.get_width() // self.width, WIN.get_width() // self.height))
        self.shade = pygame.transform.scale(self.only_shade, (WIN.get_width() // self.width, WIN.get_width() // self.height))

text_group = pygame.sprite.Group()
class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, hoverColor, font, x, y,minimum = 120, maximum = 200, color_spd = [1, 1, 1], color_dir = [1, 1, 1], def_color = [255, 159, 69]):
        super().__init__()
        self.text = text
        self.size = WIN.get_width() // size
        self.only_size = size
        self.color = color
        self.hoverColor = hoverColor
        self.font_type = font
        self.font = pygame.font.Font(self.font_type, self.size)
        self.x = WIN.get_width() // x
        self.y = WIN.get_height() // y
        self.onlyx = x
        self.onlyy = y
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        text_group.add(self)
        
        self.color_spd = color_spd
        self.color_dir = color_dir
        self.def_color = def_color

        self.maximum = maximum
        self.minimum = minimum
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    # Drawing the text onto the screen
    def draw_text_multicolor(self):
        text_surface = self.font.render(self.text, True, self.def_color)
        text_rect = text_surface.get_rect(midleft = (self.x - (self.rect.center[0] - self.rect.left), self.y))
        WIN.blit(text_surface, text_rect)
    
    # Drawing the timer onto the screen
    def draw_timer_multicolor(self):
        template_timer_image = self.font.render('0.000', True, self.color)
        template_timer_rect = template_timer_image.get_rect(center = (self.x, self.y))
        
        timer_surface = self.font.render(self.text, True, self.def_color)
        timer_rect = timer_surface.get_rect(midleft = (self.x - (template_timer_rect.center[0] - template_timer_rect.left), self.y))
        WIN.blit(timer_surface, timer_rect)
    
    # Making the color of the text change
    def multicolor_change(self):
        for i in range(3):
            self.def_color[i] += self.color_spd[i] * self.color_dir[i]
            
            if self.def_color[i] >= self.maximum:
                self.color_spd[i] *= -1
                
            elif self.def_color[i] <= self.minimum:
                self.color_spd[i] *= -1
            
            if self.def_color[i] > 255:
                self.def_color[i] = 255
    
    def touch(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.font = pygame.font.Font(self.font_type, int(self.size * 1.1))
            self.image = self.font.render(self.text, True, self.hoverColor)
            self.rect = self.image.get_rect(center = (self.x, self.y))
        else:
            self.font = pygame.font.Font(self.font_type, self.size)
            self.image = self.font.render(self.text, True, self.color)
            self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def update(self, highscore):
        self.text = f'Highscore: {highscore}'
    
    def reset(self):
        # Reseting the size and possition after the screensize has been changed
        self.x = WIN.get_width() // self.onlyx
        self.y = WIN.get_height() // self.onlyy
        self.size = WIN.get_width() // self.only_size
        self.font = pygame.font.Font(self.font_type, self.size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center = (self.x, self.y))

game_group = pygame.sprite.Group()
class Games(pygame.sprite.Sprite):
    def __init__(self, image, speed, width, height, hoverSize, x, y):
        super().__init__()
        self.image_string = image
        self.speed = speed
        self.width = WIN.get_width() // width
        self.height = WIN.get_height() // height
        self.only_width = width
        self.only_height = height
        self.hoverSize = hoverSize
        self.x = WIN.get_width() // x
        self.y = WIN.get_height() // y
        self.onlyx = x
        self.onlyy = y
        self.image = pygame.transform.scale(pygame.image.load(self.image_string).convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.originalImage = self.image
        self.originalRect = self.rect
        self.hoverSurface = pygame.transform.scale(pygame.image.load(self.image_string).convert_alpha(), (self.width * self.hoverSize, self.height * self.hoverSize))
        self.allowUpdate = True
    
    def draw(self):
        WIN.blit(self.image, self.rect)
    
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.hoverSurface
            self.rect = self.image.get_rect(center = (self.x, self.y))
        elif not self.rect.collidepoint(pygame.mouse.get_pos()) and self.allowUpdate:
            self.image = self.originalImage
            self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def scrollUp(self):
        self.y += self.speed

    def scrollDown(self):
        self.y -= self.speed
            
    def reset(self):
        # Reseting the size and possition after the screensize has been changed
        self.x = WIN.get_width() // self.onlyx
        self.y = WIN.get_height() // self.onlyy
        self.originalImage = pygame.transform.scale(pygame.image.load(self.image_string).convert_alpha(), (WIN.get_width() // self.only_width, WIN.get_height() // self.only_height))
        self.image = pygame.transform.scale(pygame.image.load(self.image_string).convert_alpha(), (WIN.get_width() // self.only_width, WIN.get_height() // self.only_height))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.hoverSurface = pygame.transform.scale(pygame.image.load(self.image_string).convert_alpha(), (WIN.get_width() // self.only_width * self.hoverSize, WIN.get_height() // self.only_height * self.hoverSize))

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((WIN.get_width() / 45, WIN.get_width() / 200))
        self.image.fill(('#ffb300'))
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def update(self):
        self.rect.x += WIN.get_width() / 123

        if self.rect.x >= (WIN.get_width() + 200):
            self.kill()
    
    def reset(self):
        # Reseting the size and possition after the screensize has been changed
        self.image = pygame.Surface((WIN.get_width() / 45, WIN.get_width() / 200))
        self.image.fill(('#ffb300'))
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
# Gun class
class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Images/gun.png').convert_alpha(), (WIN.get_width() / 8, WIN.get_height() / 7))
        self.rect = self.image.get_rect(center = (WIN.get_width() / 2, WIN.get_height() /2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        BULLET_SOUND.play()
        #return Bullet(pygame.mouse.get_pos()[0] + WIN.get_height() / 8, pygame.mouse.get_pos()[1] - WIN.get_height() / 70) # (Fun gun)
        return Bullet(pygame.mouse.get_pos()[0] + WIN.get_height() / 15, pygame.mouse.get_pos()[1] - WIN.get_height() / 19) #(pistol)
        
    def reset(self):
        
        self.image = pygame.transform.scale(pygame.image.load('Images/gun.png').convert_alpha(), (WIN.get_width() / 8, WIN.get_height() / 7))
        self.rect = self.image.get_rect(center = (WIN.get_width() / 2, WIN.get_height() /2))

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x1, x2, y1, y2):
        super().__init__()
        self.x = random.randint(WIN.get_width() // x1, WIN.get_width() // x2)
        self.y = random.randint(WIN.get_height() // y1, WIN.get_height() // y2)
        self.onlyx = (x1, x2)
        self.onlyy = (y1, y2)
        self.image = pygame.Surface((WIN.get_width() / 23, WIN.get_width() / 23))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def update(self):
        if pygame.sprite.groupcollide(enemy_group, bullet_group, True, True):
            BOX_DESTROID.play()
    
    def reset(self):
        # Reseting the size and possition after the screensize has been changed
        self.image = pygame.Surface((WIN.get_width() / 23, WIN.get_width() / 23))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center = (random.randint(WIN.get_width() // self.onlyx[0], WIN.get_width() // self.onlyx[1]), random.randint(WIN.get_height() // self.onlyy[0], WIN.get_height() // self.onlyy[1])))

# General functions

# Check for hover-collision between cursor and mouse
def hover_check():
    for button in button_group:
        if button.rect.colliderect(cursor.rect):
            button.hoverColor()
        else:
            button.normalColor()


# When in a game, you should be able to pull this menu up and leave the game.
def pause_menu():
    
    pause_menu_text = Text('PAUSE MENU', 20, (255, 255, 255), (255, 255, 255), font2, 2, 10.5)
    
    global run
    pause_menu_run = True

    while pause_menu_run:
        
        WIN.fill((255, 255, 255))

        # Update sprites

        # Buttons
        settings_button.update()
        resume_button.update()
        leave_button.update()

        WIN.blit(GREEN_BG_BUTTON, (0, 0))
        pause_menu_text.draw()
        #pause_menu_text.touch()

        # Check for mouse hover-collision over button
        hover_check()

        # Cursor
        cursor_group.draw(WIN)
        cursor_group.update()
    
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for click on play_button
                if resume_button.rect.colliderect(cursor.rect):
                    BUTTON_CLICK.play()
                    pause_menu_run = False
                    
                # Check for click on settings button
                elif settings_button.rect.colliderect(cursor.rect):
                    BUTTON_CLICK.play()
                    settings()
                
                # Check for click on leave_button
                elif leave_button.rect.colliderect(cursor.rect):
                    BUTTON_CLICK.play()
                    run = False
                    pause_menu_run = False
                    return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu_run = False

# The menu where you can choose wich game to play
def game_menu():
    game_menu_text = Text('GAME MENU', 20, (255, 255, 255), (255, 255, 255), font2, 2, 10.5)
    
    run = True
    while run:

        WIN.fill((255, 255, 255))

        # Updating game images
        gunGame.draw()
        gunGame.update()
        circleShooter.draw()
        circleShooter.update()

        # Updating buttons
        WIN.blit(GREEN_BG_BUTTON, (0, 0))
        arrow1_button.update()
        arrow1_button.hoverSize()
        arrow2_button.update()
        arrow2_button.hoverSize()
        arrow3_button.update()
        arrow3_button.hoverSize()
        
        game_menu_text.draw()
        #game_menu_text.touch()

        # Loading cursor
        cursor_group.draw(WIN)
        cursor_group.update()

        # Looping through the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if circleShooter.rect.colliderect(cursor.rect):
                        BUTTON_CLICK.play()
                        CircleShooter()
                    if gunGame.rect.colliderect(cursor.rect):
                        BUTTON_CLICK.play()
                        gun_game_start()
                    
                    if arrow1_button.rect.colliderect(cursor.rect):
                        BUTTON_CLICK.play()
                        run = False
                
                if event.button == 5 and circleShooter.rect.bottom > WIN.get_height() // 1.05:
                    gunGame.scrollDown()
                    circleShooter.scrollDown()

                if event.button == 4 and gunGame.rect.top < WIN.get_height() // 4.4:
                    gunGame.scrollUp()
                    circleShooter.scrollUp()
                
                if arrow2_button.rect.colliderect(cursor.rect) and gunGame.rect.top < WIN.get_height() // 4.4:
                    BUTTON_CLICK.play()
                    gunGame.scrollUp()
                    circleShooter.scrollUp()

                if arrow3_button.rect.colliderect(cursor.rect) and circleShooter.rect.bottom > WIN.get_height() // 1.05:
                    BUTTON_CLICK.play()
                    gunGame.scrollDown()
                    circleShooter.scrollDown()

        pygame.display.update()
        clock.tick(FPS)


# Game functions

# Settings
def settings():
    # Importing global variables to the function
    global current_screensize
    global WIN
    global GREEN_BG_BUTTON

    # Skjermen - [FULLSCREEN], [Bredden:2560, Høyden er:1440], [Bredden:1920, Høyden er:1080], [Bredden:1600, Høyden er:900], [Bredden:1280, Høyden er:720]
    settings_menu_text = Text('SETTINGS', 20, (255, 255, 255), (255, 255, 255), font2, 2, 10.5)

    screensizes = ['1280 x 720', '1600 x 900', '1920 x 1080', '2560 x 1440', 'FULLSCREEN']
    screensizes_current_index = current_screensize
    screensize = screensizes[screensizes_current_index]

    settings_run = True

    while settings_run:
        WIN.fill((255, 255, 255))

        # Drawing the menu text onto the screen
        WIN.blit(GREEN_BG_BUTTON, (0, 0))
        settings_menu_text.draw()
        #settings_menu_text.touch()

        # Drawing all the buttons and button bg's
        hover_check()
        bg_button.update()
        screensize_bg.update()
        left_button.update()
        right_button.update()
        apply_button.update()
        arrow1_button.hoverSize()
        arrow1_button.update()
        
        # Drawing the text 
        screensizes_text = pygame.font.Font(font2, (WIN.get_width() // 20)).render(screensizes[screensizes_current_index], True, '#9F9F9F')
        screensizes_text_rect = screensizes_text.get_rect(center = (bg_button.rect.center))
        screensize_text = pygame.font.Font(font2, (WIN.get_width() // 20)).render('SCREEN SIZE', True, '#9F9F9F')
        screensize_text_rect = screensize_text.get_rect(center = (WIN.get_width() // 2, WIN.get_height() // 3.5))

        WIN.blit(screensizes_text, screensizes_text_rect)
        WIN.blit(screensize_text, screensize_text_rect)

        cursor_group.draw(WIN)
        cursor_group.update()

        # Looping through the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow1_button.rect.colliderect(cursor.rect):
                        BUTTON_CLICK.play()
                        settings_run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left_button.rect.colliderect(cursor.rect) and event.button == 1 and screensizes_current_index > 0:
                    BUTTON_CLICK.play()
                    screensizes_current_index -= 1
                
                elif right_button.rect.colliderect(cursor.rect) and event.button == 1 and screensizes_current_index < 4:
                    BUTTON_CLICK.play()
                    screensizes_current_index += 1
                
                elif bg_button.rect.colliderect(cursor.rect) and right_button.rect.colliderect(cursor.rect) == False and left_button.rect.colliderect(cursor.rect) == False and event.button == 4 and screensizes_current_index < 4:
                    BUTTON_CLICK.play()
                    screensizes_current_index += 1
                
                elif bg_button.rect.colliderect(cursor.rect) and right_button.rect.colliderect(cursor.rect) == False and left_button.rect.colliderect(cursor.rect) == False and event.button == 5 and screensizes_current_index > 0:
                    BUTTON_CLICK.play()
                    screensizes_current_index -= 1
                
                elif apply_button.rect.colliderect(cursor.rect) and event.button == 1:
                    # Changing the size of the screen
                    BUTTON_CLICK.play()
                    screensize = screensizes[screensizes_current_index]
                    current_screensize = screensizes_current_index

                    if screensize == '1280 x 720':
                        WIN = pygame.display.set_mode((1280, 720))
 
                    if screensize == '1600 x 900':
                        WIN = pygame.display.set_mode((1600, 900))
  
                    if screensize == '1920 x 1080':
                        WIN = pygame.display.set_mode((1920, 1080))

                    if screensize == '2560 x 1440':
                        WIN = pygame.display.set_mode((2560, 1440))

                    if screensize == 'FULLSCREEN':
                        WIN = pygame.display.set_mode((2560, 1440), pygame.FULLSCREEN)
                    
                    for button in button_group:
                        button.reset()
                    
                    # Resetting sizes and possitions of items on the screen
                    GREEN_BG_BUTTON = pygame.Surface((WIN.get_width(), WIN.get_height() // 5))
                    GREEN_BG_BUTTON.fill('#15d798')
                    settings_menu_text = Text('SETTINGS', 20, (255, 255, 255), (255, 255, 255), font2, 2, 10.5)
                    cursor.reset()
                    crosshair.reset()
                    for text in text_group:
                        text.reset()
                    gunGame.reset()
                    circleShooter.reset()
                    gun.reset()
                    for enemy in enemy_group:
                        enemy.reset()
                    for bullet in bullet_group:
                        bullet.reset()
                    
                    
        pygame.display.update()
        clock.tick(FPS)

# gun_game start/end screen
def gun_game_start():
    # importing global variables to function
    global start_time
    global run
    global highscore

    # Making text
    game_name = Text('QUICK SHOOTER', 15, ('#a9a9a9'), ('#a9a9a9'), font1, 2, 8)
    play_text = Text('Play', 20, (255, 159, 69), (235, 159, 69), font1, 2, 3.059)
    highscore_text = Text(f'Heighscore: {highscore}', 20, (255, 159, 69), (235, 159, 69), font1, 2, 1.73)
    leave_text = Text('Leave', 20, (255, 159, 69), (235, 159, 69), font1, 2, 1.21)
    run = True

    while run:

        WIN.fill((255, 255, 255))

        # Drawing information onto the screen
        game_name.draw()
        play_text.draw()
        play_text.touch()
        highscore_text.update(highscore)
        highscore_text.draw()
        highscore_text.touch()
        leave_text.draw()
        leave_text.touch()
        cursor_group.draw(WIN)
        cursor_group.update()

        # Looping through the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                   pause_menu()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Click on play button
                    if play_text.rect.collidepoint(event.pos):
                        start_time = pygame.time.get_ticks()
                        BUTTON_CLICK.play()
                        gun_game()
                        pygame.mouse.set_pos(highscore_text.rect.center)
                        enemy_group.empty()
                        run = True
                    
                    elif leave_text.rect.collidepoint(event.pos):
                        BUTTON_CLICK.play()
                        run = False

        pygame.display.update()
        clock.tick(FPS) 

        

# Gun Game
#################################################################################
highscore = 100

def gun_game():

    # Enemy (sprite)
    number_enemy = 10
    for i in range(number_enemy):
        enemy_group.add(Enemy(6.15, 1.09, 6.7, 1.18))
    
    pygame.mouse.set_pos(WIN.get_width() / 15, WIN.get_height() / 2)
    display_time = Text(str((0) / 1000), 20, '#FF9F45', '#FF9F45', font1, 2, 17)

    global start_time
    global run
    global highscore
    
    while run:

        # BG color
        WIN.fill((255, 255, 255))

        # Timer
        cur_time = pygame.time.get_ticks()
        
        # Load bullets
        bullet_group.draw(WIN)
        bullet_group.update()

        # Load enemies
        enemy_group.draw(WIN)
        enemy_group.update()

        # Load player
        player_group.draw(WIN)
        player_group.update()

        # Update buttons
        escape_button.update()

        display_time.text = str((cur_time - start_time) / 1000)
        display_time.draw_timer_multicolor()
        display_time.multicolor_change()

        # End Game
        if len(enemy_group) == 0:
            timeUsed = cur_time - start_time
            if timeUsed / 1000 < highscore:
                highscore = timeUsed / 1000
            
            bullet_group.empty()
            run = False
        
        # Update display and fps
        pygame.display.update()
        clock.tick(FPS)

        # Checking for events in the pygame event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullet_group.add(gun.create_bullet())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cur_mouse_pos = pygame.mouse.get_pos()
                    cur_time = pygame.time.get_ticks()
                    pause_menu()
                    end_time = pygame.time.get_ticks()
                    # Making sure the timer is as much as before the pause_menu was ran
                    start_time += (end_time - cur_time)
                    pygame.mouse.set_pos(cur_mouse_pos)

#################################################################################
# Circle Shooter
def CircleShooter():

    class Player(pygame.sprite.Sprite):
        # Player color = rgb(255, 172, 51)
        def __init__(self, x, y, health = 300, maximum_health = 300):
            super().__init__()
            self. x = WIN.get_width() // x
            self.y = WIN.get_height() // y
            self.onlyx = x
            self.onlyy = y
            self.image = pygame.transform.scale(pygame.image.load('Shapes/playerCircle.png').convert_alpha(), (WIN.get_width() / 22, WIN.get_width() / 22))
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.mask = pygame.mask.from_surface(self.image)
            self.health = health
            self.maximum_health = maximum_health
            self.current_health = self.health
            self.maximum_health = self.maximum_health
            self.health_bar_lenght = WIN.get_width() / 44
            self.health_ratio = self.maximum_health / self.health_bar_lenght
        
        def draw(self):
            WIN.blit(self.image, self.rect)

        def update(self):
            self.basic_health()

            # Moving up, down, left and right
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= WIN.get_width() / 220
            if keys[pygame.K_s] and self.rect.bottom < WIN.get_height():
                self.rect.y += WIN.get_width() / 220
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= WIN.get_width() / 220
            if keys[pygame.K_d] and player.rect.right < WIN.get_width():
                self.rect.x += WIN.get_width() / 220
        
        def get_damage(self, amount):
            if self.current_health > 0:
                self.current_health -= amount
            if self.current_health <= 0:
                self.current_health = 0
        
        def get_health(self, amount):
            if self.current_health < self.maximum_health:
                self.current_health += amount
            if self.current_health >= self.maximum_health:
                self.current_health = self.maximum_health
        
        def basic_health(self):
            pygame.draw.rect(WIN, (255, 0, 0), (self.rect.centerx - self.health_bar_lenght/2, self.rect.midtop[1] - WIN.get_width()/73, self.health_bar_lenght, WIN.get_width()/88))
            pygame.draw.rect(WIN, (0, 255, 0), (self.rect.centerx - self.health_bar_lenght/2, self.rect.midtop[1] - WIN.get_width()/73, self.current_health / self.health_ratio, WIN.get_width()/88))
            pygame.draw.rect(WIN, (0, 0, 0), (self.rect.centerx - self.health_bar_lenght/2, self.rect.midtop[1] - WIN.get_width()/73, self.health_bar_lenght, WIN.get_width()/88), WIN.get_width() // 640)

        def create_bullet(self):
                bullet_group.add(Bullet(self.rect.centerx, self.rect.centery, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        
        def reset(self):
            self.image = pygame.transform.scale(pygame.image.load('Shapes/playerCircle.png').convert_alpha(), (WIN.get_width() / 22, WIN.get_width() / 22))
            self.rect = self.image.get_rect(center = (WIN.get_width() // self.onlyx, WIN.get_height() // self.onlyy))
            self.mask = pygame.mask.from_surface(self.image)
            self.current_health = self.health
            self.maximum_health = self.maximum_health
            self.health_bar_lenght = WIN.get_width() / 44
            self.health_ratio = self.maximum_health / self.health_bar_lenght


    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y, targetx, targety):
            super().__init__()
            self.x = x
            self.y = y
            self.image = pygame.transform.scale(pygame.image.load('Shapes/playerCircle.png').convert_alpha(), (WIN.get_width() / 44, WIN.get_width() / 44))
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.mask = pygame.mask.from_surface(self.image)
            self.angle = math.atan2(targety - self.y, targetx - self.x)
            self.dx = math.cos(self.angle) * WIN.get_width() / 147
            self.dy = math.sin(self.angle) * WIN.get_width() / 147
        
        def update(self):
            self.x += self.dx
            self.y += self.dy
            self.rect.centerx = int(self.x)
            self.rect.centery = int(self.y)
            
            if not self.rect.colliderect(WIN.get_rect()):
                self.kill()
        
        def reset(self):
            self.image = pygame.transform.scale(pygame.image.load('Shapes/playerCircle.png').convert_alpha(), (WIN.get_width() / 44, WIN.get_width() / 44))
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.mask = pygame.mask.from_surface(self.image)


    class Triangle(pygame.sprite.Sprite):
        def __init__(self, size, speed, x, y, health = 400, maximum_health = 400):
            super().__init__()
            self.size = (WIN.get_width() // size[0], WIN.get_width() // size[1])
            self.only_size = size
            self.speed = speed 
            self.x = x
            self.y = y
            self.chooseImage = random.choice(('Shapes/blueTriangle.png', 'Shapes/greenTriangle.png'))
            self.image = pygame.transform.scale(pygame.image.load(self.chooseImage), (self.size))
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.health = health
            self.maximum_health = maximum_health
            self.current_health = self.health
            self.maximum_health = self.maximum_health
            self.health_bar_lenght = WIN.get_width() / 44
            self.health_ratio = self.maximum_health / self.health_bar_lenght
            enemy_group.add(self)

        def update(self):
            self.basic_health()
            targetx = player.rect.centerx
            targety = player.rect.centery
            self.angle = math.atan2(targety - self.rect.centery, targetx - self.rect.centerx)
            self.dx = math.cos(self.angle) * (WIN.get_width() // self.speed)
            self.dy = math.sin(self.angle) * (WIN.get_width() // self.speed)

            self.x += self.dx
            self.y += self.dy
            self.rect.centerx = int(self.x)
            self.rect.centery = int(self.y)

        def bulletCollision(self):
            if self.current_health <= 200:
                self.remove(triangle_group, enemy_group)
                game_state.score += 1
            else:
                self.get_damage(200)
        
        def get_damage(self, amount):
            if self.current_health > 0:
                self.current_health -= amount
            if self.current_health <= 0:
                self.current_health = 0
        
        def get_health(self, amount):
            if self.current_health < self.maximum_health:
                self.current_health += amount
            if self.current_health >= self.maximum_health:
                self.current_health = self.maximum_health
        
        def basic_health(self):
            pygame.draw.rect(WIN, (255, 0, 0), (self.rect.centerx - self.health_bar_lenght/2, self.rect.center[1], self.health_bar_lenght, WIN.get_width()/88))
            pygame.draw.rect(WIN, (0, 255, 0), (self.rect.centerx - self.health_bar_lenght/2, self.rect.center[1], self.current_health / self.health_ratio, WIN.get_width()/88))
            pygame.draw.rect(WIN, (0, 0, 0), (self.rect.centerx - self.health_bar_lenght/2, self.rect.center[1], self.health_bar_lenght, WIN.get_width()/88), WIN.get_width() // 640)
        
        def reset(self):
            self.image = pygame.transform.scale(pygame.image.load(self.chooseImage), (WIN.get_width() // self.only_size[0], WIN.get_width() // self.only_size[1]))
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.current_health = self.health
            self.maximum_health = self.maximum_health
            self.health_bar_lenght = WIN.get_width() / 44
            self.health_ratio = self.maximum_health / self.health_bar_lenght

    class GameState:
        global circleShooterScore
        global circleShooterHighscore
        def __init__(self):
            self.state = 'game_menu'
            self.score = circleShooterScore
            self.highscore = circleShooterHighscore
        
        def game_menu(self):
            global run
            player.rect.center = (player.x, player.y)
            run = True
            while run:
                # Screen color
                WIN.fill((255, 255, 255))

                # Updating text
                play_text.draw()
                play_text.touch()
                leave_text.draw()
                leave_text.touch()

                # Score
                score_font = pygame.font.Font('Fonts/HaveFun.ttf', WIN.get_width() // 13)
                score_text = score_font.render(f'SCORE: {self.score}', True, (0,0,0))
                score_text_rect = score_text.get_rect(center = (WIN.get_width() // 2, WIN.get_height() // 6))
                WIN.blit(score_text, score_text_rect)

                # Highscore 
                highscore_text = score_font.render(f'HIGHSCORE: {self.highscore}', True, (0,0,0))
                highscore_text_rect = highscore_text.get_rect(center = (WIN.get_width() // 2, WIN.get_height() // 15))
                WIN.blit(highscore_text, highscore_text_rect)

                # Updating the cursor
                cursor_group.draw(WIN)
                cursor_group.update()

                # Looping through the events each frame
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            quit = pause_menu()
                            if quit == True:
                                self.state = 'game_done'
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            # Checking for click on play button
                            if play_text.rect.collidepoint(event.pos):
                                self.state = 'main_game'
                                run = False
                            # Checking for click on leave button
                            if leave_text.rect.collidepoint(event.pos):
                                self.state = 'game_done'
                                run = False

                pygame.display.update()
                clock.tick(FPS)
        
        def main_game(self):
            global run
            timer_ticks = 0
            game_state.score = 0
            timer = pygame.USEREVENT + 1
            pygame.time.set_timer(timer, 100)
            run = True
            while run:
                # Screen color
                WIN.fill((255, 255, 255))

                # Update escape button
                escape_button.update()

                # Updating sprites
                triangle_group.draw(WIN)
                triangle_group.update()
                bullet_group.draw(WIN)
                bullet_group.update()
                player.draw()
                player.update()
                
                # Check for collision between player and enemy
                if pygame.sprite.spritecollide(player, enemy_group, False):
                    player.get_damage(2)
                    if player.current_health <= 0:
                        enemy_group.empty()
                        triangle_group.empty()
                        player.get_health(300)
                        if self.score > self.highscore:
                            self.highscore = self.score
                        self.state = 'game_menu'
                        run = False
                
                # Check if bullet collides with triangle
                for triangle in triangle_group:
                    triangle.update()
                    if pygame.sprite.spritecollide(triangle, bullet_group, True):
                        triangle.bulletCollision()
                
                # Updating the cursor
                crosshair.draw()
                crosshair.update()

                # Updating text 
                score_font = pygame.font.Font('Fonts/HaveFun.ttf', WIN.get_width() // 20)
                score_text = score_font.render(f'SCORE: {self.score}', True, (0,0,0))
                score_text_rect = score_text.get_rect(center = (WIN.get_width() // 2, WIN.get_height() // 20))
                WIN.blit(score_text, score_text_rect)
                
                # looping through the events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            quit = pause_menu()
                            player.reset()
                            for triangle in triangle_group:
                                triangle.reset()
                            for bullet in bullet_group:
                                bullet.reset()
                            if quit == True:
                                self.state = 'game_menu'
                                triangle_group.empty()
                                enemy_group.empty()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player.create_bullet()
                    
                    if event.type == timer:
                        timer_ticks += 1
                        # Every second second (2s)
                        if timer_ticks % 5 == 0 and len(triangle_group) < 10:
                            triangle_group.add(Triangle((20, 23), 1000, random.randint(0, W), random.randint(0, H)))

                pygame.display.update()
                clock.tick(FPS)

        def wave_one(self):
            pass

        def state_manager(self):
            if self.state == 'game_menu':
                self.game_menu()
            if self.state == 'main_game':
                self.main_game()

    game_state = GameState()
    ###############################################################################################################

    # Font
    font_string = 'Fonts/HaveFun.ttf'
    font = pygame.font.Font(font_string, 100)

    # Texts
    play_text = Text('PLAY', 10, (0,0,0), (64,64,64), font_string, 2, 1.6)
    leave_text = Text('LEAVE', 10, (0,0,0), (64,64,64), font_string, 2, 1.2)

    # Objects
    player = Player(2, 2)

    # Groups
    bullet_group = pygame.sprite.Group()
    triangle_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    global circleShooterHighscore
    global circleShooterScore

    run = True
    while run:
        game_state.state_manager()
        if game_state.state == 'game_done':
            circleShooterHighscore = game_state.highscore
            circleShooterScore = game_state.score
            run = False

        clock.tick(FPS)




# Game setup
pygame.init()
clock = pygame.time.Clock()
W, H = 2560, 1440
WIN = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
FPS = 120
run = True
pygame.mouse.set_visible(False)
#pygame.event.set_grab(True)
current_screensize = 4

# Font
font1 = 'Fonts/zorque.otf'
font2 = 'Fonts/opensans-bold.ttf'

# Sounds
BULLET_SOUND = pygame.mixer.Sound('Audio/laser.mp3')
BOX_DESTROID = pygame.mixer.Sound('Audio/boxsound.wav')
BUTTON_CLICK = pygame.mixer.Sound('Audio/buttonclick.mp3')
SETTINGS_BUTTON_CLICK = pygame.mixer.Sound('Audio/button_click_settings.wav')


# Follow mouse
CURSOR = pygame.image.load('Images/cursor.png').convert_alpha()
cursor = Cursor(CURSOR, 60, 40, 2, 2)
cursor_group.add(cursor)

CROSSHAIR = pygame.image.load('Images/crosshair.png').convert_alpha()
crosshair = Cursor(CROSSHAIR, 50, 50, 2, 2)

# Gun (sprite)
gun = Gun()
player_group = pygame.sprite.Group()
player_group.add(gun)

# Bullet (sprite)
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()


# Buttons (surf), Button color (light) = #15d798, Button color (dark) = #25AB80
SETTINGS_BUTTON = pygame.image.load('Buttons/SETTINGS_button_light.png').convert_alpha()
SETTINGS_BUTTON_DARK = pygame.image.load('Buttons/SETTINGS_button_dark.png').convert_alpha()
settings_button = Buttons(SETTINGS_BUTTON, SETTINGS_BUTTON_DARK, 7.6, 26, 2, 1.7)

QUIT_BUTTON = pygame.image.load('Buttons/QUIT_button_light.png').convert_alpha()
QUIT_BUTTON_DARK = pygame.image.load('Buttons/QUIT_button_dark.png').convert_alpha()
quit_button = Buttons(QUIT_BUTTON, QUIT_BUTTON_DARK, 11, 26, 2, 1.15)

PLAY_BUTTON = pygame.image.load('Buttons/PLAY_button_light.png').convert_alpha()
PLAY_BUTTON_DARK = pygame.image.load('Buttons/PLAY_button_dark.png').convert_alpha()
play_button = Buttons(PLAY_BUTTON, PLAY_BUTTON_DARK, 11, 26, 2, 3.2)

RESUME_BUTTON = pygame.image.load('Buttons/RESUME_button_light.png').convert_alpha()
RESUME_BUTTON_DARK = pygame.image.load('Buttons/RESUME_button_dark.png').convert_alpha()
resume_button = Buttons(RESUME_BUTTON, RESUME_BUTTON_DARK, 7.6, 26, 2, 3.2)

LEAVE_BUTTON = pygame.image.load('Buttons/LEAVE_button_light.png').convert_alpha()
LEAVE_BUTTON_DARK = pygame.image.load('Buttons/LEAVE_button_dark.png').convert_alpha()
leave_button = Buttons(LEAVE_BUTTON, LEAVE_BUTTON_DARK, 9.3, 26, 2, 1.15)

BG_BUTTON = pygame.image.load('Images/BG_button_light.png').convert_alpha()
bg_button = Buttons(BG_BUTTON, BG_BUTTON, 1.8, 14.2, 2, 2.3)

GREEN_BG_BUTTON = pygame.Surface((WIN.get_width(), WIN.get_height() // 5))
GREEN_BG_BUTTON.fill('#15d798')

SCREENSIZE_BG = pygame.image.load('Images/BG_button_settings2.png').convert_alpha()
screensize_bg = Buttons(SCREENSIZE_BG, SCREENSIZE_BG, 2.56, 14.2, 2, 3.5)

LEFT_BUTTON = pygame.image.load('Buttons/LEFT_button_light.png').convert_alpha()
LEFT_BUTTON_DARK = pygame.image.load('Buttons/LEFT_button_dark.png').convert_alpha()
left_button = Buttons(LEFT_BUTTON, LEFT_BUTTON_DARK, 10.3, 14.2, 3.68, 2.3)

RIGHT_BUTTON = pygame.image.load('Buttons/RIGHT_button_light.png').convert_alpha()
RIGHT_BUTTON_DARK = pygame.image.load('Buttons/RIGHT_button_dark.png').convert_alpha()
right_button = Buttons(RIGHT_BUTTON, RIGHT_BUTTON_DARK, 10.3, 14.2, 1.35, 2.3)

APPLY_BUTTON = pygame.image.load('Buttons/APPLY_button_light.png').convert_alpha()
APPLY_BUTTON_DARK = pygame.image.load('Buttons/APPLY_button_dark.png').convert_alpha()
apply_button = Buttons(APPLY_BUTTON, APPLY_BUTTON_DARK, 5, 14.2, 2, 1.7)

ARROW1_BUTTON = pygame.transform.rotate(pygame.image.load('Buttons/arrow3.png').convert_alpha(), 90)
arrow1_button = Buttons(ARROW1_BUTTON, ARROW1_BUTTON, 10, 15, 12, 10)

ARROW2_BUTTON = pygame.transform.rotate(pygame.image.load('Buttons/arrow2.png').convert_alpha(), 0)
arrow2_button = Buttons(ARROW2_BUTTON, ARROW2_BUTTON, 12, 12, 1.15, 2)

ARROW3_BUTTON = pygame.transform.rotate(pygame.image.load('Buttons/arrow2.png').convert_alpha(), 180)
arrow3_button = Buttons(ARROW3_BUTTON, ARROW3_BUTTON, 12, 12, 1.15, 1.4)

ESCAPE_BUTTON = pygame.image.load('Buttons/ESCAPE_button.webp').convert_alpha()
escape_button = Buttons(ESCAPE_BUTTON, ESCAPE_BUTTON, 20, 20, 35, 20)

# Game images
GUN_GAME = 'Images/gunGameBoarder.png'
gunGame = Games(GUN_GAME, 60, 2, 2, 1.1, 2, 2)

CIRCLE_SHOOTER = 'Images/CircleShooterImage.png'
circleShooter = Games(CIRCLE_SHOOTER, 60, 2, 2, 1.1, 2, 0.9)

global circleShooterScore
global circleShooterHighscore

circleShooterScore = 0
circleShooterHighscore = 0

def main():
    main_menu_text = Text('MAIN MENU', 20, (255, 255, 255), (255, 255, 255), font2, 2, 10.5)

    while True:

        # BG color
        WIN.fill((255, 255, 255))

        # Check for mouse hover-collision over button
        hover_check()

        # Update sprites

        # Blit buttons on to screen
        play_button.update()
        settings_button.update()
        quit_button.update()

        WIN.blit(GREEN_BG_BUTTON, (0, 0))
        main_menu_text.draw()
        #main_menu_text.touch()
        
        # Draw the cursor on to the screen
        cursor_group.draw(WIN)
        cursor_group.update()


        # Update display and fps
        pygame.display.update()
        clock.tick(FPS)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # Check for mouse button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                # Check for click on play_button
                    if play_button.rect.colliderect(cursor.rect):
                        BUTTON_CLICK.play()
                        game_menu()
                    
                    elif settings_button.rect.colliderect(cursor.rect):
                        BUTTON_CLICK.play()
                        settings()
                    
                    # Check for click on quit_button
                    elif quit_button.rect.colliderect(cursor.rect):
                        BUTTON_CLICK.play()
                        pygame.quit()
                        exit()


main()