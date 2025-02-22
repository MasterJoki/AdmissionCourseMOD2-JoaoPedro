from dino_runner.utils.constants import SHIELD, SHIELD_TYPE, SHIELD_INVERT
from dino_runner.components.power_ups.power_up import PowerUp

class Shield(PowerUp):
    def __init__(self):
        self.image = [SHIELD, SHIELD_INVERT]
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)