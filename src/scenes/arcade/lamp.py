import pygame

from ..anim_scene import AnimScene
from ..scene import Scene
from paths import SPRITESHEETS_DIR, IMAGES_DIR


class Lamp(AnimScene):
    """
    Street lamp.
    """

    SPRITESHEET_FILE = SPRITESHEETS_DIR / "lamp.png"
    NUM_ROWS = 1
    NUM_COLS = 2
    PX_WIDTH = 270
    PX_HEIGHT = 420

    def __init__(self, left, bottom, **kwargs):
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
            left=left,
            bottom=bottom,
            **kwargs
        )
        self.add_animation("loop", 0, 2, 1)
        self.play_animation("loop")
