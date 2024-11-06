import pygame

from .anim_scene import AnimScene
from paths import SPRITESHEETS_DIR
from managers import TransitionManager
# from ..focusable_item import FocusableItem


class ExitSign(AnimScene):
    """
    Pygame logo on a screen.
    """

    SPRITESHEET_FILE = SPRITESHEETS_DIR / "exit_sign.png"
    NUM_ROWS = 1
    NUM_COLS = 17
    PX_WIDTH = 2975
    PX_HEIGHT = 75
    custom_watched_events = {pygame.KEYDOWN, pygame.KEYUP}


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
            watched_events = self.custom_watched_events,
            **kwargs
        )
        # super().__init__(left, top, width=self.PX_WIDTH // self.NUM_COLS, height=self.PX_HEIGHT // self.NUM_ROWS, )
        self.focused = False
        self.add_animation("loop", 0, 17, 0.2)
        self.play_animation("loop")

    def _on_event(self, event):
        if self.focused and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            pygame.quit()