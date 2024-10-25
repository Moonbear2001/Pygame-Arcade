import pygame
import time

from managers import *
from paths import *

class Game:
    """
    Top level class. Initializes pygame, manages global resources, and holds the main game loop.
    """

    def __init__(self):
        """
        Initialize the game.
        """
        pygame.init()

        self.name = "Template"
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.name)

        self.running = True
        self.playing = True
        self.delta_time = 0
        self.prev_time = 0
        self.fps = 60

        self.managers_init()

        self.example_img = None
        self.image_init()

        self.example_sound = None
        self.sound_init()

    def managers_init(self):
        """
        Initialize all managers. They are all singletons so can just be instantiated here.
        """
        StateManager()
        SaveLoadManager()
        AudioManager()

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

            # Quit gracefully
            if event.type == pygame.QUIT:
                self.game_quit()

            if event.type == pygame.KEYDOWN:
                
                # Esc to quit
                if event.key == pygame.K_ESCAPE:
                    self.game_quit()

            StateManager().handle_event(event)

    def update(self):
        StateManager().update(self.delta_time)

    def render(self):
        canvas = StateManager().render()
        scaled_canvas = pygame.transform.scale(canvas, (self.screen_width, self.screen_height))
        self.screen.blit(scaled_canvas, (0, 0))
        pygame.display.flip()

    def game_quit(self):
        """
        Gracefully quit.
        """
        pygame.quit()
        exit()


    def game_loop(self):
        """
        The main game loop.
        """
        clock = pygame.time.Clock()
        self.prev_time = time.time()
        StateManager().set_state("loading")

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