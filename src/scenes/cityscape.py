import pygame

from .scene import Scene
from paths import IMAGES_DIR


class Cityscape(Scene):

    WIDTH_PX = 405
    HEIGHT_PX = 180

    def __init__(self, left, top):
        super().__init__(width=self.WIDTH_PX, height=self.HEIGHT_PX, top=top, left=left)
        self.trash_img = pygame.image.load(IMAGES_DIR / "cityscape.png")

    def _render_before_children(self):
        self.canvas.blit(self.trash_img, (0, 0))
