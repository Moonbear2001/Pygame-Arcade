import pygame
from .anim_button import AnimButton
from paths import SPRITESHEETS_DIR


BUTTON_SPRITESHEETS = SPRITESHEETS_DIR / "buttons"


class PlusMinusButton(AnimButton):
    """
    Plus button.
    """

    PLUS_SPRITESHEET_FILE = BUTTON_SPRITESHEETS / "plus_button.png"
    MINUS_SPRITESHEET_FILE = BUTTON_SPRITESHEETS / "minus_button.png"
    NUM_ROWS = 3
    NUM_COLS = 1
    PX_WIDTH = 50
    PX_HEIGHT = 150

    def __init__(self, left, top, callback=None, minus=False,**kwargs):
        super().__init__(
            left=left,
            top=top,
            sprite_sheet_file=self.MINUS_SPRITESHEET_FILE if minus else self.PLUS_SPRITESHEET_FILE,
            num_rows=self.NUM_ROWS,
            num_cols=self.NUM_COLS,
            px_width=self.PX_WIDTH,
            px_height=self.PX_HEIGHT,
            callback=callback,
            **kwargs
        )
        self.hovered = False
        self.clicked = False

        self.add_animation("clicked", 2, 1, 1)
        self.add_animation("hovered", 1, 1, 1)
        self.add_animation("idle", 0, 1, 1)

        self.play_animation("idle")

    def _on_update(self, delta_time):
        """
        Updates the animation and hover state.
        """
        if self.clicked:
            self.play_animation("clicked")
        elif self.hovered:
            self.play_animation("hovered")
        super()._on_update(delta_time)
