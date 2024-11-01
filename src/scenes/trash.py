import pygame

from .scene import Scene
from paths import IMAGES_DIR


class Trash(Scene):

    def __init__(self, left, top):
        super().__init__(watched_events=self.custom_watched_events)
        self.trash_img = pygame.image.load(IMAGES_DIR / "settings.png").convert_alpha()

    def _on_render(self):
        self.canvas.blit(self.trash_img, (0, 0))
        