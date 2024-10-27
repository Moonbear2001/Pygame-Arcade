import pygame
from abc import ABC, abstractmethod  


class Transition(ABC):
    """
    A transition between two states. This is usually just some visual effect. If there is a transition taking place, the TransitionManager draws the visual effect on top of the current state.
    """
    def __init__(self, next_state_name):
        """
        Next state is the name of state to go to after the transition is finished.
        """
        super().__init__()
        self.next_state_name = next_state_name
        self.surface = pygame.Surface((1280, 720))
        self.finished = False

    @abstractmethod
    def update(self, delta_time):
        """
        Update the transition over time. This is where you set finished to true, signaling to the TransitionManager to go to the next state.
        """
        pass

    @abstractmethod
    def render(self, canvas):
        """
        Draw the visual effect onto the canvas.
        """
        pass
