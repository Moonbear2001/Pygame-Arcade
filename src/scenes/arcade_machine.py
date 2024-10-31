import pygame
from random import randint

from .anim_scene import AnimScene


class ArcadeMachine(AnimScene):
    """
    Arcade machine scene.
    """

    class Bar(AnimScene):
        """
        Animations that take place in the bar of the arcade machine.
        """

        custom_watched_events = {pygame.KEYDOWN}

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
                left=40,
                top=540,
                width=self.PX_WIDTH // self.NUM_COLS,
                height=self.PX_HEIGHT // self.NUM_ROWS,
            )

            self.add_animation("pong", 0, 23, 0.5)
            self.add_animation("out_of_order", 1, 10, 2.2)

            self.play_animation("pong")

    class Screen(AnimScene):
        """
        Preview animation that plays on the arcade machine screen before the game is
        played.
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
                left=130,
                top=150,
                width=self.PX_WIDTH // self.NUM_COLS,
                height=self.PX_HEIGHT // self.NUM_ROWS,
            )

            self.add_animation("pong", 0, 23, 0.5)
            self.add_animation("out_of_order", 1, 10, 2.2)

            self.play_animation(game)

    class Title(AnimScene):
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
                left=80,
                top=40,
                width=self.PX_WIDTH // self.NUM_COLS,
                height=self.PX_HEIGHT // self.NUM_ROWS,
            )

            self.add_animation("arcade", 0, 5, 1.3)
            self.add_animation("pong", 1, 5, 1.3)

            if game == "out_of_order":
                self.play_animation("arcade")
            else:
                self.play_animation(game)

    SPRITESHEET_FILE = "arcade_machine/arcade_machine.png"
    NUM_ROWS = 10
    NUM_COLS = 1
    PX_WIDTH = 600
    PX_HEIGHT = 10000
    COLORKEY = None

    def __init__(self, game_name="pong"):
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

        self.title = ArcadeMachine.Title(game_name)
        self.screen = ArcadeMachine.Screen(game_name)
        self.bar = ArcadeMachine.Bar()

        self.add_child(self.title)
        self.add_child(self.screen)
        self.add_child(self.bar)
