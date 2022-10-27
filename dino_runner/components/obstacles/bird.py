from dino_runner.components.obstacles.obstacles import Obstacles
from random import randint, choice

class Bird(Obstacles):
    def __init__(self, image):
        self.type = randint(0, 1)
        super().__init__(image, self.type, True)
        self.rect.y = choice([230, 275, 320])
    