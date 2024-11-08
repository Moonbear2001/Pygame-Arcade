import pygame

from ..scene import Scene
from paths import IMAGES_DIR


class LampLight(Scene):

    WIDTH_PX = 245
    HEIGHT_PX = 420

    def __init__(self, left, bottom, **kwargs):
        super().__init__(
            width=self.WIDTH_PX, height=self.HEIGHT_PX, bottom=bottom, left=left
        )
        self.light_img = pygame.image.load(
            IMAGES_DIR / "lamp_light.png"
        ).convert_alpha()
        self.canvas.set_alpha(20)

    def _render_before_children(self):
        self.canvas.blit(self.light_img, (0, 0))
