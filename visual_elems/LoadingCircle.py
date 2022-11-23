import pygame
from visual_elems.VisualElement import VisualElement


class LoadingCircle(VisualElement):

    def __init__(self, state, x: int = 0, y: int = 0, width: int = 100, height: int = 100, center=False):
        super().__init__(state, x, y, width, height, center)
        self.circle_radius = width/20
        self.left_center = (self.rect.x + width/4, self.rect.top + height / 2)
        self.middle_center = (self.rect.x + width/2, self.rect.top + height / 2)
        self.right_center = (self.rect.x + width*(3/4), self.rect.top + height / 2)
        self.left_alpha = 0
        self.middle_alpha = 0.5
        self.right_alpha = 1

    def update(self):
        self.left_alpha = (self.left_alpha + 0.001) % 1
        self.middle_alpha = (self.middle_alpha + 0.001) % 1
        self.right_alpha = (self.right_alpha + 0.001) % 1

    def render(self):
        pygame.draw.circle(self.state.game.canvas, (0, 0, 0, self.left_alpha), self.left_center, self.circle_radius)
        pygame.draw.circle(self.state.game.canvas, (0, 0, 0, self.middle_alpha), self.middle_center, self.circle_radius)
        pygame.draw.circle(self.state.game.canvas, (0, 0, 0, self.right_alpha), self.right_center, self.circle_radius)

