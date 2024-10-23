import pygame
import time
from states.title import Title
from states.loading import Loading
from SaveLoadManager import SaveLoadManager


class Game:

    screen_width = 1280
    screen_height = 720

    custom_colors = {"gold": (255, 215, 0)}

    def __init__(self):
        """
        Initialize the game.
        """
        pygame.init()

        self.game_name = "Template"
        self.canvas_width = 1280
        self.canvas_height = 720
        self.canvas = pygame.Surface((self.canvas_width, self.canvas_height))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.game_name)

        self.state_stack = []
        self.running = True
        self.playing = True
        self.delta_time = 0
        self.prev_time = 0
        self.fps = 60

        self.score = 0
        self.save_load_manager = SaveLoadManager(".save", "save_data")
        self.saved_game_data = self.save_load_manager.load_data("data")

        self.fonts = None
        self.font_init()

        self.example_img = None
        self.example_sprite_sheet = None
        self.image_init()

        self.example_sound = None
        self.sound_init()

    def font_init(self):
        self.fonts = ("pokemon", "roboto")

    def image_init(self):
        self.example_img = pygame.image.load("images/pygame_logo.png").convert()
        self.example_sprite_sheet = pygame.image.load("images/example_sprite_sheet.png").convert_alpha()

    def sound_init(self):
        self.example_sound = pygame.mixer.Sound("sounds/example_sound.mp3")

    def render_text(self, surface, text, font, color, x, y, size=10, center=True):
        """
        :param surface:
        :param text:
        :param font:
        :param color:
        :param x:
        :param y:
        :param size:
        :param center: positions text using provided x, y as center
        :return:
        """
        # If font is nonexistent, rendering is skipped
        if font is None or font not in self.fonts:
            return

        path = "fonts/" + font + ".ttf"
        text_surface = pygame.font.Font(path, size).render(text, True, color)
        text_rect = text_surface.get_rect()
        if center:
            text_rect.center = (x, y)
        else:
            text_rect.x = x
            text_rect.y = y
        surface.blit(text_surface, text_rect)

    def get_delta_time(self):
        now = time.time()
        self.delta_time = now - self.prev_time
        self.prev_time = now

    def event_loop(self):
        for event in pygame.event.get():
            self.state_stack[-1].handle_event(event)

    def update(self):
        self.state_stack[-1].update()

    def render(self):
        self.state_stack[-1].render()
        scaled_canvas = pygame.transform.scale(self.canvas, (self.screen_width, self.screen_height))
        self.screen.blit(scaled_canvas, (0, 0))
        pygame.display.flip()

    def game_loop(self):
        """
        The main game loop.
        """
        clock = pygame.time.Clock()
        self.prev_time = time.time()
        Loading(self).enter_state()

        while self.playing:

            # --- Delta time logic --- #
            self.get_delta_time()

            # --- Event Loop --- #
            self.event_loop()

            # --- Game logic --- #
            self.update()

            # --- Drawing to screen --- #
            self.render()

            # --- Limit frame rate --- #
            clock.tick(self.fps)

        self.game_quit()

    def game_quit(self):
        """
        Maintenance before game closes. Save data, etc.
        :return:
        """
        # Save Data
        self.save_load_manager.save_data(self.saved_game_data, "data")

        pygame.quit()
        exit()
