import pygame

from states.state import State
import Game
from managers import SaveLoadManager

class Clicker(State):
    """
    Simple clicker game in which the player just tries to beat the high score number of clicks.
    """

    def __init__(self, game):
        super().__init__(game)
        self.name = "Clicker"
        self.player = pygame.Rect(0, 0, 50, 50)
        self.score = 0
        self.saved_data = SaveLoadManager().load_data("clicker")
        self.high_score = self.saved_data["high_score"]

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.score += 1

    def render(self):
        self.game.canvas.fill("white")
        self.game.render_text(self.game.canvas, "The high score is: " + str(self.high_score), "roboto", "blue",
                              Game.canvas_width / 2, self.game.Game.canvas_height * 0.9, size=30)
        self.game.render_text(self.game.canvas, str(self.score), "roboto", "black",
                              Game.canvas_width / 2, self.game.Game.canvas_height / 2, size=60)
        super().render()

    def exit_state(self):
        """
        Save new high score if acheived before exiting.
        """
        self.high_score = max(self.high_score, self.score)
        self.saved_data["high_score"] = self.high_score
        SaveLoadManager().save_data(self.saved_data, "clicker")
        super().exit_state()
