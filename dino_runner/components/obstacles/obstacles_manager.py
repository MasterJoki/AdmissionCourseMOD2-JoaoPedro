import pygame
from random import choice

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class ObstaclesManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            image_cactus = [SMALL_CACTUS, LARGE_CACTUS]
            cactus = Cactus(image_cactus)

            bird_images = BIRD
            bird = Bird(bird_images)

            obstacles = [bird, cactus]
            self.obstacles.append(choice(obstacles))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    if game.player.type == "shield":
                        self.obstacles.remove(obstacle)
                    elif obstacle.isBird:
                        self.obstacles.remove(obstacle)
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []