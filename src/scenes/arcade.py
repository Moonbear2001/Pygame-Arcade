import pygame
from random import randint

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from .lamp import Lamp
from .lamp_light import LampLight
from .trash import Trash
from .cityscape import Cityscape
from .viewport_scene import ViewportScene
from .arcade_machine import ArcadeMachine
from .python_logo import PythonLogo
from .pygame_snake import PygameSnake
from .arcade_sign import ArcadeSign
from .exit_sign import ExitSign
from managers import AudioManager, SceneManager
from paths import IMAGES_DIR
from .parallax_scene import ParallaxScene
from .info_screen import InfoScreen

MOVE_SPEED = 100


# Arcade machine positioning
STARTING_X = 1200
SPACING_LOW = 200
SPACING_HIGH = 300

FOCUS_RECT_Y = 300

GROUND_PX_HEIGHT = 130 * 5

GAME_NAMES = [
    "pong",
    "clicker",
    "tic_tac_toe",
    "out_of_order",
    "out_of_order",
    "out_of_order",
]


class Arcade(ViewportScene):
    """
    Arcade room with all of the arcade machines.
    """

    name = "arcade"
    custom_watched_events = {pygame.KEYDOWN}
    target = pygame.Rect(0, CANVAS_WIDTH // 2, CANVAS_WIDTH, CANVAS_HEIGHT)

    def __init__(self):
        """
        Initialize a new scene.
        """
        super().__init__(
            self.target, world_width=2560, watched_events=self.custom_watched_events
        )

        self.arcade_img = pygame.image.load(IMAGES_DIR / "arcade.png")
        self.ropes_img = pygame.image.load(IMAGES_DIR / "ropes.png")

        self.focused_item_index = 1
        self.focusable_items = []

        # Visual elements in arcade
        self.add_child(Lamp(880, GROUND_PX_HEIGHT + 10))
        self.add_child(LampLight(830, 305))
        self.add_child(Trash(400, GROUND_PX_HEIGHT + 10))
        self.add_child(PythonLogo(655, 430))  # 131, 86
        self.add_child(PygameSnake(655, 225))  # 131, 45
        self.add_child(ArcadeSign(25, 95))  # 5, 19
        self.add_child(ParallaxScene("skyline", 900, 30, 1618, 180, static_layers={0, 100, 2, 3, 4}))

        exit_sign = ExitSign(90, 245)
        self.add_child(exit_sign)  # 18, 49
        self.focusable_items.append(exit_sign)

        info_screen = InfoScreen(335, 390) #67, 78
        self.add_child(info_screen)
        self.focusable_items.append(info_screen)

        # Spawn arcade machines
        # self.arcade_machines = []
        self.am_positions = []
        posx = STARTING_X
        for game in GAME_NAMES:
            self.am_positions.append(posx)
            arcade_machine = ArcadeMachine(posx, GROUND_PX_HEIGHT + 25, game, scale=0.34)
            # self.arcade_machines.append(arcade_machine)
            # posx += randint(SPACING_LOW, SPACING_HIGH)
            posx += 200
            self.add_child(arcade_machine)
            self.focusable_items.append(arcade_machine)

    def _on_enter(self):
        # AudioManager().play_playlist("arcade_music")
        pass

    def _render_before_children(self):
        self.canvas.blit(self.arcade_img, (0, 0))

    def _render_after_children(self):
        pygame.draw.rect(self.canvas, "white", self.focusable_items[self.focused_item_index].rect, 5)
        self.canvas.blit(self.ropes_img, (0, 0))

    def _on_event(self, event):

        if event.type == pygame.KEYDOWN:

            # Open settings
            if event.key == pygame.K_p:
                SceneManager().push_scene("settings")

            # Movement
            elif event.key == pygame.K_LEFT:
                self.target.move_ip(-1 * MOVE_SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                self.target.move_ip(MOVE_SPEED, 0)

            # Focusing
            elif event.key == pygame.K_a:
                self.focus_left()
            elif event.key == pygame.K_d:
                self.focus_right()

    def focus_left(self):
        """
        Move one game selection to the left.
        """
        # if self.focused_item_index is not None:
        #     if self.focused_item == 0:
        #         self.arcade_machines[self.focused_item].focused = False
        #         self.focused_item = None
        #     elif self.focused_item > 0:
        #         self.arcade_machines[self.focused_item].focused = False
        #         self.focused_item -= 1
        #         self.arcade_machines[self.focused_item].focused = True

        if self.focused_item_index != 0:
            self.focusable_items[self.focused_item_index].focused = False
            self.focused_item_index -= 1
            self.focusable_items[self.focused_item_index].focused = True


    def focus_right(self):
        """
        Move one game selection to the right.
        """
        # if self.focused_item is None:
        #     self.focused_item = 0
        #     self.arcade_machines[self.focused_item].focused = True
        # elif self.focused_item < len(self.arcade_machines) - 1:
            # self.arcade_machines[self.focused_item].focused = False
            # self.focused_item += 1
            # self.arcade_machines[self.focused_item].focused = True
        if self.focused_item_index != len(self.focusable_items) - 1:
            self.focusable_items[self.focused_item_index].focused = False
            self.focused_item_index += 1
            self.focusable_items[self.focused_item_index].focused = True