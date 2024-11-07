import pygame
from random import random

from ..anim_scene import AnimScene
from paths import SPRITESHEETS_DIR


class Cityscape(AnimScene):

    SPRITESHEET_FILE = SPRITESHEETS_DIR / "cityscape.png"
    NUM_ROWS = 1
    NUM_COLS = 43
    PX_WIDTH = 17415
    PX_HEIGHT = 180

    def __init__(self, left, top):
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
            left=left,
            top=top,
            width=self.PX_WIDTH // self.NUM_COLS,
            height=self.PX_HEIGHT // self.NUM_ROWS,
        )
        self.add_animation("loop", 0, 43, random())
        self.play_animation("loop")
