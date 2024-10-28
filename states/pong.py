import pygame

from states import State
from managers import SaveLoadManager
from utilities import render_text


class Pong(State):
    """
    Pong placeholder.
    """
    def __init__(self):
        super().__init__()
        self.name = "Pong"


    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)

    def render(self):
        self.canvas.fill("red")
        return self.canvas

    def cleanup(self):
        """
        Save new high score if acheived before exiting.
        """
        pass
