import pygame
import time

from states.title import Title
from states.loading import Loading
from managers import SaveLoadManager
from paths import *

class Game:
    """
    Top level class. Initializes pygame, manages global resources, and holds the main game loop.

    Uses the singleton design pattern, so the single instance of Game can be accessed to use useful functions and get constants like canvas width.
    """

    name = "Template"
    screen_width = 1280
    screen_height = 720
    canvas_width = 1280
    canvas_height = 720

    # Store custom global colors here
    custom_colors = {"gold": (255, 215, 0)}

    # Class-level variable to hold the single instance
    _instance = None  

    def __new__(cls, *args, **kwargs):
        """
        Ensure only one instance of Game is created (singleton pattern).
        """
        if cls._instance is None:
            cls._instance = super(Game, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Initialize the game.
        """
        # Prevent re-initialization
        if hasattr(self, "initialized"):
            return
        
        pygame.init()


        self.canvas = pygame.Surface((self.canvas_width, self.canvas_height))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.name)

        self.state_stack = []
        self.running = True
        self.playing = True
        self.delta_time = 0
        self.prev_time = 0
        self.fps = 60

        self.fonts = None
        self.font_init()

        self.example_img = None
        self.image_init()

        self.example_sound = None
        self.sound_init()

    def font_init(self):
        """
        Store globally available fonts.
        """
        self.fonts = ("pokemon", "roboto")

    def image_init(self):
        """
        Store globally available images.
        """
        self.example_img = pygame.image.load(IMAGES_DIR / "pygame_logo.png").convert()

    def sound_init(self):
        """
        Store globally available sounds.
        """
        self.example_sound = pygame.mixer.Sound(SOUNDS_DIR / "example_sound.mp3")

    def manage_delta_time(self):
        now = time.time()
        self.delta_time = now - self.prev_time
        self.prev_time = now

    def event_loop(self):
        for event in pygame.event.get():
            self.state_stack[-1].handle_event(event)

    def update(self):
        self.state_stack[-1].update(self.delta_time)

    def render(self):
        self.state_stack[-1].render()
        scaled_canvas = pygame.transform.scale(self.canvas, (self.screen_width, self.screen_height))
        self.screen.blit(scaled_canvas, (0, 0))
        pygame.display.flip()

    @staticmethod
    def render_text(self, surface, text, font, color, x, y, size=10, center=True):
        """
        Static utility function for rendering some text.
        """
        # If font is nonexistent, rendering is skipped
        if font is None or font not in self.fonts:
            return

        path = FONTS_DIR / (font + ".ttf")
        text_surface = pygame.font.Font(path, size).render(text, True, color)
        text_rect = text_surface.get_rect()
        if center:
            text_rect.center = (x, y)
        else:
            text_rect.x = x
            text_rect.y = y
        surface.blit(text_surface, text_rect)

    @staticmethod
    def game_quit(self):
        """
        Static function for maintenance before game closes. Saves data, exits.
        """
        self.save_load_manager.save_data(self.saved_game_data, "data")
        pygame.quit()
        exit()


    def game_loop(self):
        """
        The main game loop.
        """
        clock = pygame.time.Clock()
        self.prev_time = time.time()
        Loading(self).enter_state()

        while self.playing:

            # --- Delta time logic --- #
            self.manage_delta_time()

            # --- Event Loop --- #
            self.event_loop()

            # --- Game logic --- #
            self.update()

            # --- Drawing to screen --- #
            self.render()

            # --- Limit frame rate --- #
            clock.tick(self.fps)

        self.game_quit()