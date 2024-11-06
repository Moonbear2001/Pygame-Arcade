from .anim_scene import AnimScene
from paths import SPRITESHEETS_DIR


class ArcadeSign(AnimScene):
    """
    "Pygame Arcade" arcade sign.
    """

    SPRITESHEET_FILE = SPRITESHEETS_DIR / "pygame_arcade_sign.png"
    NUM_ROWS = 1
    NUM_COLS = 29
    PX_WIDTH = 20590
    PX_HEIGHT = 110

    def __init__(self, left, top, **kwargs):
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
            **kwargs
        )
        self.add_animation("loop", 0, 29, 0.25)
        self.play_animation("loop")
