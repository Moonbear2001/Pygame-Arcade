import pygame
from pygame.locals import MOUSEBUTTONDOWN

# from states import State, ParallaxExample, Clicker, Platformer
from states import State
# from states.parallax_example import ParallaxExample
from sprite.sprites import Button

from utilities import render_text
from managers import StateManager


class Title(State):
    """
    Title page with buttons leading to differente examples.
    """

    def __init__(self):
        super().__init__()
        self.name = "title"
        self.clicker_btn = Button(x=self.canvas_width * 0.1, y=self.canvas_width//2, width=200, height=100, text="Clicker", text_color=(0, 0, 255), callback=lambda: StateManager().set_state("clicker"))
        self.platformer_btn = Button(x=self.canvas_width * 0.4, y=self.canvas_width//2, width=200, height=100, text="Platformer", text_color=(0, 0, 255), callback=lambda: StateManager().set_state("platformer"))
        self.parallax_btn = Button(x=self.canvas_width * 0.7, y=self.canvas_width//2, width=200, height=100, text="Parallax Example", text_color=(0, 0, 255), callback=lambda: StateManager().set_state("parallax_example"))

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)
        self.clicker_btn.handle_event(event)
        self.platformer_btn.handle_event(event)
        self.parallax_btn.handle_event(event)

    def render(self):
        self.canvas.fill("gray")
        render_text(self.canvas, "Title screen", "roboto",  "blue", self.canvas_width / 2, self.canvas_height * 0.25, size=40)
        self.canvas.blit(self.clicker_btn.render(), self.clicker_btn.rect)
        self.canvas.blit(self.platformer_btn.render(), self.platformer_btn.rect)
        self.canvas.blit(self.parallax_btn.render(), self.parallax_btn.rect)
        return self.canvas
