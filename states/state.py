import pygame
from abc import ABC, abstractmethod  
from utilities import render_text

class State(ABC):
    """
    A state that the game can be in (e.g., menu, paused, looking at map, gameplay).
    
    A state is responsible for passing events, updating, and drawing each of its components.
    The state manager is responsible for handling transitions between states.
    """

    def __init__(self):
        super().__init__()
        self.canvas_width = 1280
        self.canvas_height = 720
        self.canvas = pygame.Surface((self.canvas_width, self.canvas_height))

    @abstractmethod
    def update(self, delta_time):
        """
        Update the state. Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def render(self) -> pygame.Surface:
        """
        Render the state. Must be implemented by subclasses.
        Returns a pygame Surface.
        """
        pass

    def enter(self):
        """
        Courtesy location to set things up before state is entered.
        """
        pass

    def cleanup(self):
        """
        Courtesy location to clean up resources, save, etc.
        Called by the state manager before exiting out of this state.
        """
        pass

    def handle_event(self, event):
        """
        Handle individual events. Can be overridden by subclasses.
        """
        pass
