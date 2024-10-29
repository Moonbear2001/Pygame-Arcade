import pygame

from .scene import Scene
from .test2 import Test2
from sprite.sprites import Player

class Test(Scene):

    name = "test"
    
    def __init__(self):
        """
        Initialize a new scene.
        """
        super().__init__()

        self.add_child(Test2())
        self.add_sprite(Player())

    def on_update(self, delta_time):
        pass

    def on_render(self):
        self.canvas.fill("green")

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("enter")

    def on_enter(self):
        print("test ON ENTER")

    def on_cleanup(self):
        print("test ON CLEANUP")




