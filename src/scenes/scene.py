import pygame
from abc import ABC
from managers import EventManager


class Scene(ABC):
    """
    A scene that can contain other nested scenes.
    A scene is responsible for passing events, updating, and drawing each of its
    components onto its own Surface, which it returns to either the parent Scene or if
    it is the top level Scene returns up to the SceneManager.
    """

    def __init__(self, watched_events=set(), left=0, top=0, width=1280, height=720):
        """
        Initializes a new scene.
        """
        super().__init__()
        self.rect = pygame.Rect(left, top, width, height)
        self.canvas = pygame.Surface((width, height), pygame.SRCALPHA)
        self.children = []
        self.sprites = pygame.sprite.Group()
        self.active = False
        self.watched_events = watched_events

    # UPDATING

    def update(self, delta_time):
        """
        Updates the scene, all child scenes, and all child sprites.
        """
        if self.active:
            self._on_update(delta_time)
            for child in self.children:
                if child.active:
                    child.update(delta_time)
            self.sprites.update(delta_time)

    def _on_update(self, delta_time):
        """
        Updates specifically for the current scene.
        """
        pass

    # RENDERING

    def render(self) -> pygame.Surface:
        """
        Render the scene, all child scenes, and all child sprites.
        """
        if self.active:
            self._on_render()
            for child in self.children:
                if child.active:
                    self.canvas.blit(child.render(), child.rect)
            self.sprites.draw(self.canvas)
            return self.canvas

    def _on_render(self):
        """
        Rendering specifically for the current scene.
        """
        pass

    # EVENTS

    def handle_events(self, event):
        """
        Subscribed event handing, controls blocking event handling in superclass if
        the scene is inactive.
        """
        if self.active:
            self._on_event(event)

    def _on_event(self, event):
        """
        Subscribed event handling in subclasses.
        """
        pass

    # ENTERING AND LEAVING SCENE

    def enter(self):
        """
        Set things up before the scene is entered.
        """
        EventManager().subscribe(self.watched_events, self.handle_events)
        self.active = True
        self._on_enter()

    def _on_enter(self):
        pass

    def reenter(self):
        """
        Set things up when the scene is re-entered.
        """
        EventManager().subscribe(self.watched_events, self.handle_events)
        self.active = True
        self._on_reenter()

    def _on_reenter(self):
        pass

    def cleanup(self):
        """
        Clean up resources, save, unsubscribe from events, etc.
        Called by the scene manager before exiting this scene.
        """
        self.active = False
        EventManager().unsubscribe(self.watched_events, self.handle_events)
        self._on_cleanup()
        for child in self.children:
            child.cleanup()

    def _on_cleanup(self):
        pass

    # CHILD SCENE MANAGEMENT

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

    # SPRITE MANAGEMENT

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
