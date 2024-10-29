import pygame

from .scene import Scene

class Test(Scene):
    
    def __init__(self):
        """
        Initialize a new scene.
        """
        super().__init__()

    def update(self, delta_time):
        pass

    def render(self) -> pygame.Surface:
        
        return self.canvas

    def enter(self):
        """
        Set things up before the scene is entered.
        """
        self.active = True
        self.on_enter()

    def cleanup(self):
        """
        Clean up resources, save, etc. 
        Called by the scene manager before exiting this scene.
        """
        self.on_cleanup()
        for child in self.children:
            child.cleanup()

    def handle_event(self, event):
        """
        Handle individual events. Can be overridden by subclasses.
        """
        if self.active:
            self.on_event(event)
            for child in self.children:
                if child.active:
                    child.handle_event(event)

    def update_children(self, delta_time):
        """
        Update all child scenes.
        """
        if self.active:
          for child in self.children:
            if child.active:
                child.update(delta_time)

    # def render_children(self):
    #     """
    #     Render all child scenes.
    #     """
    #     if self.active:
    #       for child in self.children:
    #         if child.active:
    #             child.render(self.canvas)

    def add_child(self, scene):
        """
        Add a nested scene.
        """
        self.children.append(scene)

    def remove_child(self, scene):
        """
        Remove a nested scene.
        """
        if scene in self.children:
            self.children.remove(scene)

    def on_enter(self):
        pass

    def on_cleanup(self):
        pass

    def on_event(self, event):
        pass

    def on_update(self, delta_time):
        pass

    def on_render(self, surface):
        pass
