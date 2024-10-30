import pygame
from abc import ABC, abstractmethod
from utilities import render_text


class Scene(ABC):
    """
    A scene that can contain other nested scenes.
    A scene is responsible for passing events, updating, and drawing each of its components onto its own Surface, which it returns to either the parent Scene or if it is the top level Scene returns up to the SceneManager.
    """

    def __init__(self, left=0, top=0, width=1280, height=720):
        """
        Initialize a new scene.
        """
        super().__init__()
        self.rect = pygame.Rect(left, top, width, height)
        self.canvas = pygame.Surface((width, height), pygame.SRCALPHA)
        self.children = []
        self.sprites = pygame.sprite.Group()
        self.active = True

    ### UPDATING ###

    def update(self, delta_time):
        """
        Update the scene, all child scenes, and all child sprites.
        """
        if self.active:
            self.on_update(delta_time)
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
                    self.canvas.blit(child.render(), child.rect)
            self.sprites.draw(self.canvas)
            return self.canvas

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
            for sprite in self.sprites:
                sprite.handle_event(event)

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

    ### CHILD SCENE MANAGEMENT ###

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

    ### SPRITE MANAGEMENT ###

    def add_sprite(self, sprite):
        """
        Add a nested scene.
        """
        self.sprites.add(sprite)

    def remove_add(self, sprite):
        """
        Remove a nested scene.
        """
        self.sprites.remove(sprite)
