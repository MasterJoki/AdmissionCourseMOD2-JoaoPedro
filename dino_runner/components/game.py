from ssl import VerifyMode
from tkinter import NORMAL
import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, BG_INVERT, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, GAME_OVER, RESET, RUNNING, RUNNING_INVERT, DEAD, DEFAULT_TYPE, NORMAL_TYPE, INVERTED_TYPE
from dino_runner.components.obstacles.obstacles_manager import ObstaclesManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.clouds.clouds_magager import CloudManager

pygame.init()
pygame.mixer.init()

HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.highScore = 0
        self.death_count = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        self.cloud_manager = CloudManager()
        self.power_up_manager = PowerUpManager()

        #Ala psiquiátrica
        self.isDark = False
        self.type = NORMAL_TYPE
        self.bgDicio = {NORMAL_TYPE: BG, INVERTED_TYPE: BG_INVERT}
        self.fillDicio = {NORMAL_TYPE: (255, 255, 255), INVERTED_TYPE: (0, 0, 0)}

        #Ala psiquiátrica 2
        self.score_sound = pygame.mixer.Sound("dino_runner/assets/sons/score_sound.wav")
        self.score_sound.set_volume(1)

    def verifyType(self):
        if self.isDark:
            return INVERTED_TYPE
        else:
            return NORMAL_TYPE

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.resetGame()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.isDark = False

    def resetGame(self):
        self.obstacle_manager.reset_obstacles(self.player)
        self.power_up_manager.reset_power_ups()
        self.cloud_manager.reset()
        self.score = 0
        self.game_speed = 20

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.obstacle_manager.update(self)
        self.cloud_manager.update(self.game_speed, self.isDark)
        self.player.update(user_input, self.isDark)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player, self.isDark)

    def update_score(self):
        self.score += 0.5

        if self.highScore < self.score:
            self.highScore = self.score

        if self.score % 100 == 0 and self.game_speed <= 46:
            self.game_speed += 2
            self.score_sound.play()
        
        if not self.isDark:
            if self.score % 300 == 0:
                self.isDark = True
        else:
            if self.score % 300 == 0:
                self.isDark = False

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(self.fillDicio[self.verifyType()]) #Também aceita código hexadecimal "#FFFFFF"
        self.draw_background()
        self.obstacle_manager.draw(self.screen)
        self.cloud_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = self.bgDicio[self.verifyType()]
        image_width = image.get_width()

        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (image_width + self.x_pos_bg, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(image, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed
    
    def draw_score(self):
        self.text_format((f"Score: {round(self.score)}"), (1000, 50))
        self.text_format((f"HighScore: {round(self.highScore)}"), (1000, 85))
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.text_format(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds.", (500, 40), 18)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()
            
    def text_format(self, textReceived, position, fontSize=22, font=FONT_STYLE):
        if self.isDark:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        
        font = pygame.font.Font(font, fontSize)
        text = font.render(textReceived, True, color)        
        text_rect = text.get_rect()
        text_rect.center = position
        self.screen.blit(text, text_rect)

    def image_format(self, imageReceived, position):
        image = imageReceived
        image_rect = image.get_rect()
        image_rect.center = position
        self.screen.blit(image, image_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))

        if self.death_count == 0:
            self.show_start()
        else:
            self.show_death()

        pygame.display.update()
        self.handle_events_on_menu()

    def show_start(self):
        self.screen.blit(RUNNING[0], (HALF_SCREEN_WIDTH - 40, HALF_SCREEN_HEIGHT - 120))
        self.text_format("Press any Key to Start", (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT))
    
    def show_death(self):
        self.screen.blit(DEAD, (HALF_SCREEN_WIDTH - 40, HALF_SCREEN_HEIGHT - 170))
        self.image_format(GAME_OVER, (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT - 40))
        self.text_format("Press any Key to Restart", (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT))
        self.image_format(RESET, (HALF_SCREEN_WIDTH - 5, HALF_SCREEN_HEIGHT + 80))
        self.text_format((f"Score: {round(self.score)}"), (1000, 50))
        self.text_format((f"HighScore: {round(self.highScore)}"), (1000, 85))
        self.text_format((f"Deaths: {self.death_count}"), (70, 50))