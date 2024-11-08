import pygame
from pathlib import Path

from paths import PARALLAX_DIR
from .scene import Scene


class ParallaxScene(Scene):
    def __init__(
        self,
        folder_name,
        left,
        top,
        width,
        height,
        speed=1,
        static_layers=None,
        **kwargs
    ):
        """
        Layers specified in `static_layers` will be treated as static and will not
        scroll.
        """
        super().__init__(left=left, top=top, width=width, height=height, **kwargs)
        self.background_width = width
        self.background_height = height
        self.speed = speed
        self.static_layers = static_layers if static_layers else set()
        self.static_background = None
        self.static_foreground = None
        self.static_images = []
        self.layers = self.load_layers(folder_name)

    def load_layers(self, folder_name: Path):
        """
        Load the layers from the provided directory.
        """
        layers = []
        folder_path = PARALLAX_DIR / folder_name
        files = sorted(folder_path.iterdir(), key=lambda x: int(x.stem))

        # Load repeating static background (if "0.png" exists)
        static_bg_path = folder_path / "0.png"
        if static_bg_path.exists() and static_bg_path.is_file():
            self.static_background = pygame.image.load(static_bg_path).convert_alpha()

        # Load repeating static foreground (if "100.png" exists)
        static_fg_path = folder_path / "100.png"
        if static_fg_path.exists() and static_fg_path.is_file():
            self.static_foreground = pygame.image.load(static_fg_path).convert_alpha()

        # Load parallax layers (files named 1, 2, 3, ...)
        for i, file_path in enumerate(files):
            if file_path.is_file() and file_path.stem not in ["0", "100"]:
                layer_image = pygame.image.load(file_path).convert_alpha()
                layer_index = int(file_path.stem)

                if layer_index in self.static_layers:
                    # Add to static images if specified in static_layers
                    self.static_images.append(layer_image)
                else:
                    # Add to moving parallax layers
                    layer_speed = self.speed / (i + 1)
                    layers.append({"image": layer_image, "x": 0, "speed": layer_speed})

        return layers

    def _on_update(self, delta_time):
        """
        Updates the position of each parallax layer.
        """
        for layer in self.layers:
            layer["x"] -= layer["speed"]
            if layer["x"] <= -self.background_width:
                layer["x"] = 0

    def _render_before_children(self):
        """
        Draws the repeating static background (if present), each parallax layer, and the
        repeating static foreground (if present).
        """
        # Draw the repeating static background, if it exists
        if self.static_background:
            bg_width = self.static_background.get_width()
            for x in range(0, self.background_width, bg_width):
                self.canvas.blit(self.static_background, (x, 0))

        # Draw the static layers specified by `static_layers`
        for static_image in self.static_images:
            static_width = static_image.get_width()
            for x in range(0, self.background_width, static_width):
                self.canvas.blit(static_image, (x, 0))

        # Draw the parallax layers
        for layer in self.layers:
            for i in range(0, self.background_width, layer["image"].get_width()):
                self.canvas.blit(layer["image"], (layer["x"] + i, 0))
                self.canvas.blit(
                    layer["image"], (layer["x"] + i + self.background_width, 0)
                )

        # Draw the repeating static foreground, if it exists
        if self.static_foreground:
            fg_width = self.static_foreground.get_width()
            for x in range(0, self.background_width, fg_width):
                self.canvas.blit(self.static_foreground, (x, 0))
