import pygame
from states.state import State


class Clicker(State):
    """
    Simple clicker game in which the player just tries to beat the high score number of clicks.
    """

    def __init__(self, game):
        super().__init__(game)
        self.name = "Clicker"
        self.player = pygame.Rect(0, 0, 50, 50)
        self.score = 0
        self.high_score = self.game.saved_game_data.high_score

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.score += 1

    def render(self):
        self.game.canvas.fill("white")
        self.game.render_text(self.game.canvas, "The high score is: " + str(self.high_score), "roboto", "blue",
                              self.game.canvas_width / 2, self.game.canvas_height * 0.9, size=30)
        self.game.render_text(self.game.canvas, str(self.score), "roboto", "black",
                              self.game.canvas_width / 2, self.game.canvas_height / 2, size=60)
        super().render()

    def exit_state(self):
        self.game.saved_game_data.high_score = max(self.high_score, self.score)
        super().exit_state()
