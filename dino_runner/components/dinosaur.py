import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import *

pygame.init()
pygame.mixer.init()

DUCK_IMG = {
    DEFAULT_TYPE: [DUCKING, DUCKING_INVERT], 
    SHIELD_TYPE: [DUCKING_SHIELD, DUCKING_SHIELD_INVERT], 
    HAMMER_TYPE: [DUCKING_HAMMER, DUCKING_HAMMER_INVERT]
}

JUMP_IMG = {
    DEFAULT_TYPE: [JUMPING, JUMPING_INVERT], 
    SHIELD_TYPE: [JUMPING_SHIELD, JUMPING_SHIELD_INVERT], 
    HAMMER_TYPE: [JUMPING_HAMMER, JUMPING_HAMMER_INVERT]
}

RUN_IMG = {
    DEFAULT_TYPE: [RUNNING, RUNNING_INVERT], 
    SHIELD_TYPE: [RUNNING_SHIELD, RUNNING_SHIELD_INVERT], 
    HAMMER_TYPE: [RUNNING_HAMMER, RUNNING_HAMMER_INVERT]
}

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_jump = False
        self.dino_run = True
        self.dino_duck = False
        self.jump_vel = JUMP_VEL
        self.position = 0
        self.setup_state()
        self.sound_jump = pygame.mixer.Sound("dino_runner/assets/sons/jump_sound.wav")
        self.sound_jump.set_volume(1)

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, user_input, isDark):
        if isDark:
            self.position = 1
        else:
            self.position = 0

        if self. dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()
        elif self.dino_run:
            self.run()

        if self.step_index >= 9:
            self.step_index = 0

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE] or user_input[pygame.K_w]) and not self.dino_jump and not self.dino_duck:
            self.dino_jump = True
            self.dino_run = False
            self.sound_jump.play()
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
        
        if (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and not self.dino_duck and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True

    def run(self):
        self.image = RUN_IMG[self.type][self.position][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type][self.position]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.position][self.step_index // 5]
        self.dino_rect.y = Y_POS + 37
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))