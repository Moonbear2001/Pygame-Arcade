import pygame
from .anim_scene import AnimScene
from paths import SPRITESHEETS_DIR

BUTTON_SPRITESHEETS = SPRITESHEETS_DIR / "buttons"

class AnimButton(AnimScene):
    """
    An animatable button class that combines animation functionality with button interaction.
    """

    custom_watched_events = {pygame.MOUSEBUTTONDOWN}

    def __init__(self, callback, **kwargs):
        super().__init__(watched_events=self.custom_watched_events, **kwargs)
        # self.hovered = False
        self.click = False
        self.callback = callback

    def _on_event(self, event):
        """
        Check for click events on the button.
        """
        # if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
        #     print("hovered")
        #     self.hovered = True
        #     if event.button == 1:
        #         print("clicked")
        #         self.clicked = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.click = True

    def _on_update(self, delta_time):
        """
        Updates the animation and hover state, calls the callback func if clicked.
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if self.click:
                self.play_animation("clicked")
                self.callback()
            else:
                self.play_animation("hovered")
        else:
            self.play_animation("idle")
        self.click = False
        # if self.clicked:
        #     self.play_animation("clicked")
        #     if self.callback:
        #         self.callback()
        # elif self.hovered:
        #     self.play_animation("hovered")
        super()._on_update(delta_time)