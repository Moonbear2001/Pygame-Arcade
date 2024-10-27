import pygame
from ..animatable_sprite import AnimatableSprite

class GameplayPreview(AnimatableSprite):
    """
    Preview animation that plays on the arcade machine screen before the game is played.
    """

    SPRITESHEET_FILE = "arcade_machine/gameplay_previews.png"
    NUM_ROWS = 1
    NUM_COLS = 24
    PX_WIDTH = 11424
    PX_HEIGHT = 280
    COLORKEY = None

    def __init__(self):
        super().__init__()


class ArcadeMachineBar(AnimatableSprite):
    """
    Loading, idle, etc. animations that play on the bar space on the arcade machine before the game is played.
    """

    SPRITESHEET_FILE = "arcade_machine/bar_animations.png"
    NUM_ROWS = 2
    NUM_COLS = 10
    PX_WIDTH = 5000
    PX_HEIGHT = 80
    COLORKEY = None

    def __init__(self):
        super().__init__()

class GameTitle(AnimatableSprite):
    """
    Top bar of the arcade machine that shows the game title.
    """

    SPRITESHEET_FILE = "arcade_machine/arcade_machine_title.png"
    NUM_ROWS = 2
    NUM_COLS = 1
    PX_WIDTH = 440
    PX_HEIGHT = 140
    COLORKEY = None

    def __init__(self):
        super().__init__()


class ArcadeMachine(AnimatableSprite):
    """
    Arcade machine that previews a game and takes the player into that game.
    """

    SPRITESHEET_FILE = "arcade_machine/arcade_machine.png"
    NUM_ROWS = 2
    NUM_COLS = 1
    PX_WIDTH = 540
    PX_HEIGHT = 1800
    COLORKEY = None

    def __init__(self):
        super().__init__(self.SPRITESHEET_FILE, self.NUM_ROWS, self.NUM_COLS, self.PX_WIDTH, self.PX_HEIGHT)

        self.add_animation("default", 0, 1, 1)
        self.add_animation("transparent_screens", 1, 1, 1)
        
        self.play_animation("default")
    
    def update(self, delta_time):
        super().update(delta_time)

    def render(self):
        return self.image

    

