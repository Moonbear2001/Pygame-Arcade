import pygame
from states.state import State
from states.clicker import Clicker
from states.platformer import Platformer
from visual_elems.Button import Button


class Title(State):

    def __init__(self, game):
        super().__init__(game)
        self.name = "Title"
        self.clicker_btn = Button(self, width=200, height=100, x=self.game.canvas_width * 0.35,
                                  y=self.game.canvas_width//2, text="Clicker", text_color=(0, 0, 255))
        self.platformer_btn = Button(self, width=200, height=100, x=self.game.canvas_width * 0.65,
                                     y=self.game.canvas_width//2, text="Platformer", text_color=(0, 0, 255))

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.locals.MOUSEBUTTONDOWN:
            if self.clicker_btn.rect.collidepoint(event.pos):       # Leads to clicker game
                Clicker(self.game).enter_state()
            if self.platformer_btn.rect.collidepoint(event.pos):    # Leads to platformer game
                Platformer(self.game).enter_state()

    def render(self):
        self.game.canvas.fill("white")
        self.game.render_text(self.game.canvas, "Title screen", "roboto",  "blue",
                              self.game.canvas_width / 2, self.game.canvas_height * 0.25, size=40)
        self.clicker_btn.render()
        self.platformer_btn.render()
        super().render()
