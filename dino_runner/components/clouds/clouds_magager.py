from dino_runner.components.clouds.cloud import Cloud
from dino_runner.utils.constants import CLOUD

class CloudManager:
    def __init__(self):
        self.clouds = []
    
    def update(self, game_speed):
        if len(self.clouds) == 0:
            self.clouds.append(Cloud(CLOUD))

        for cloud in self.clouds:
            cloud.update(game_speed, self)

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)

    def reset(self):
        self.clouds = []