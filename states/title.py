import pygame

# from states import State, ParallaxExample, Clicker, Platformer
from states.state import State
from states.clicker import Clicker
from states.platformer import Platformer
# from states.parallax_example import ParallaxExample
from visual_elems.Button import Button

from utilities import render_text
from managers import StateManager


class Title(State):

    def __init__(self):
        super().__init__()
        self.name = "title"
        # self.clicker_btn = Button(self, width=200, height=100, x=self.canvas_width * 0.35,
        #                           y=self.canvas_width//2, text="Clicker", text_color=(0, 0, 255))
        # self.platformer_btn = Button(self, width=200, height=100, x=self.canvas_width * 0.65,
        #                              y=self.canvas_width//2, text="Platformer", text_color=(0, 0, 255))
        # self.parallax_btn = Button(self, width=200, height=100, x=self.canvas_width * 0.65,
        #                              y=self.canvas_width//2, text="Parallax Example", text_color=(0, 0, 255))

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)
        # if event.type == pygame.locals.MOUSEBUTTONDOWN:
        #     if self.clicker_btn.rect.collidepoint(event.pos):
        #         StateManager().set_state("clicker")
        #     if self.platformer_btn.rect.collidepoint(event.pos):    
        #         StateManager().set_state("platformer")
            # if self.platformer_btn.rect.collidepoint(event.pos):    
            #     ParallaxExample(self.game).enter_state()

    def render(self):
        self.canvas.fill("white")
        render_text(self.canvas, "Title screen", "roboto",  "blue",
                              self.canvas_width / 2, self.canvas_height * 0.25, size=40)
        # self.clicker_btn.render()
        # self.platformer_btn.render()
        return self.canvas
