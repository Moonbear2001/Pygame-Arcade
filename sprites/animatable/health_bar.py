import pygame
from .animatable_sprite import AnimatableSprite


class HealthBar(AnimatableSprite):
    """
    Simple health bar sprite.
    """

    # All HealthBars share one sprite sheet, so information can be shared across instances
    SPRITESHEET_FILE = "example_sprite_sheet.png"
    NUM_ROWS = 1
    NUM_COLS = 7
    PX_WIDTH = 1792
    PX_HEIGHT = 64
    COLORKEY = None

    def __init__(self, x=0, y=0, width=256, height=64):
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
            colorkey=self.COLORKEY,
        )
        self.rect = pygame.Rect(x, y, width, height)

        self.add_animation("loop", 0, 7, 1)
        self.play_animation("loop")

    def update(self, delta_time):
        super().update(delta_time)
