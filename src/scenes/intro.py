import pygame
from threading import Timer

from .scene import Scene
from managers import TransitionManager
from paths import IMAGES_DIR


class Intro(Scene):
    """
    Shows an intro screen then transitions to the arcade.
    """

    name = "intro"

    def __init__(self):
        super().__init__()
        self.timer = Timer(
            1,
            lambda: TransitionManager().start_transition(
                "fade_to_black", "arcade", "fade_from_black"
            ),
        )
        self.intro_image = pygame.image.load(IMAGES_DIR / "intro.png")

    def _on_enter(self):
        self.timer.start()

    def _on_render(self):
        self.canvas.blit(self.intro_image, (0, 0))
        return self.canvas
