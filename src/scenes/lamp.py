import pygame

from .scene import Scene
from paths import IMAGES_DIR


class Lamp(Scene):
    """
    Street lamp.
    """

    WIDTH_PX = 135
    HEIGHT_PX = 420

    def __init__(self, left, bottom):
        super().__init__(
            width=self.WIDTH_PX, height=self.HEIGHT_PX, bottom=bottom, left=left
        )
        self.lamp_img = pygame.image.load(IMAGES_DIR / "lamp.png").convert_alpha()

    def _on_render(self):
        self.canvas.blit(self.lamp_img, (0, 0))
