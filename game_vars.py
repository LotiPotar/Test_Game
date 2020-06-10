import pygame

pygame.font.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', False, pygame.color.Color('White'))
title_text = pygame.font.SysFont('Consolas', 32).render('Test_game V.1', False, pygame.color.Color('White'))
prompt_text = pygame.font.SysFont('Consolas', 32).render('Press a key to proceed', False, pygame.color.Color('White'))
gameover_text = pygame.font.SysFont('Consolas', 32).render('Game Over' , False, pygame.color.Color('White'))