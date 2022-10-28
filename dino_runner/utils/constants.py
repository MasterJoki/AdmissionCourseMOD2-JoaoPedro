from asyncio import shield
import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]
RUNNING_INVERT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]
RUNNING_SHIELD_INVERT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer.png")),
]
RUNNING_HAMMER_INVERT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoRun2Hammer.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_INVERT = pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoJump.png"))

JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_SHIELD_INVERT = pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoJumpShield.png"))

JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_HAMMER_INVERT = pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]
DUCKING_INVERT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]
DUCKING_SHIELD_INVERT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]
DUCKING_HAMMER_INVERT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/InvertDinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
SMALL_CACTUS_INVERT = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/InvertSmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/InvertSmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/InvertSmallCactus3.png")),
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]
LARGE_CACTUS_INVERT = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/InvertLargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/InvertLargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/InvertLargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]
BIRD_INVERT = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/InvertBird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/InvertBird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
CLOUD_INVERT = pygame.image.load(os.path.join(IMG_DIR, 'Other/InvertCloud.png'))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
SHIELD_INVERT = pygame.image.load(os.path.join(IMG_DIR, 'Other/Invertshield.png'))

HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
HAMMER_INVERT = pygame.image.load(os.path.join(IMG_DIR, 'Other/Inverthammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_INVERT = pygame.image.load(os.path.join(IMG_DIR, 'Other/InvertTrack.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))
RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))
DEAD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDead.png'))

FONT_STYLE = "freesansbold.ttf"

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

INVERTED_TYPE = "invert"
NORMAL_TYPE = "normal"