import pygame

from .scene import Scene
from paths import IMAGES_DIR

class Lamp(Scene):
    """
    Street lamp.
    """

    def __init__(self, left, top):
        super().__init__(watched_events=self.custom_watched_events)
        self.lamp_img = pygame.image.load(IMAGES_DIR / "lamp.png").convert_alpha()

    def _on_render(self):
        self.canvas.blit(self.lamp_img, (0, 0))
        
        
