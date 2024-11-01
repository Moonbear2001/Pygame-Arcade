import pygame
from abc import ABC, abstractmethod

from constants import CANVAS_WIDTH, CANVAS_HEIGHT


class Transition(ABC):
    """
    A transition between two scenes.
    This is usually just some visual effect. If there is a transition taking place,
    the TransitionManager draws the visual effect on top of the current scene.
    """

    def __init__(self):
        """
        Next scene is the name of scene to go to after the transition is finished.
        """
        super().__init__()
        self.surface = pygame.Surface(
            (CANVAS_WIDTH, CANVAS_HEIGHT), pygame.SRCALPHA
        ).convert_alpha()
        self.finished = False

    @abstractmethod
    def update(self, delta_time):
        """
        Update the transition over time. This is where you set finished to true,
        signaling to the TransitionManager to go to the next scene.
        """
        pass

    @abstractmethod
    def render(self, canvas):
        """
        Draw the visual effect onto the canvas.
        """
        pass
