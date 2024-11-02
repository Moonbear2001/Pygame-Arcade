import pygame

from .scene import Scene
from paths import IMAGES_DIR


class Trash(Scene):

    WIDTH_PX = 65
    HEIGHT_PX = 90

    def __init__(self, left, bottom):
        super().__init__(
            width=self.WIDTH_PX, height=self.HEIGHT_PX, bottom=bottom, left=left
        )
        self.trash_img = pygame.image.load(IMAGES_DIR / "trash_can.png").convert_alpha()

    def _on_render(self):
        self.canvas.blit(self.trash_img, (0, 0))
