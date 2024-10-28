import pygame
from states import State

from sprite.sprites import Button
from utilities import render_text
from managers import AudioManager


class Settings(State):
    """
    Settings menu.
    """

    def __init__(self):
        super().__init__()
        self.name = "settings"

        self.canvas_width = 640
        self.canvas_height = 360
        self.canvas = pygame.Surface((self.canvas_width, self.canvas_height))

        self.music_vol_up_btn = Button(self.canvas_width * 0.41, self.canvas_height * 1/3, 200, 100, center_coords=True, bg_color="black", text="Music Volume Up", text_color="white", callback=lambda: AudioManager().increase_music_volume(0.1))

        self.music_vol_down_btn = Button(self.canvas_width * 0.59, self.canvas_height * 1/3, 200, 100, center_coords=True, bg_color="black", text="Music Volume Down", text_color="white", callback=lambda: AudioManager().decrease_music_volume(0.1))

        self.sounds_vol_up_btn = Button(self.canvas_width * 0.41, self.canvas_height * 1/2, 200, 100, center_coords=True, bg_color="black", text="Sounds Volume Up", text_color="white", callback=lambda: AudioManager().increase_music_volume(0.1))

        self.sounds_vol_down_btn = Button(self.canvas_width * 0.59, self.canvas_height * 1/2, 200, 100, center_coords=True, bg_color="black", text="Sounds Volume Down", text_color="white", callback=lambda: AudioManager().decrease_music_volume(0.1))

    def update(self, delta_time):
        pass

    def handle_event(self, event):
        self.music_vol_up_btn.handle_event(event)
        self.music_vol_down_btn.handle_event(event)
        self.sounds_vol_up_btn.handle_event(event)
        self.sounds_vol_down_btn.handle_event(event)


    def render(self):
        self.canvas.fill("yellow")
        render_text(self.canvas, "Settings", "roboto", "black", coord=(self.canvas_width * 0.5, self.canvas_height * 0.2), size=30)
        self.canvas.blit(self.music_vol_up_btn.render(), self.music_vol_up_btn.rect)
        self.canvas.blit(self.music_vol_down_btn.render(), self.music_vol_down_btn.rect)
        self.canvas.blit(self.sounds_vol_up_btn.render(), self.sounds_vol_up_btn.rect)
        self.canvas.blit(self.sounds_vol_down_btn.render(), self.sounds_vol_down_btn.rect)
        return self.canvas