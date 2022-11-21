import pygame

class SpriteSheet:

    def __init__(self, image):
        self.sheet = image
        self.image_width = 100
        self.image_height = 100

    def get_frame(self, actions, width, height):
        surface = pygame.Surface((width, height)).convert_alpha()
        surface.blit(self.sheet, (0, 0), ())