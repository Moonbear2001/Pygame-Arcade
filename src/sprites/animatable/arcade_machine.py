import pygame
from random import randint

from .animatable_sprite import AnimatableSprite


class GameplayPreview(AnimatableSprite):
    """
    Preview animation that plays on the arcade machine screen before the game is played.
    """

    SPRITESHEET_FILE = "arcade_machine/gameplay_previews.png"
    NUM_ROWS = 2
    NUM_COLS = 23
    PX_WIDTH = 7820
    PX_HEIGHT = 400
    COLORKEY = None

    def __init__(self, game):
        """
        'game' = name of game to preview
        """
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
        )

        self.add_animation("pong", 0, 23, 0.5)
        self.add_animation("out_of_order", 1, 10, 2.2)

        self.play_animation(game)

    def update(self, delta_time):
        super().update(delta_time)

    def render(self):
        return self.image


class ArcadeMachineBar(AnimatableSprite):
    """
    Loading, idle, etc. animations that play on the bar space on the arcade machine
    before the game is played.
    """

    SPRITESHEET_FILE = "arcade_machine/bar_animations.png"
    NUM_ROWS = 3
    NUM_COLS = 10
    PX_WIDTH = 5000
    PX_HEIGHT = 120
    COLORKEY = None

    def __init__(self):
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
        )

        self.add_animation("loading", 0, 10, 1)
        self.add_animation("idle1", 1, 24, 1)
        self.add_animation("idle2", 2, 2, 3)

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
    NUM_COLS = 5
    PX_WIDTH = 2200
    PX_HEIGHT = 140
    COLORKEY = None

    def __init__(self, game):
        """
        'game' = name of game
        """
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
        )

        self.add_animation("arcade", 0, 5, 1.3)
        self.add_animation("pong", 1, 5, 1.3)

        if game == "out_of_order":
            self.play_animation("arcade")
        else:
            self.play_animation(game)

    def update(self, delta_time):
        super().update(delta_time)

    def render(self):
        return self.image


class ArcadeMachine(AnimatableSprite):
    """
    Arcade machine that previews a game and takes the player into that game.
    """

    SPRITESHEET_FILE = "arcade_machine/arcade_machine.png"
    NUM_ROWS = 10
    NUM_COLS = 1
    PX_WIDTH = 600
    PX_HEIGHT = 10000
    COLORKEY = None

    def __init__(self, game_name):
        """
        Pick a random arcade machine sprite upon initialization.
        'game' = tells which preview to show
        """
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
        )

        self.game_name = game_name

        self.add_animation("random", randint(0, self.NUM_ROWS - 1), 1, 1)
        self.play_animation("random")

        # Add game preview animation
        self.game_title = GameTitle(game_name)
        self.game_preview = GameplayPreview(game_name)
        self.bar = ArcadeMachineBar()

    def update(self, delta_time):
        super().update(delta_time)
        self.game_title.update(delta_time)
        self.game_preview.update(delta_time)
        self.bar.update(delta_time)

    def render(self):
        self.image.blit(
            self.game_title.render(),
            (8 / 60 * self.image.get_width(), 4 / 100 * self.image.get_height()),
        )
        self.image.blit(
            self.game_preview.render(),
            (13 / 60 * self.image.get_width(), 15 / 100 * self.image.get_height()),
        )
        self.image.blit(
            self.bar.render(),
            (4 / 60 * self.image.get_width(), 54 / 100 * self.image.get_height()),
        )
        return pygame.transform.scale_by(self.image, 0.5)

    def handle_event(self, event):
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
        #     print('ENTER')
        pass
