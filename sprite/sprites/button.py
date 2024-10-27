import pygame

from utilities import render_text

class Button(pygame.sprite.Sprite):
    """
    Button that detects clicks and calls a function when clicked.
    """
    def __init__(self, x: int = 0, y: int = 0, width: int = 100, height: int = 100,
                 color: tuple = (0, 0, 0), text: str = "", font_name: str = "roboto",
                 text_color: tuple = (0, 0, 0), callback=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font_name = font_name
        self.rect.center = (x, y)

        self.callback = callback

        self.surface = pygame.Surface((width, height))
        self.surface.fill(self.color)
        if self.text:
            render_text(self.surface, self.text, self.font_name, self.text_color, self.rect.centerx, self.rect.centery)

    def update(self):
        pass

    def render(self):
        return self.surface

    def is_hovered(self, mouse_pos):
        """
        Check if the button is hovered over.
        """
        return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        """
        Call the callback function when clicked.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered(event.pos):
                if self.callback:
                    self.callback()
