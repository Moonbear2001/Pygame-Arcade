import pygame

from ..scene import Scene
from paths import IMAGES_DIR


class LampLight(Scene):

    def __init__(self, left, top, **kwargs):
        super().__init__(left, top, **kwargs)
        self.light_img = pygame.image.load(IMAGES_DIR / "lamp_light.png")
        self.canvas.set_alpha(40)

    def _render_before_children(self):
        self.canvas.blit(self.light_img, (0, 0))
