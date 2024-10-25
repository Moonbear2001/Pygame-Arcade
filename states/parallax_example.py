import pygame

from states import State


class ParallaxExample(State):
    """
    Example using the parallax effect.
    """
    def __init__(self):
        super().__init__()
        self.name = "Parallax"

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)