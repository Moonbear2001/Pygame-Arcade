import pygame

from ..scene import Scene
from utilities import render_text_block
from paths import IMAGES_DIR


TEXT_BLOCK = """Welcome to the Pygame Arcade. I created this project as a way to catalog my various pygame projects into one central game. 

Use the 'a' and 'd' or 'left arrow' and 'right arrow' keys to navigate between the exit, the info screen, and the games. Hold 'e' or 'enter' in order to play the game.

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
        self.info_img = pygame.image.load(IMAGES_DIR / "info.png")

    def _render_before_children(self):
        self.canvas.blit(self.info_img, (0, 0))
        render_text_block(
            self.canvas, TEXT_BLOCK, "roboto", color="black", padding_x=100, padding_y=100, size=35
        )
