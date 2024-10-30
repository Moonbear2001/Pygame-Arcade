import pygame

from .animatable_sprite import AnimatableSprite


class Player(AnimatableSprite):
    """
    Basic player with animations and movement.
    """

    SPRITESHEET_FILE = "example_sprite_sheet.png"
    NUM_ROWS = 2
    NUM_COLS = 5
    PX_WIDTH = 300
    PX_HEIGHT = 128
    COLORKEY = (247, 247, 247)

    def __init__(self, x=0, y=0, width=100, height=100):
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
            colorkey=self.COLORKEY,
        )
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 10
        self.actions = {"right": False, "left": False, "up": False, "down": False}

        # Add animations
        self.add_animation("run", 0, 5, 0.1)
        self.play_animation("run")

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.actions["right"] = True
            if event.key == pygame.K_a:
                self.actions["left"] = True
            if event.key == pygame.K_w:
                self.actions["up"] = True
            if event.key == pygame.K_s:
                self.actions["down"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.actions["right"] = False
            if event.key == pygame.K_a:
                self.actions["left"] = False
            if event.key == pygame.K_w:
                self.actions["up"] = False
            if event.key == pygame.K_s:
                self.actions["down"] = False

    def update(self, delta_time):
        super().update(delta_time)
        if self.actions["right"]:
            self.rect.x += self.speed
        if self.actions["left"]:
            self.rect.x -= self.speed
        if self.actions["up"]:
            self.rect.y -= self.speed
        if self.actions["down"]:
            self.rect.y += self.speed
