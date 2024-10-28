import pygame

from utilities import render_text

class Button(pygame.sprite.Sprite):
    """
    Customizable button that detects clicks and calls a function when clicked.
    """
    def __init__(self, x, y, width, height, center_coords: bool = True, bg_color: tuple = (0, 0, 0), text: str = "", font_name: str = "roboto", text_color: pygame.Color = "black", center_text=True, callback=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback

        if center_coords:
            self.rect.center = (x, y)

        # Render once here
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        if bg_color:
            self.surface.fill(bg_color)
        if text:
            render_text(self.surface, text, font_name, text_color)
        

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
