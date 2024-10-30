import pygame
from pathlib import Path

from paths import PARALLAX_DIR


class ParallaxBackground(pygame.sprite.Sprite):
    """
    Parallax background that is essentially a sprite.
    Reads from a directory where images are labeled 1-n. 1 is drawn first (background) and n is drawn last (foreground).
    """

    def __init__(self, folder_name, speed=1):
        super().__init__()
        self.canvas_width = 1280
        self.canvas_height = 720
        self.canvas = pygame.Surface((self.canvas_width, self.canvas_height))
        self.speed = speed
        self.layers = self.load_layers(folder_name)

    def load_layers(self, folder_name: Path):
        """
        Load the layers from the provided directory.
        """
        layers = []
        folder_path = PARALLAX_DIR / folder_name
        files = sorted(folder_path.iterdir(), key=lambda x: int(x.stem))
        for i, file_path in enumerate(files):

            # Only load files
            if file_path.is_file():
                layer_image = pygame.image.load(file_path).convert_alpha()

                # TODO: layers are forced to scale, might have a layer that is narrower and needs to repeat more
                layer_image = pygame.transform.scale(
                    layer_image, (self.canvas_width, self.canvas_height)
                )

                # TODO: find a better way to manage speed
                layer_speed = self.speed / (i + 1)

                layers.append({"image": layer_image, "x": 0, "speed": layer_speed})
        return layers

    def update(self, delta_time):
        """
        Move each layer left or right.
        """
        for layer in self.layers:
            layer["x"] -= layer["speed"]
            if layer["x"] <= -self.canvas_width:
                layer["x"] = 0

    def draw(self, surface):
        """
        Draw from background to foreground.
        """
        for layer in self.layers:
            surface.blit(layer["image"], (layer["x"], 0))
            surface.blit(layer["image"], (layer["x"] + self.canvas_width, 0))
