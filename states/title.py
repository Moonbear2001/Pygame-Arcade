import pygame
from pygame.locals import MOUSEBUTTONDOWN

from states import State
from sprite.sprites import Button

from utilities import render_text
from managers import StateManager, AudioManager


class Title(State):
    """
    Title page with buttons leading to differente examples.
    """

    def __init__(self):
        super().__init__()
        self.name = "title"
        self.clicker_btn = Button(self.canvas_width * 0.1, self.canvas_width//2, 200, 100, bg_color="black", text="Clicker", text_color="white", callback=lambda: StateManager().set_state("clicker"), center_text=True)
        
        self.platformer_btn = Button(self.canvas_width * 0.3, self.canvas_width//2, 200, 100, bg_color="black", text="Platformer", text_color="blue", callback=lambda: StateManager().set_state("platformer"))
        
        self.parallax_btn = Button(self.canvas_width * 0.5, self.canvas_width//2, 200, 100, bg_color="black", text="Parallax Example", text_color=(0, 0, 255), callback=lambda: StateManager().set_state("parallax_example"))
        
        self.arcade_btn = Button(self.canvas_width * 0.7, self.canvas_width//2, 200, 100, bg_color="black", text="arcade", text_color=(0, 255, 255), callback=lambda: StateManager().set_state("arcade"))

        self.canvas.fill("gray")
        render_text(self.canvas, "Title screen", "roboto",  "blue", size=40)
        self.canvas.blit(self.clicker_btn.render(), self.clicker_btn.rect)
        self.canvas.blit(self.platformer_btn.render(), self.platformer_btn.rect)
        self.canvas.blit(self.parallax_btn.render(), self.parallax_btn.rect)
        self.canvas.blit(self.arcade_btn.render(), self.arcade_btn.rect)

    def enter(self):
        # AudioManager().play_music("arcade_music/1.mp3", loops=-1)
        pass

    def update(self, delta_time):
        pass

    def handle_event(self, event):
        self.clicker_btn.handle_event(event)
        self.platformer_btn.handle_event(event)
        self.parallax_btn.handle_event(event)
        self.arcade_btn.handle_event(event)

    def render(self):
        # self.canvas.fill("gray")
        # render_text(self.canvas, "Title screen", "roboto",  "blue", size=40)
        # self.canvas.blit(self.clicker_btn.render(), self.clicker_btn.rect)
        # self.canvas.blit(self.platformer_btn.render(), self.platformer_btn.rect)
        # self.canvas.blit(self.parallax_btn.render(), self.parallax_btn.rect)
        # self.canvas.blit(self.arcade_btn.render(), self.arcade_btn.rect)
        return self.canvas
