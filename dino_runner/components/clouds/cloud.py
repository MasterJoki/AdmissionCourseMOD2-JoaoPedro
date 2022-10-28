import pygame
from pygame.sprite import Sprite
from random import randint, choice
from dino_runner.utils.constants import SCREEN_WIDTH

class Cloud(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - randint(0, 50)
        self.rect.y = choice([100, 150, 200])

    def update(self, game_speed, cloudManager):
        self.rect.x -= game_speed * 0.75

        if self.rect.x < -self.rect.width:
            cloudManager.clouds.pop(0)
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))