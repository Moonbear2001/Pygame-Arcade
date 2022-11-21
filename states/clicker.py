import pygame
import os
from states.state import State


class ClickGameplay(State):

    def __init__(self, game):
        super().__init__(game)
        self.player = pygame.Rect(0, 0, 50, 50)

    def update(self):
        super().update()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.game.score += 1

    def render(self):
        self.game.canvas.fill(self.game.colors["white"])
        # pygame.draw.rect(self.game.canvas, self.game.colors["blue"], self.player)
        self.game.render_text(self.game.canvas, str(self.game.score), self.game.colors["black"], self.game.canvas_width / 10, self.game.canvas_height / 10)
