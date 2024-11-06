from .anim_scene import AnimScene
from paths import SPRITESHEETS_DIR


class PythonLogo(AnimScene):
    """
    Python logo on a screen.
    """

    SPRITESHEET_FILE = SPRITESHEETS_DIR / "python_logo.png"
    NUM_ROWS = 1
    NUM_COLS = 4
    PX_WIDTH = 720
    PX_HEIGHT = 190

    def __init__(self, left, top, **kwargs):
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
            left=left,
            top=top,
            # width=self.PX_WIDTH // self.NUM_COLS,
            # height=self.PX_HEIGHT // self.NUM_ROWS,
            **kwargs
        )
        self.add_animation("loop", 0, 4, 1)
        self.play_animation("loop")
