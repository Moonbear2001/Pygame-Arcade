import pygame
import time

from managers import (
    AudioManager,
    SceneManager,
    TransitionManager,
    EventManager,
)
from constants import CANVAS_WIDTH, CANVAS_HEIGHT


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
        self.screen_width = CANVAS_WIDTH
        self.screen_height = CANVAS_HEIGHT
        flags = pygame.NOFRAME | pygame.RESIZABLE
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height), flags=flags
        )
        pygame.display.set_caption(self.name)

        self.running = True
        self.playing = True
        self.delta_time = 0
        self.prev_time = 0
        self.fps = 60

    def manage_delta_time(self):
        now = time.time()
        self.delta_time = now - self.prev_time
        self.prev_time = now

    def process_global_events(self, event):
        """
        Handle global events that are relevant to the entire game.
        This can include input handling for scene transitions or other game controls.
        """
        # Esc go back one scene (if possible)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            SceneManager().pop_scene()

        # Quit gracefully
        if event.type == pygame.QUIT:
            self.game_quit()

        # Update resolution if window is resized
        if event.type == pygame.WINDOWRESIZED:
            self.screen_width = event.x
            self.screen_height = event.y

    def event_loop(self):
        """
        Handle global events, let managers handle events, then publish events to
        suscribed scenes.
        """
        for event in pygame.event.get():
            self.process_global_events(event)
            AudioManager().handle_event(event)
            EventManager().publish(event)

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
        SceneManager().set_scene("intro")

        while self.playing:
            self.manage_delta_time()
            self.event_loop()
            self.update()
            self.render()
            clock.tick(self.fps)

        self.game_quit()
