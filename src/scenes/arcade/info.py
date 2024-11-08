import pygame

from ..scene import Scene
from utilities import render_text_block
from paths import IMAGES_DIR


WELCOME = "Welcome to the Pygame Arcade."
NAVIGATION = "Navigate between the exit, info screen, games."
CAMERA = "Pan the camera left and right."
BACK_SCENE = "Go back one scene."
SELECT = "Hold to select or play a game."
FINAL = "Enjoy!"


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
            self.canvas,
            WELCOME,
            55,
            "pixel",
            color="black",
            padding_x=300,
            padding_y=100,
            size=40,
        )
        render_text_block(
            self.canvas,
            NAVIGATION,
            55,
            "pixel",
            color="black",
            padding_x=230,
            padding_y=220,
            size=32,
        )
        render_text_block(
            self.canvas,
            CAMERA,
            55,
            "pixel",
            color="black",
            padding_x=230,
            padding_y=300,
            size=32,
        )
        render_text_block(
            self.canvas,
            BACK_SCENE,
            55,
            "pixel",
            color="black",
            padding_x=230,
            padding_y=380,
            size=32,
        )
        render_text_block(
            self.canvas,
            SELECT,
            55,
            "pixel",
            color="black",
            padding_x=230,
            padding_y=460,
            size=32,
        )
        render_text_block(
            self.canvas,
            FINAL,
            55,
            "pixel",
            color="black",
            padding_x=580,
            padding_y=600,
            size=40,
        )
