import pygame

from paths import SPRITESHEETS_DIR

class SpriteSheet:
    """
    Uplads and stores a spritesheet in a pygame Surface.
    Provides frames for said sprite sheet.
    """

    def __init__(self, sprite_sheet_file, num_rows, num_cols, px_width, px_height, colorkey=None):
        """
        'image' should be an image file name with its extension ie. spritesheet.png
        """
        self.sheet = self.load_sprite_sheet(sprite_sheet_file, colorkey)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.px_width = px_width
        self.px_height = px_height
        self.frame_width = self.px_width / self.num_cols
        self.frame_height = self.px_height / self.num_rows
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
        frame = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA).convert_alpha()
        frame.blit(self.sheet, (0, 0), (col * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height))
        if scale != 1:
            frame = pygame.transform.scale(frame, (int(self.frame_width * scale), int(self.frame_height * scale)))
        return frame
