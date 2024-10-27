import pygame

from states.transitions import FadeToBlack, FadeFromBlack
# from states import FadeToBlack, FadeFromBlack
from .state_manager import StateManager

class TransitionManager:
    """
    Manages transitions between states amd their visual effects.
    Uses the singleton design pattern.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TransitionManager, cls).__new__(cls)
            cls._instance._init()
        return cls._instance
    
    def _init(self):
        self.current_transition = None
        self.transitions = {
            "fade_to_black": FadeToBlack,
            "fade_from_black": FadeFromBlack
        }

    def start_transition(self, transition_name, next_state_name):
        """
        Starts a transition, given the name of that transition as a string and the name of the state to transition to.
        """
        transition_class = self.transitions.get(transition_name)
        if transition_class:
            self.current_transition = transition_class(next_state_name)

    def update(self, delta_time):
        """
        Updates the current transition and switches to the next state if finished.
        """
        if self.current_transition:
            if self.current_transition.finished:
                StateManager().set_state(self.current_transition.next_state_name)
                self.current_transition = None

    def render(self, canvas):
        """
        Render the current transition effect if active.
        """
        if self.current_transition:
            self.current_transition.render(canvas)

