import pygame

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from .scene import Scene


class ViewportScene(Scene):
    def __init__(
        self,
        target,
        viewport_width=CANVAS_WIDTH,
        viewport_height=CANVAS_HEIGHT,
        world_width=CANVAS_WIDTH,
        world_height=CANVAS_HEIGHT,
        **kwargs
    ):
        """
        Initializes the ViewportScene.

        Parameters:
        - target: The object the viewport centers on, typically the player.
        - viewport_width, viewport_height: Dimensions of the viewport window.
        - world_width, world_height: Dimensions of the entire world/canvas.
        """
        super().__init__(width=world_width, height=world_height, **kwargs)
        self.viewport = pygame.Rect(0, 0, viewport_width, viewport_height)
        self.target = target

    def _on_update(self, delta_time):
        """
        Updates the viewport position based on the target's position.
        """
        self.viewport.center = self.target.center
        self.target.clamp_ip(self.rect)
        self.viewport = self.target

    def render(self) -> pygame.Surface:
        """
        Renders only the section of the scene within the viewport.
        """

        if self.active:
            self._on_render()
            for child in self.children:
                if child.active:
                    self.canvas.blit(child.render(), child.rect)
            self._render_after_children()

            # Create a new surface for the viewport view
            viewport_surface = pygame.Surface(
                (self.viewport.width, self.viewport.height)
            ).convert_alpha()

            # Blit the viewport section from the full canvas
            viewport_surface.blit(self.canvas, (0, 0), area=self.viewport)

            if self.scale != 1:
                return pygame.transform.scale_by(viewport_surface, self.scale)
            return viewport_surface
