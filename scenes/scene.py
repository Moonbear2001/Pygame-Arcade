import pygame
from abc import ABC, abstractmethod  
from utilities import render_text

class Scene(ABC):
    """
    A scene that can contain other nested scenes.
    A scene is responsible for passing events, updating, and drawing each of its components onto its own Surface, which it returns to either the parent Scene or if it is the top level Scene returns up to the SceneManager.
    """

    def __init__(self, left, top, width, height):
        """
        Initialize a new scene.
        """
        super().__init__()
        self.rect = pygame.Rect(left, top, width, height)
        self.canvas = pygame.Surface((width, height))
        self.children = []
        self.sprites = pygame.sprite.Group()
        self.active = False

    ### UPDATING ###

    def update(self, delta_time):
        """
        Update the scene, all child scenes, and all child sprites.
        """
        if self.active:
            self.on_update()
            for child in self.children:
                if child.active:
                  child.update(delta_time)
            self.sprites.update(delta_time)

    def on_update(self, delta_time):
        """
        Updates specifically for the current scene.
        """
        pass
    
    ### RENDERING ###

    def render(self) -> pygame.Surface:
        """
        Render the scene, all child scenes, and all child sprites.
        """
        if self.active:
            self.on_render()
            for child in self.children:
                if child.active:
                    self.canvas.blit(child.canvas, child.rect)
            self.sprites.render(self.canvas)

    def on_render(self):
        """
        Rendering specifically for the current scene.
        """
        pass

    ### EVENTS ###

    def handle_event(self, event):
        """
        Handle individual events. Can be overridden by subclasses.
        """
        if self.active:
            self.on_event(event)
            for child in self.children:
                if child.active:
                    child.handle_event(event)

    def on_event(self, event):
        pass

    ### ENTERING AND LEAVING SCENE ###

    def enter(self):
        """
        Set things up before the scene is entered.
        """
        self.active = True
        self.on_enter()

    def on_enter(self):
        pass

    def cleanup(self):
        """
        Clean up resources, save, etc. 
        Called by the scene manager before exiting this scene.
        """
        self.on_cleanup()
        for child in self.children:
            child.cleanup()

    def on_cleanup(self):
        pass

    ### CHILD MANAGEMENT ###

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








