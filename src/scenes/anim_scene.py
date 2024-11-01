import pygame

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from paths import SPRITESHEETS_DIR
from .scene import Scene


class AnimScene(Scene):
    """
    A scene with the ability to set, create, loop, etc. animations.
    Currently no way to stop animations.
    """

    def __init__(
        self,
        sprite_sheet_file,
        num_rows,
        num_cols,
        px_width,
        px_height,
        colorkey=None,
        left=0,
        top=0,
        width=CANVAS_WIDTH,
        height=CANVAS_HEIGHT,
        watched_events=set(),
        scale=1,
    ):
        super().__init__(left, top, width, height, watched_events, scale)
        self.sprite_sheet = SpriteSheet(
            sprite_sheet_file, num_rows, num_cols, px_width, px_height, colorkey
        )
        self.animations = {}
        self.current_animation = None

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
            self.canvas = self.sprite_sheet.get_frame(
                self.current_animation.start_row, self.current_animation.current_frame
            )

    def _on_update(self, delta_time):
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
            self.canvas = self.sprite_sheet.get_frame(
                anim.start_row, anim.current_frame
            )


class Animation:
    """
    Defines an animation.
    """

    def __init__(self, start_row, num_frames, frame_duration, loop=False):
        self.start_row = start_row
        self.num_frames = num_frames
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.time_elapsed = 0
        self.loop = loop


class SpriteSheet:
    """
    Uplads and stores a spritesheet in a pygame Surface.
    Provides frames for said sprite sheet.
    """

    def __init__(
        self, sprite_sheet_file, num_rows, num_cols, px_width, px_height, colorkey=None
    ):
        """
        'image' should be an image file name with its extension ie. spritesheet.png
        """
        self.sheet = self.load_sprite_sheet(sprite_sheet_file, colorkey)
        self.num_rows = num_rows
        self.num_cols = num_cols
        # self.px_width = px_width
        # self.px_height = px_height
        self.frame_width = px_width / self.num_cols
        self.frame_height = px_height / self.num_rows
        self.curr_row = 0
        self.curr_col = 0

    def load_sprite_sheet(self, sprite_sheet_file, colorkey):
        sheet = pygame.image.load(SPRITESHEETS_DIR / sprite_sheet_file).convert_alpha()
        if colorkey is not None:
            sheet.set_colorkey(colorkey)
        return sheet

    def get_frame(self, row, col, scale=1):
        """
        Get a specific frame from the sprite sheet.
        Scale and make certain colors to transparent if requested.
        """
        frame = pygame.Surface(
            (self.frame_width, self.frame_height), flags=pygame.SRCALPHA
        ).convert_alpha()

        frame.blit(
            self.sheet,
            (0, 0),
            (
                col * self.frame_width,
                row * self.frame_height,
                self.frame_width,
                self.frame_height,
            ),
        )
        if scale != 1:
            frame = pygame.transform.scale(
                frame, (int(self.frame_width * scale), int(self.frame_height * scale))
            )
        return frame
