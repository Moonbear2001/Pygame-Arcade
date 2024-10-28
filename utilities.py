import pygame
from pathlib import Path

from paths import FONTS_DIR

def render_text(surface, text, font_name, color, coord=None, size=10):
    """
    Utility function for rendering some text to a surface.

    'text' is rendered with parameters 'font_name', 'color', and 'size' and then drawn onto 'surface'. 'coord' is the draw location, if no coordinate is provided then the text is centered horizontally and vertically in the provided surface.
    """
    font_path = FONTS_DIR / (font_name + ".ttf")
    
    if not font_path.is_file():
        return  

    text_surface = pygame.font.Font(str(font_path), size).render(text, True, color)
    text_rect = text_surface.get_rect()

    # No drawing coordinate provided, draw in center of provided Surface
    if coord is None:
        text_rect.center = surface.get_rect().center
    else:
        text_rect.centerx = coord[0]
        text_rect.centery = coord[1]

    surface.blit(text_surface, text_rect)
