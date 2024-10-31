import pygame

from .animatable_sprite import AnimatableSprite
from ..button import Button

class AnimatableButton(Button, AnimatableSprite):
    def __init__(
        self,
        x, y, width, height,
        sprite_sheet_file, num_rows, num_cols, px_width, px_height,
        colorkey=None, **kwargs
    ):
        # Initialize Button and AnimatableSprite
        Button.__init__(self, x, y, width, height, **kwargs)
        AnimatableSprite.__init__(self, sprite_sheet_file, num_rows, num_cols, px_width, px_height, colorkey)

        self.add_animation("idle", start_row=0, num_frames=4, frame_duration=100)
        self.add_animation("hover", start_row=1, num_frames=4, frame_duration=100)
        self.play_animation("idle")

    def update(self, delta_time):
        """
        Check if hovered and switch to hover animation.
        """
        if self.is_hovered(pygame.mouse.get_pos()):
            self.play_animation("hover")
        else:
            self.play_animation("idle")

        super().update(delta_time) 

    def render(self):
        surface = self.surface.copy()
        surface.blit(self.image, (0, 0)) 
        return surface
