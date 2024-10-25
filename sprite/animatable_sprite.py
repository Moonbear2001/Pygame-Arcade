import pygame

from .sprite_sheet import SpriteSheet
from .animation import Animation

class AnimatableSprite(pygame.sprite.Sprite):
    """
    Sprite that accepts a sprite sheet and can create, set, loop etc. various animations.
    Designed to work with sprite sheets where each row contains an animation.
    """
    def __init__(self, sprite_sheet_file, num_rows, num_cols, px_width, px_height, colorkey=None):
        super().__init__()
        self.sprite_sheet = SpriteSheet(sprite_sheet_file, num_rows, num_cols, px_width, px_height, colorkey)
        self.animations = {}
        self.current_animation = None
        self.image = None
        self.rect = None

    def add_animation(self, name, start_row, num_frames, frame_duration):
        self.animations[name] = Animation(start_row, num_frames, frame_duration)

    def play_animation(self, animation_name):
        """
        If the animation doesn't exist, does nothing.
        """
        if animation_name in self.animations:
            self.current_animation = self.animations[animation_name]
            self.current_animation.current_frame = 0
            self.current_animation.time_elapsed = 0
            self.image = self.sprite_sheet.get_frame(self.current_animation.start_row, self.current_animation.current_frame)

    def update(self, delta_time):
        """
        Manage transitioning to next frame on time, etc.
        """
        if not self.current_animation:
            return
        
        anim = self.current_animation
        anim.time_elapsed += delta_time
        
        # Current frame over
        if anim.time_elapsed >= anim.frame_duration:
            anim.time_elapsed = anim.time_elapsed - anim.frame_duration
            anim.time_elapsed = 0
            anim.current_frame = (anim.current_frame + 1) % anim.num_frames
            self.image = self.sprite_sheet.get_frame(anim.start_row, anim.current_frame)

    def render(self):
        """
        Return an image to be rendered one level above.
        """
        return self.image

    





    