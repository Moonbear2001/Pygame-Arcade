import pygame
import time

from managers import AudioManager, SaveLoadManager, SceneManager, TransitionManager


class Game:
    """
    Top level class.
    Initializes pygame, manages global resources, and holds the main game loop.
    """

    def __init__(self):
        """
        Initialize the game.
        """
        pygame.init()

        self.name = "Template"
        self.screen_width = 1280
        self.screen_height = 720
        # flags = pygame.NOFRAME | pygame.RESIZABLE
        flags = pygame.RESIZABLE
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height), flags=flags
        )
        pygame.display.set_caption(self.name)

        self.running = True
        self.playing = True
        self.delta_time = 0
        self.prev_time = 0
        self.fps = 60

        SceneManager()
        SaveLoadManager()
        AudioManager()
        TransitionManager()

    def manage_delta_time(self):
        now = time.time()
        self.delta_time = now - self.prev_time
        self.prev_time = now

    def event_loop(self):
        for event in pygame.event.get():

            # Quit gracefully
            if event.type == pygame.QUIT:
                self.game_quit()

            # Update resolution if window is resized
            if event.type == pygame.WINDOWRESIZED:
                self.screen_width = event.x
                self.screen_height = event.y

            # Let managers handle events
            SceneManager().handle_event(event)
            AudioManager().handle_event(event)

    def update(self):
        SceneManager().update(self.delta_time)
        TransitionManager().update(self.delta_time)

    def render(self):
        """
        Get the canvas from the SceneManager.
        Draw any current transition effects on top.
        Scale the canvas to the screen width.
        """
        canvas = SceneManager().render()
        TransitionManager().render(canvas)
        scaled_canvas = pygame.transform.scale(
            canvas, (self.screen_width, self.screen_height)
        )
        self.screen.blit(scaled_canvas, (0, 0))
        # self.screen.blit(canvas, (0, 0))
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
        SceneManager().set_scene("intro", 0, 0, 1280, 720)

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
