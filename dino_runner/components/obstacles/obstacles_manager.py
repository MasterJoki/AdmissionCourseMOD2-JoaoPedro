import pygame
from random import randint
from dino_runner.components import obstacles
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstaclesManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            image_cactus = [SMALL_CACTUS, LARGE_CACTUS]
            cactus = Cactus(image_cactus)

            bird = Bird(BIRD)

            obstacles_possibilities = [cactus, bird, cactus]
            random_obstacles = randint(0,2)

            self.obstacles.append(obstacles_possibilities[random_obstacles])
        
        for obstacle in self.obstacles:
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
            
            obstacle.update(game.game_speed, self.obstacles)
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)