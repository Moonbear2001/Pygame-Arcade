import pygame

from .scene import Scene
from managers import AudioManager
from paths import IMAGES_DIR

MOVE_SPEED = 100

class Arcade(Scene):
    """
    Arcade room with all of the arcade machines.
    """

    name = "arcade"
    
    def __init__(self):
        """
        Initialize a new scene.
        """
        super().__init__()
        self.window = pygame.Rect(0, 0, 1280, 720)
        self.arcade_img = pygame.image.load(IMAGES_DIR / "arcade.png")

    def on_enter(self):
        AudioManager().play_playlist("arcade_music")

    def on_update(self, delta_time):
        pass

    def on_render(self):
        self.canvas.blit(self.arcade_img, (0, 0), self.window)
        pygame.draw.rect(self.canvas, "black", (1600, 360, 360, 360))

    def on_event(self, event):

        # Controls for selecting game to play
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.window.move_ip(-1 * MOVE_SPEED, 0)
                self.go_left()
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.window.move_ip(MOVE_SPEED, 0)
                self.go_right()
            if event.key == pygame.K_e or event.key == pygame.K_RETURN:
                self.enter_game()

    def on_cleanup(self):
        pass

    def go_left(self):
        """
        Move one game selection to the left.
        """
        # if len(self.arcade_machines) > self.current_game_index + 1:
        #     self.current_game_index += 1
        print("go left")

    def go_right(self):
        """
        Move one game selection to the right.
        """
        # if self.current_game_index - 1 >= 0 :
        #     self.current_game_index -= 1
        print("go right")

    def enter_game(self):
        """
        Enter and play the selected game.
        """
        # print(self.arcade_machines[self.current_game_index].game_name)
        print("enter game")



