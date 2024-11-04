import pygame
from abc import ABC

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from managers import EventManager


class Scene(ABC):
    """
    A scene is an object with the ability to handle events, update, and render. Scenes
    can nest within one another, and when a scene renders it passes its surface up its
    parent scene. The parent scene is then responsible for using its child's positioning
    rect to blit the child onto its own surface.

    A scene then also functions as a node in a graph. The top-level scene updates and
    renders its children, which in turn do the same, etc.

    Scenes subscribe to events via the EventManager. Events are not passed from the top
    of the scene graph down to each child. Each scene is responsible for subscribing to
    the events it wants to handle. This prevents scenes from ever receiving events they
    do not care about.
    """

    def __init__(
        self,
        left=0,
        top=0,
        right=0,
        bottom=0,
        width=CANVAS_WIDTH,
        height=CANVAS_HEIGHT,
        watched_events=None,
        scale=1,
    ):
        """
        Initializes a new scene.
        """
        super().__init__()
        self.scale = scale
        self.canvas = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        self.rect = pygame.Rect(left, top, width * scale, height * scale)
        if right != 0:
            self.rect.right = right
        if bottom != 0:
            self.rect.bottom = bottom
        self.children = []
        self.active = False
        self.watched_events = watched_events if watched_events is not None else set()

    # UPDATING

    def update(self, delta_time):
        """
        Updates the scene and all child scenes.
        """
        if self.active:
            self._on_update(delta_time)
            for child in self.children:
                if child.active:
                    child.update(delta_time)

    def _on_update(self, delta_time):
        """
        Updates specifically for the current scene.
        """
        pass

    # RENDERING

    def render(self) -> pygame.Surface:
        """
        Render the scene and all child scenes.
        """
        if self.active:
            self._render_before_children()
            for child in self.children:
                if child.active:
                    self.canvas.blit(child.render(), child.rect)
            self._render_after_children()
            if self.scale != 1:
                return pygame.transform.scale_by(self.canvas, self.scale)
            return self.canvas

    def _render_before_children(self):
        """
        Render certain elements before this scene's children.
        """
        pass

    def _render_after_children(self):
        """
        Render certain elements after this scene's children.
        """
        pass

    # EVENTS

    def handle_events(self, event):
        """
        Receives events the scene has subscribed to.

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
        for child in self.children:
            child.enter()
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

    def leave(self):
        """
        Clean up resources, save, unsubscribe from events, etc.
        Called by the scene manager before exiting this scene.
        """
        self.active = False
        EventManager().unsubscribe(self.watched_events, self.handle_events)
        self._on_leave()
        for child in self.children:
            child.leave()

    def _on_leave(self):
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
