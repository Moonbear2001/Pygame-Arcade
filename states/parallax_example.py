import pygame

from states import State
from sprite import ParallaxBackground


class ParallaxExample(State):
    """
    Example using the parallax effect.
    """
    def __init__(self):
        super().__init__()
        self.name = "Parallax"
        # self.prlx_bg = ParallaxBackground("cyberpunk_cityscape1")
        self.prlx_bg = ParallaxBackground("cyberpunk_cityscape2")

    def update(self, delta_time):
        super().update(delta_time)
        self.prlx_bg.update(delta_time)
    
    def render(self):
        # self.canvas.blit(self.prlx_bg.canvas, (0, 0))
        self.prlx_bg.draw(self.canvas)
        return self.canvas

    def handle_event(self, event):
        super().handle_event(event)