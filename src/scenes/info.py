import pygame

from .scene import Scene
from utilities import render_text_block


TEXT_BLOCK = """Welcome to the Pygame Arcade. I created this project as a way to catalog my various pygame projects into one central game. 

Use the 'a' and 'd' keys to navigate between games and hold 'e' or 'enter' in order to play the game.

Enjoy!
"""

class Info(Scene):
    """
    Settings.
    """

    name = "info"
    custom_watched_events = {pygame.KEYDOWN}

    def __init__(self):
        super().__init__(watched_events=self.custom_watched_events)

    def _render_before_children(self):
        self.canvas.fill("gray")
        render_text_block(self.canvas, TEXT_BLOCK, "roboto", padding=100, size=50)