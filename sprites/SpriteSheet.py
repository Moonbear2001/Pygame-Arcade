import pygame


class SpriteSheet:

    def __init__(self, image):
        self.sheet = image
        self.num_rows = 2
        self.num_cols = 5
        self.num_frames = self.num_rows * self.num_cols
        self.px_width = 300
        self.px_height = 128
        self.frame_width = self.px_width / self.num_cols
        self.frame_height = self.px_height / self.num_rows
        self.curr_row = 0
        self.curr_col = 0

    def get_frame(self, actions, width, height, scale=1):

        self.curr_col = (self.curr_col + 1) % self.num_cols
        self.curr_row = (self.curr_row + 1) % self.num_rows

        frame = pygame.Surface((width, height)).convert_alpha()
        frame.blit(self.sheet, (0, 0), (self.curr_row * self.frame_width, self.curr_col * self.frame_height,
                                        self.frame_width, self.frame_height))
        if scale != 1:
            frame = pygame.transform.scale(frame, (width * scale, height * scale))

        frame.set_colorkey((255, 255, 255))

        return frame

