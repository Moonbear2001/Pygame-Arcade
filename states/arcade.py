import pygame
from pygame.locals import MOUSEBUTTONDOWN

from states import State
from sprite.sprites import ArcadeMachine

from utilities import render_text
from managers import StateManager


class Arcade(State):
    """
    Arcade.
    """

    def __init__(self):
        super().__init__()
        self.name = "arcade"

        self.machine1 = ArcadeMachine()
        

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)


    def render(self):
        self.canvas.fill("pink")
        return self.canvas
