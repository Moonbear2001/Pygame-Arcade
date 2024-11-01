import pygame

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from .scene import Scene
from .viewport_scene import ViewportScene
from .arcade_machine import ArcadeMachine
from managers import AudioManager, SceneManager
from paths import IMAGES_DIR

MOVE_SPEED = 100


# Arcade machine positioning
STARTING_X = 1000
SPACING = 400


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
        super().__init__(self.target, world_width=2560, watched_events=self.custom_watched_events)

        # self.window = pygame.Rect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
        self.arcade_img = pygame.image.load(IMAGES_DIR / "arcade.png")

        game_names = [
            "pong",
            "out_of_order",
            "pong",
            "out_of_order",
            "pong",
            "out_of_order",
        ]

        self.arcade_machines = []
        posx = STARTING_X
        for game in game_names:
            self.arcade_machines.append(ArcadeMachine(game, left=posx, top=220))
            posx += SPACING

        for arcade_machine in self.arcade_machines:
            self.add_child(arcade_machine)

        # for arcade_machine in self.arcade_machines:
        #     #print(arcade_machine.rect)

    def _on_enter(self):
        # AudioManager().play_playlist("arcade_music")
        pass

    # def render(self) -> pygame.Surface:
    #     """
    #     Render the scene and all child scenes.
    #     """
    #     if self.active:
    #         self._on_render()
    #         for child in self.children:
    #             if child.active:
    #                 self.canvas.blit(child.render(), child.rect)
    #         if self.scale != 1:
    #             return pygame.transform.scale_by(self.canvas, self.scale)
    #         window_surf = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
    #         window_surf.blit(self.canvas, (0, 0), self.window)
    #         return window_surf

    def _on_render(self):
        self.canvas.blit(self.arcade_img, (0, 0))
        # pygame.draw.rect(self.canvas, "black", (1600, 360, 360, 360))

    def _on_event(self, event):

        if event.type == pygame.KEYDOWN:

            # Open settings
            if event.key == pygame.K_p:
                SceneManager().push_scene("settings")

            # Go to clicker
            elif event.key == pygame.K_c:
                SceneManager().push_scene("clicker")

            # Go to clicker
            elif event.key == pygame.K_l:
                SceneManager().push_scene("pong")

            # Movement
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.target.move_ip(-1 * MOVE_SPEED, 0)
                self.go_left()
                #print("Move right, self.target: ", self.target)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.target.move_ip(MOVE_SPEED, 0)
                self.go_right()
                #print("Move right, self.target: ", self.target)
            elif event.key == pygame.K_e or event.key == pygame.K_RETURN:
                self.enter_game()

    def go_left(self):
        """
        Move one game selection to the left.
        """
        # if len(self.arcade_machines) > self.current_game_index + 1:
        #     self.current_game_index += 1
        pass

    def go_right(self):
        """
        Move one game selection to the right.
        """
        # if self.current_game_index - 1 >= 0 :
        #     self.current_game_index -= 1
        pass

    def enter_game(self):
        """
        Enter and play the selected game.
        """
        # #print(self.arcade_machines[self.current_game_index].game_name)
        pass
