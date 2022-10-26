import random
from dino_runner.components.obstacles.obstacles import Obstacles

class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, random.randint(0, 2))
        self.rect.y = 325
