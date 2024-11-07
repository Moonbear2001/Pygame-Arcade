import pygame

from ..anim_scene import AnimScene
from paths import SPRITESHEETS_DIR
from managers import SceneManager


class InfoScreen(AnimScene):
    """
    Pygame logo on a screen.
    """

    SPRITESHEET_FILE = SPRITESHEETS_DIR / "info_screen.png"
    NUM_ROWS = 1
    NUM_COLS = 8
    PX_WIDTH = 1400
    PX_HEIGHT = 105
    custom_watched_events = {pygame.KEYDOWN}

    def __init__(self, left, top, **kwargs):
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
            left=left,
            top=top,
            watched_events=self.custom_watched_events,
            **kwargs
        )
        self.focused = False
        self.add_animation("loop", 0, 5, 0.25)
        self.play_animation("loop")

    def _on_event(self, event):
        if (
            self.focused
            and event.type == pygame.KEYDOWN
            and (event.key == pygame.K_RETURN or event.key == pygame.K_e)
        ):
            SceneManager().push_scene("info")
