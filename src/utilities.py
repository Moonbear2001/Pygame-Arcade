import pygame
import textwrap

from paths import FONTS_DIR


def render_text(surface, text, font_name=None, color="white", coord=None, size=10):
    """
    Utility function for rendering some text to a surface.

    'text' is rendered with parameters 'font_name', 'color', and 'size' and then drawn
    onto 'surface'. 'coord' is the draw location, if no coordinate is provided then the
    text is centered horizontally and vertically in the provided surface.
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


def render_text_block(
    surface, text, font_name=None, color="white", padding_x=10, padding_y=10, coord=(0, 0), size=10
):
    """
    Render a block of text.
    Surface width is used to know how much space is available.
    Padding can be supplied from top and left of surface.
    """
    font_path = FONTS_DIR / (font_name + ".ttf")

    wrapper = textwrap.TextWrapper(
        width=65, replace_whitespace=False, drop_whitespace=False
    )
    wrapped_text = []
    split_lines = text.splitlines()
    # print(split_lines)
    for l in split_lines:
        if l:
            wrapped_text.extend(wrapper.wrap(l))
        else:
            wrapped_text.append(l)
    # print("wrapped text: ", wrapped_text)

    # wrapped_text = textwrap.wrap(text, 40)
    # wrapped_text = textwrap.wrap(text, surface.get_width() - 2 * padding)
    # print(wrapped_text)
    # font = pygame.font.Font(str(font_path), size)
    # req_width, req_height = font.size(text)

    blit_coord = list(coord)
    blit_coord[0] += padding_x
    blit_coord[1] += padding_y
    for line in wrapped_text:
        text_surface = pygame.font.Font(str(font_path), size).render(line, True, color)
        surface.blit(text_surface, blit_coord)
        blit_coord[1] += size


__all__ = ["render_text", "render_text_block"]
