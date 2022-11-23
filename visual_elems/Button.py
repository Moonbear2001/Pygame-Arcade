import pygame
from visual_elems.VisualElement import VisualElement
from states.state import State


class Button(VisualElement):

    def __init__(self, state, x: int = 0, y: int = 0, width: int = 100, height: int = 100,
                 color: tuple = (0, 0, 0), text: str = "", font: pygame.font = None,
                 text_color: tuple = (0, 0, 0)):
        super().__init__(state, x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.pressed = False
        self.rect.center = (x, y)

    def render(self):
        pygame.draw.rect(self.state.game.canvas, self.color, self.rect)

        if self.text != "":
            self.state.game.render_text(self.state.game.canvas, self.text, "roboto", self.text_color, self.rect.centerx,
                                        self.rect.centery)
