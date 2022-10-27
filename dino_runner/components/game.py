import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, GAME_OVER, RESET, RUNNING, DEAD
from dino_runner.components.obstacles.obstacles_manager import ObstaclesManager

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

    def resetGame(self):
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.game_speed = 20

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.obstacle_manager.update(self)
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()

    def update_score(self):
        self.score += 1

        if self.highScore < self.score:
            self.highScore = self.score

        if self.score % 100 == 0 and self.game_speed <= 46:
            self.game_speed += 2

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #Também aceita código hexadecimal "#FFFFFF"
        self.draw_background()
        self.obstacle_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed
    
    def draw_score(self):
        self.text_format((f"Score: {self.score}"), (1000, 50))
        self.text_format((f"HighScore: {self.highScore}"), (1000, 85))

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()
            
    def text_format(self, textReceived, position):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(textReceived, True, (0, 0, 0))        
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
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        if self.death_count == 0:
            self.screen.blit(RUNNING[0], (half_screen_width - 40, half_screen_height - 120))
            self.text_format("Press any Key to Start", (half_screen_width, half_screen_height))
        else:
            self.screen.blit(DEAD, (half_screen_width - 40, half_screen_height - 170))
            self.image_format(GAME_OVER, (half_screen_width, half_screen_height - 40))
            self.text_format("Press any Key to Restart", (half_screen_width, half_screen_height))
            self.image_format(RESET, (half_screen_width - 5, half_screen_height + 80))
            self.text_format((f"Score: {self.score}"), (1000, 50))
            self.text_format((f"HighScore: {self.highScore}"), (1000, 85))
            self.text_format((f"Deaths: {self.death_count}"), (70, 50))

        pygame.display.update()
        self.handle_events_on_menu()