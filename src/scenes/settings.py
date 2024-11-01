import pygame

from .scene import Scene
from paths import IMAGES_DIR
from managers import SceneManager


class Settings(Scene):
    """
    Settings.
    """

    name = "settings"
    custom_watched_events = {pygame.KEYDOWN}

    def __init__(self):
        super().__init__(watched_events=self.custom_watched_events)
        self.settings_image = pygame.image.load(
            IMAGES_DIR / "settings.png"
        ).convert_alpha()
        # self.background = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT), pygame.SRCALPHA).convert_alpha()
        # self.background.fill((0, 0, 0, 1))

    def _on_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            SceneManager().pop_scene()

    def _on_render(self):
        # self.canvas.blit(self.background, (0, 0))
        self.canvas.blit(self.settings_image, (0, 0))
        return self.canvas

        # self.music_vol_up_btn = Button(
        #     self.canvas_width * 0.41,
        #     self.canvas_height * 1 / 3,
        #     200,
        #     100,
        #     center_coords=True,
        #     bg_color="black",
        #     text="Music Volume Up",
        #     text_color="white",
        #     callback=lambda: AudioManager().increase_music_volume(0.1),
        # )

        # self.music_vol_down_btn = Button(
        #     self.canvas_width * 0.59,
        #     self.canvas_height * 1 / 3,
        #     200,
        #     100,
        #     center_coords=True,
        #     bg_color="black",
        #     text="Music Volume Down",
        #     text_color="white",
        #     callback=lambda: AudioManager().decrease_music_volume(0.1),
        # )

        # self.sounds_vol_up_btn = Button(
        #     self.canvas_width * 0.41,
        #     self.canvas_height * 1 / 2,
        #     200,
        #     100,
        #     center_coords=True,
        #     bg_color="black",
        #     text="Sounds Volume Up",
        #     text_color="white",
        #     callback=lambda: AudioManager().increase_music_volume(0.1),
        # )

        # self.sounds_vol_down_btn = Button(
        #     self.canvas_width * 0.59,
        #     self.canvas_height * 1 / 2,
        #     200,
        #     100,
        #     center_coords=True,
        #     bg_color="black",
        #     text="Sounds Volume Down",
        #     text_color="white",
        #     callback=lambda: AudioManager().decrease_music_volume(0.1),
        # )
