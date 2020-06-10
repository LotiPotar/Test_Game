import random
import pygame
import time
from game_vars import (SCREEN_WIDTH,SCREEN_HEIGHT, pause_text, title_text, prompt_text, gameover_text)
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT, K_ESCAPE, K_SPACE, K_p, K_r, K_RETURN, RLEACCEL)
from sprite_classes import (Player,Enemy,Laser,Powerup)

#Imported the required modules

#Initialize the score, pygame module, font module, create a font, set the clock and create a screen for the game.
SCORE = 0
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("Calibri", 25)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Creating the custom events.
ADDENEMY = pygame.USEREVENT +1
pygame.time.set_timer(ADDENEMY,250)

ADDPOWERUP = pygame.USEREVENT + 2
pygame.time.set_timer(ADDPOWERUP,1000)

#Initializing the player
player = Player()

#Grouping the sprites into type groups and all_sprites group
enemies = pygame.sprite.Group()
lasers = pygame.sprite.Group()
powerups = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#Set the running variable to False, because we want to start with a prompt to start, and also set the state variables which are used to pause and unpause
running = False
PAUSE, UNPAUSE = 0,1
state = UNPAUSE

#fill the screen with black
screen.fill((0,0,0))

#Prompt the player to press 'Enter' to start the game
while not running:
    screen.blit(title_text,(200,100))
    screen.blit(prompt_text,(200,150))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                running = True
    pygame.display.flip()

#Main game loop
while running:
    #Rendering the current score
    text_surface = myfont.render(str(int(SCORE/120)), False, (255,255,255))

    #Listening to events (if the player wants to quit, or wants to shoot etc., new enemy or powerup shows up)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_p:
                state = PAUSE
            elif event.key == K_r:
                state = UNPAUSE
            elif event.key == K_SPACE:
                new_laser = Laser(player.rect.left,player.rect.top)
                lasers.add(new_laser)
                all_sprites.add(new_laser)
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY and state == UNPAUSE:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDPOWERUP and state == UNPAUSE:
            new_powerup = Powerup()
            powerups.add(new_powerup)
            all_sprites.add(new_powerup)
    #If the game is not paused do this:
    if state == UNPAUSE:
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        for group in (lasers,powerups,enemies):
            group.update()
        screen.fill((0,0,0))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        #Checking for collisions, if player hits enemy the main loop quits
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False
        if pygame.sprite.groupcollide(lasers, enemies, True, True):
            SCORE += 10000
        if pygame.sprite.spritecollide(player,powerups, True):
            SCORE += 60000

        SCORE += 60
        screen.blit(player.surf, player.rect)
        screen.blit(text_surface,(int(SCREEN_WIDTH/2),20))
    
    #if the game is paused do this:
    elif state == PAUSE:
        screen.blit(pause_text,(100,100))
    
    #Set the clock and update the display
    pygame.display.flip()   
    clock.tick(30)

#Player hit an enemy so the game ends, prompting the player to press any key to quit
end_game = True
score_text = pygame.font.SysFont('Consolas', 32).render('Your Score was:' + str(int(SCORE/120)) , False, pygame.color.Color('White'))
while end_game:
    screen.blit(gameover_text,(200,100))
    screen.blit(score_text,(200,150))
    screen.blit(prompt_text,(200,200))
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            end_game = False
            print("Your final score was: " + str(int(SCORE/120)))
    pygame.display.flip()
