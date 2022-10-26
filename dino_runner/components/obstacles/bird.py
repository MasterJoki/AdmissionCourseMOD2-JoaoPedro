from dino_runner.components.obstacles.obstacles import Obstacles

class Bird(Obstacles):
    def __init__(self, image):
        self.image = image
        super().__init__(self.image, 0, True)
    