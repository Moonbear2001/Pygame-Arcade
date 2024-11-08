import pygame

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from .lamp import Lamp
from .lamp_light import LampLight
from .trash import Trash
from ..viewport_scene import ViewportScene
from .arcade_machine import ArcadeMachine
from .python_logo import PythonLogo
from .pygame_snake import PygameSnake
from .arcade_sign import ArcadeSign
from .exit_sign import ExitSign
from managers import AudioManager, SceneManager
from paths import IMAGES_DIR
from ..parallax_scene import ParallaxScene
from .info_screen import InfoScreen

MOVE_SPEED = 100


# Arcade machine positioning
STARTING_X = 1200
SPACING = 275

FOCUS_RECT_Y = 300

GROUND_PX_HEIGHT = 130 * 5

GAME_NAMES = [
    "pong",
    "clicker",
    "out_of_order",
    "tic_tac_toe",
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
        self.add_child(Lamp(850, GROUND_PX_HEIGHT + 10))
        self.add_child(LampLight(875, GROUND_PX_HEIGHT + 30))
        self.add_child(Lamp(2295, GROUND_PX_HEIGHT + 10))
        self.add_child(LampLight(2320, GROUND_PX_HEIGHT + 30))
        self.add_child(Trash(400, GROUND_PX_HEIGHT + 10))
        self.add_child(PythonLogo(655, 430))  # 131, 86
        self.add_child(PygameSnake(655, 225))  # 131, 45
        self.add_child(ArcadeSign(25, 70))  # 5, 19
        self.add_child(
            ParallaxScene(
                "skyline", 900, 30, 1618, 180, static_layers={0, 100, 2, 3, 4}
            )
        )

        exit_sign = ExitSign(90, 245)
        self.add_child(exit_sign)  # 18, 49
        self.focusable_items.append(exit_sign)

        info_screen = InfoScreen(335, 390)  # 67, 78
        self.add_child(info_screen)
        self.focusable_items.append(info_screen)
        info_screen.focused = True

        # Spawn arcade machines
        # self.arcade_machines = []
        self.am_positions = []
        posx = STARTING_X
        for game in GAME_NAMES:
            self.am_positions.append(posx)
            arcade_machine = ArcadeMachine(
                posx, GROUND_PX_HEIGHT + 25, game, scale=0.34
            )
            # self.arcade_machines.append(arcade_machine)
            posx += SPACING
            self.add_child(arcade_machine)
            self.focusable_items.append(arcade_machine)

    def _on_enter(self):
        AudioManager().play_playlist("arcade_music")

    def _render_before_children(self):
        self.canvas.blit(self.arcade_img, (0, 0))

    def _render_after_children(self):
        focused_item_rect = self.focusable_items[self.focused_item_index].rect
        pygame.draw.rect(self.canvas, "white", focused_item_rect, 5, 20)
        offset_y = 20
        offset_x = 10
        right_points = [
            (focused_item_rect.right + offset_x, focused_item_rect.centery + offset_y),
            (focused_item_rect.right + offset_x, focused_item_rect.centery - offset_y),
            (focused_item_rect.right + offset_x + 20, focused_item_rect.centery),
        ]
        left_points = [
            (focused_item_rect.left - offset_x, focused_item_rect.centery + offset_y),
            (focused_item_rect.left - offset_x, focused_item_rect.centery - offset_y),
            (focused_item_rect.left - offset_x - 20, focused_item_rect.centery),
        ]
        if self.focused_item_index != 0:
            pygame.draw.polygon(self.canvas, "white", left_points)
        if self.focused_item_index != len(self.focusable_items) - 1:
            pygame.draw.polygon(self.canvas, "white", right_points)
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
