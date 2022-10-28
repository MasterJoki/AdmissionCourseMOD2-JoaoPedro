from dino_runner.components.clouds.cloud import Cloud
from dino_runner.utils.constants import CLOUD, CLOUD_INVERT

class CloudManager:
    def __init__(self):
        self.clouds = []
        self.position = 0
        self.image = [CLOUD, CLOUD_INVERT]
    
    def update(self, game_speed, isDark):
        if isDark:
            self.position = 1
        else:
            self.position = 0

        if len(self.clouds) == 0:
            self.clouds.append(Cloud(self.image[self.position]))

        for cloud in self.clouds:
            cloud.update(game_speed, self)

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)

    def reset(self):
        self.clouds = []