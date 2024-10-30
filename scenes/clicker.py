import pygame

from .scene import Scene
from utilities import render_text
from managers import SaveLoadManager


class Clicker(Scene):
    """
    Simple clicker game in which the player just tries to beat the high score number of
    clicks.
    """

    name = "clicker"

    def __init__(self):
        """
        Initialize a new scene.
        """
        super().__init__()
        self.score = 0
        self.saved_data = SaveLoadManager().load_data("clicker")
        self.high_score = self.saved_data["high_score"]

    def on_update(self, delta_time):
        pass

    def on_render(self):
        self.canvas.fill("gray")
        render_text(
            self.canvas,
            "The high score is: " + str(self.high_score),
            "roboto",
            "blue",
            coord=(self.rect.width / 2, self.rect.height * 0.9),
            size=30,
        )
        render_text(
            self.canvas,
            str(self.score),
            "roboto",
            "black",
            coord=(self.rect.width / 2, self.rect.height / 2),
            size=60,
        )
        return self.canvas

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.score += 1

    def on_enter(self):
        pass

    def on_cleanup(self):
        """
        Save new high score if acheived before exiting.
        """
        self.high_score = max(self.high_score, self.score)
        self.saved_data["high_score"] = self.high_score
        SaveLoadManager().save_data(self.saved_data, "clicker")
