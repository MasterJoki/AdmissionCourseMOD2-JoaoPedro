import random
from dino_runner.components.obstacles.obstacles import Obstacles

class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        self.size = random.randint(0, 1)
        super().__init__(image[self.size], self.type)
        self.rect.y = self.verify()
    
    def verify(self):
        if self.size == 0:
            return 325
        else:
            return 300
