import pygame
from pathlib import Path

from paths import FONTS_DIR

def render_text(surface, text, font_name, color, x, y, size=10, center=True):
    """
    Utility function for rendering some text to a surface.
    """
    font_path = FONTS_DIR / (font_name + ".ttf")
    
    if not font_path.is_file():
        return  

    text_surface = pygame.font.Font(str(font_path), size).render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.x = x
        text_rect.y = y
    surface.blit(text_surface, text_rect)
