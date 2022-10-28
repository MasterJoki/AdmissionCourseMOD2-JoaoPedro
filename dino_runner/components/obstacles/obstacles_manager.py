from email.policy import default
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
                    if game.player.type == "shield" or obstacle.isBird:
                        self.obstacles.remove(obstacle)
                        self.desative_power_up(game.player)
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        self.desative_power_up(game.player)
                        break
                
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
        self.desative_power_up()
    
    def desative_power_up(self, player):
        player.shield = False
        player.has_power_up = False
        player.type = "default"
        player.power_up_time = 0