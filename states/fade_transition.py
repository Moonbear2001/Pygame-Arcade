import pygame
from pygame.locals import MOUSEBUTTONDOWN

from states import State
from sprite.sprites import ArcadeMachine

from utilities import render_text
from managers import StateManager, AudioManager


class FadeTransition(State):
    """
    Transition between states that fades to black and then fades back in from black.
    """

    def __init__(self, next_state_name):
        super().__init__()
        self.name = "arcade"

        self.machine1 = ArcadeMachine()

        # AudioManager().play_music("arcade_music/1.mp3", loops=-1)
        AudioManager().play_playlist("arcade_music")
        

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)


    def render(self):
        self.canvas.fill("pink")
        self.canvas.blit(self.machine1.render(), self.machine1.rect)
        return self.canvas
