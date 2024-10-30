import pygame


class Parallax:
    """
    Parallax background.
    Expects a file with images 1-n where 1 is the furthest in the back and n is in the foreground.
    """

    def __init__(self, screen, folder):
        self.screen = screen
        # sel
