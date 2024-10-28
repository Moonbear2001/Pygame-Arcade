import pygame
from ..animatable_sprite import AnimatableSprite

class GameplayPreview(AnimatableSprite):
    """
    Preview animation that plays on the arcade machine screen before the game is played.
    """

    SPRITESHEET_FILE = "arcade_machine/gameplay_previews.png"
    NUM_ROWS = 1
    NUM_COLS = 23
    PX_WIDTH = 7820
    PX_HEIGHT = 200
    COLORKEY = None

    def __init__(self):
        super().__init__(self.SPRITESHEET_FILE, self.NUM_ROWS, self.NUM_COLS, self.PX_WIDTH, self.PX_HEIGHT)

        self.add_animation("pong", 0, 24, 0.5)
        
        self.play_animation("pong")

    def update(self, delta_time):
            super().update(delta_time)

    def render(self):
        return self.image


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
        super().__init__(self.SPRITESHEET_FILE, self.NUM_ROWS, self.NUM_COLS, self.PX_WIDTH, self.PX_HEIGHT)

        self.add_animation("loading", 0, 10, 1)
        self.add_animation("idle", 1, 24, 1)
        
        self.play_animation("loading")

    def update(self, delta_time):
        super().update(delta_time)

    def render(self):
        return self.image

    

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
    PX_WIDTH = 600
    PX_HEIGHT = 2000
    COLORKEY = None
    
    screen_px_pos = (13, 15)
    orig_px_size = (60, 100)

    """
    33px original screen width
    50 px original arcade width
    33/50 * actual arcade width

    width of arcade * 33/50
    
    
    """


    def __init__(self):
        super().__init__(self.SPRITESHEET_FILE, self.NUM_ROWS, self.NUM_COLS, self.PX_WIDTH, self.PX_HEIGHT)

        self.add_animation("default", 0, 1, 1)
        self.add_animation("transparent_screens", 1, 1, 1)
        
        self.play_animation("default")

        # Add game preview animation
        self.game_preview = GameplayPreview()
        self.bar = ArcadeMachineBar()
        
    
    def update(self, delta_time):
        super().update(delta_time)
        self.game_preview.update(delta_time)
        self.bar.update(delta_time)

    def render(self):
        self.image.blit(self.game_preview.render(), (13/60 * self.image.get_width(), 15/100 * self.image.get_height()))
        self.image.blit(self.bar.render(), (4/60 * self.image.get_width(), 54/100 * self.image.get_height()))
        # self.image.blit(self.game_preview.render(), pygame.Rect(13/60 * self.image.get_width(), 15/100 * self.image.get_height(), 1, 19/100 * self.image.get_height()))
        return self.image

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            print('ENTER')

