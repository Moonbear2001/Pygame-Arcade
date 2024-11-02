import pygame
from random import randint, choice

from .anim_scene import AnimScene
from paths import SPRITESHEETS_DIR

ARCADE_MACHINE_SPRITESHEETS_DIR = SPRITESHEETS_DIR / "arcade_machine"


class ArcadeMachine(AnimScene):
    """
    Arcade machine scene.
    """

    class Bar(AnimScene):
        """
        Animations that take place in the bar of the arcade machine.
        """

        custom_watched_events = {pygame.KEYDOWN}

        SPRITESHEET_FILE = ARCADE_MACHINE_SPRITESHEETS_DIR / "bar_animations.png"
        NUM_ROWS = 3
        NUM_COLS = 10
        PX_WIDTH = 5000
        PX_HEIGHT = 120

        def __init__(self, random=True):
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

            self.add_animation("loading", 0, 10, 2.2)
            self.add_animation("flyby", 1, 10, 1)
            self.add_animation("dancing", 2, 2, 1)

            # Play random idle animation
            self.play_animation(choice(list(self.animations.keys())))

    class Screen(AnimScene):
        """
        Preview animation that plays on the arcade machine screen before the game is
        played.
        """

        SPRITESHEET_FILE = ARCADE_MACHINE_SPRITESHEETS_DIR / "gameplay_previews.png"
        NUM_ROWS = 2
        NUM_COLS = 23
        PX_WIDTH = 7820
        PX_HEIGHT = 400

        def __init__(self, game_name=None):
            """
            Show an out of order message if no game name is provided.
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

            if game_name:
                self.add_animation("pong", 0, 23, 0.5)
                self.play_animation(game_name)
            else:
                self.add_animation("out_of_order", 1, 10, 2.2)
                self.play_animation("out_of_order")

    class Title(AnimScene):
        """
        Top bar of the arcade machine that shows the game title.
        """

        SPRITESHEET_FILE = ARCADE_MACHINE_SPRITESHEETS_DIR / "arcade_machine_title.png"
        NUM_ROWS = 2
        NUM_COLS = 5
        PX_WIDTH = 2200
        PX_HEIGHT = 140

        def __init__(self, game_name):
            """
            Animation is left blank if no game name is provided.
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

            if game_name:
                self.add_animation("arcade", 0, 5, 1.3)
                self.add_animation("pong", 1, 5, 1.3)
                self.play_animation(game_name)

    SPRITESHEET_FILE = ARCADE_MACHINE_SPRITESHEETS_DIR / "arcade_machine.png"
    NUM_ROWS = 10
    NUM_COLS = 1
    PX_WIDTH = 600
    PX_HEIGHT = 10000

    def __init__(self, left, bottom, game_name, **kwargs):
        """
        Pick a random arcade machine sprite upon initialization, tell screen, bar, and
        title which animation to play by providing game name.
        """
        super().__init__(
            self.SPRITESHEET_FILE,
            self.NUM_ROWS,
            self.NUM_COLS,
            self.PX_WIDTH,
            self.PX_HEIGHT,
            left=left,
            bottom=bottom,
            width=self.PX_WIDTH // self.NUM_COLS,
            height=self.PX_HEIGHT // self.NUM_ROWS,
            **kwargs
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
