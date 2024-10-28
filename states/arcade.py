import pygame
from pygame.locals import MOUSEBUTTONDOWN

from states import State
from sprite.sprites import ArcadeMachine

from utilities import render_text
from managers import StateManager, AudioManager


class Arcade(State):
    """
    Arcade room with all of the arcade machines.
    """

    def __init__(self):
        super().__init__()
        self.name = "arcade"
        self.arcade_machines = [
            ArcadeMachine("pong"),
            ArcadeMachine("out_of_order"),
            ArcadeMachine("out_of_order")
        ]
        self.current_game_index = 0
        
    def enter(self):
        # AudioManager().play_music("arcade_music/1.mp3", loops=-1)
        AudioManager().play_playlist("arcade_music")

    def update(self, delta_time):
        super().update(delta_time)
        for arcade_machine in self.arcade_machines:
            arcade_machine.update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)
        for arcade_machine in self.arcade_machines:
            arcade_machine.handle_event(event)

        # Controls for selecting game to play
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.go_left()
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.go_right()
            if event.key == pygame.K_e or event.key == pygame.K_RETURN:
                self.enter_game()

    def render(self):
        self.canvas.fill("pink")
        left = 0
        for arcade_machine in self.arcade_machines:
            pos_rect = arcade_machine.rect
            # pos_rect.bottom = 720
            pos_rect.left = left
            self.canvas.blit(arcade_machine.render(), pos_rect)
            left += 300
        return self.canvas

    def go_left(self):
        """
        Move one game selection to the left.
        """
        if len(self.arcade_machines) > self.current_game_index + 1:
            self.current_game_index += 1


    def go_right(self):
        """
        Move one game selection to the right.
        """
        if self.current_game_index - 1 >= 0 :
            self.current_game_index -= 1

    def enter_game(self):
        """
        Enter and play the selected game.
        """
        print(self.arcade_machines[self.current_game_index].game_name)
        StateManager().push_state(self.arcade_machines[self.current_game_index].game_name)
