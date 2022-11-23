import pygame


class VisualElement:

    def __init__(self, state, x: int = 0, y: int = 0, width: int = 100, height: int = 100, center=False):
        self.state = state
        self.surface = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        if center:
            self.rect.center = (x, y)

    def render(self):
        pass


