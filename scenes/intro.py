import pygame
from threading import Timer

from .scene import Scene
from sprites import Player
from managers import TransitionManager
from paths import IMAGES_DIR


class Intro(Scene):
    """
    Shows an intro screen then transitions to the arcade.
    """

    name = "intro"

    def __init__(self, left, top, width, height):
        """
        Initialize a new scene.
        """
        super().__init__(left, top, width, height)
        self.timer = Timer(
            1, lambda: TransitionManager().start_transition("fade_to_black", "arcade")
        )
        self.intro_image = pygame.image.load(IMAGES_DIR / "intro.png")

    def on_enter(self):
        self.timer.start()

    def on_render(self):
        self.canvas.blit(self.intro_image, (0, 0))
        return self.canvas
