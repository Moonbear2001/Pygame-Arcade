import pygame

from states.state import State


class ParallaxExample(State):
    """
    """
    def __init__(self, game, folder):
        super().__init__(game)
        self.name = "Parallax"

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)

    def render(self):
        
        super().render()