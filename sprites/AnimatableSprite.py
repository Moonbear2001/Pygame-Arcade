import pygame

import SpriteSheet

class AnimatableSprite(pygame.sprite.Sprite):
    """
    Sprite that accepts a sprite sheet and can create, set, loop etc. various animations.
    """
    def __init__(self, sprite_sheet: SpriteSheet):
        super().__init__()
        self.animations = {}