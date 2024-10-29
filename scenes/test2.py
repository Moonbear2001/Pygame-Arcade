import pygame

from .scene import Scene

class Test2(Scene):

    name = "test2"
    
    def __init__(self):
        """
        Initialize a new scene.
        """
        super().__init__()

    def on_update(self, delta_time):
        pass

    def on_render(self):
        self.canvas.fill("gray")

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                print("j")

    def on_enter(self):
        print("test 2 ON ENTER")

    def on_cleanup(self):
        print("test 2 ON CLEANUP")




