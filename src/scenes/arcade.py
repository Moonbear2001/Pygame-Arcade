import pygame

from .scene import Scene
from .arcade_machine import ArcadeMachine
from managers import AudioManager, SceneManager
from paths import IMAGES_DIR

MOVE_SPEED = 100


class Arcade(Scene):
    """
    Arcade room with all of the arcade machines.
    """

    name = "arcade"
    custom_watched_events = {pygame.KEYDOWN}

    def __init__(self):
        """
        Initialize a new scene.
        """
        super().__init__(watched_events=self.custom_watched_events)
        self.window = pygame.Rect(0, 0, 1280, 720)
        self.arcade_img = pygame.image.load(IMAGES_DIR / "arcade.png")

        self.add_child(ArcadeMachine())

    def _on_enter(self):
        AudioManager().play_playlist("arcade_music")

    def _on_update(self, delta_time):
        pass

    def _on_render(self):
        self.canvas.blit(self.arcade_img, (0, 0), self.window)
        pygame.draw.rect(self.canvas, "black", (1600, 360, 360, 360))

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
                self.window.move_ip(-1 * MOVE_SPEED, 0)
                self.go_left()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.window.move_ip(MOVE_SPEED, 0)
                self.go_right()
            elif event.key == pygame.K_e or event.key == pygame.K_RETURN:
                self.enter_game()

    def _on_leave(self):
        pass

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
        # print(self.arcade_machines[self.current_game_index].game_name)
        pass
