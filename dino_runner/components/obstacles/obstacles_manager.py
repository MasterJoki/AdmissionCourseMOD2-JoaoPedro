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
            random_cactu = randint(0, 1)
            cactus = Cactus(image_cactus[random_cactu])

            bird = Bird(BIRD)

            obstacles_possibilities = [cactus, bird]
            random_obstacles = randint(0,1)

            self.obstacles.append(obstacles_possibilities[random_obstacles])
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)