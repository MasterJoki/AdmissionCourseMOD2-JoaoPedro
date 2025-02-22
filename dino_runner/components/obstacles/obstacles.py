import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacles(Sprite):
    def __init__(self, image, type, isBird=False):
        self.image = image
        self.type = type
        self.position = 0
        self.rect = self.image[0][self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0
        self.isBird = isBird
        self.imageBird = self.image

    def update(self, game_speed, obstacles, isDark):
        if isDark:
            self.position = 1
        else:
            self.position = 0
        
        if self.isBird:
            self.updateBird()
        
        self.rect.x -= game_speed 

        if self.rect.x < -self.rect.width:
            obstacles.pop()
    
    def updateBird(self):
        if self.step_index >= 12:
            self.step_index = 0

        self.imageBird = self.image[self.position][0] if self.step_index < 6 else self.image[self.position][1]
        self.step_index += 1

    def draw(self, screen: pygame.Surface):
        if self.isBird:
            return self.drawBird(screen)
        
        screen.blit(self.image[self.position][self.type], (self.rect.x, self.rect.y))

    def drawBird(self, screen: pygame.Surface):
        screen.blit(self.imageBird, (self.rect.x, self.rect.y))