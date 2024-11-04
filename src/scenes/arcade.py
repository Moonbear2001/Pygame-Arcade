import pygame

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from .lamp import Lamp
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

MOVE_SPEED = 100


# Arcade machine positioning
STARTING_X = 1200
SPACING = 275

FOCUS_RECT_Y = 300

GROUND_PX_HEIGHT = 130 * 5

GAME_NAMES = [
    "pong",
    "clicker",
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

        self.focused_game = None
        self.focus_rect = pygame.Rect(0, 0, 400, 400)

        # Spawn arcade machines
        self.arcade_machines = []
        self.am_positions = []
        posx = STARTING_X
        for game in GAME_NAMES:
            self.am_positions.append(posx)
            arcade_machine = ArcadeMachine(posx, GROUND_PX_HEIGHT + 25, game, scale=0.3)
            self.arcade_machines.append(arcade_machine)
            posx += SPACING
            self.add_child(arcade_machine)

        # Visual elements
        self.add_child(Lamp(945, GROUND_PX_HEIGHT))
        self.add_child(Trash(525, GROUND_PX_HEIGHT))
        self.add_child(PythonLogo(655, 430))  # 131, 86
        self.add_child(PygameSnake(655, 225))  # 131, 45
        self.add_child(ArcadeSign(25, 95))  # 5, 19
        self.add_child(ExitSign(90, 245))  # 18, 49
        self.add_child(Cityscape(900, 30))  # 180, 6
        self.add_child(Cityscape(1295, 30))  # 260, 6
        self.add_child(Cityscape(1490, 30))
        self.add_child(Cityscape(1895, 30))
        # self.add_child(Cityscape(2300, 30))

    def _on_enter(self):
        # AudioManager().play_playlist("arcade_music")
        pass

    def _render_before_children(self):
        self.canvas.blit(self.arcade_img, (0, 0))

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
            # elif event.key == pygame.K_e or event.key == pygame.K_RETURN:
            #     self.enter_game()
            print("focused game: ", self.focused_game)

    def focus_left(self):
        """
        Move one game selection to the left.
        """
        if self.focused_game is not None:
            if self.focused_game == 0:
                self.arcade_machines[self.focused_game].focused = False
                self.focused_game = None
            elif self.focused_game > 0:
                self.arcade_machines[self.focused_game].focused = False
                self.focused_game -= 1
                self.arcade_machines[self.focused_game].focused = True

    def focus_right(self):
        """
        Move one game selection to the right.
        """
        if self.focused_game is None:
            self.focused_game = 0
            self.arcade_machines[self.focused_game].focused = True
        elif self.focused_game < len(self.arcade_machines) - 1:
            self.arcade_machines[self.focused_game].focused = False
            self.focused_game += 1
            self.arcade_machines[self.focused_game].focused = True
            

    def enter_game(self):
        """
        Enter and play the selected game.
        """
        pass
