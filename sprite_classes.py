import random
import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
#from game import (SCREEN_HEIGHT, SCREEN_WIDTH)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((60,23))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center = (50,int(SCREEN_HEIGHT/2))
        )

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -6)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 6)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-6, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(6, 0)
 

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:   
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite): 
    
    def __init__(self):
        super().__init__()
        self.surf =pygame.Surface((20,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center =(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()

class Powerup(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20,10))
        self.value = random.randint(100,255)
        self.surf.fill((0,0,self.value))
        self.rect = self.surf.get_rect(
            center =(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5,20)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()

class Laser(pygame.sprite.Sprite):

    def __init__(self, loc1, loc2):
        super().__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center=(loc1,loc2))

    def update(self): 
        self.rect.move_ip(10,0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()