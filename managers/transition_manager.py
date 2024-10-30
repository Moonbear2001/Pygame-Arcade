import pygame

from transitions import FadeToBlack, FadeFromBlack
from .scene_manager import SceneManager


class TransitionManager:
    """
    Manages transitions between scenes amd their visual effects.
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
            "fade_from_black": FadeFromBlack,
        }

    def start_transition(self, transition_name, next_scene_name):
        """
        Starts a transition, given the name of that transition as a string and the name of the scene to transition to.
        """
        print("start transition")
        transition_class = self.transitions.get(transition_name)
        if transition_class:
            self.current_transition = transition_class(next_scene_name)

    def update(self, delta_time):
        """
        Updates the current transition and switches to the next scene if finished.
        """
        if self.current_transition:
            if self.current_transition.finished:
                SceneManager().set_scene(self.current_transition.next_scene_name)
                self.current_transition = None
            else:
                self.current_transition.update(delta_time)

    def render(self, canvas):
        """
        Render the current transition effect if active.
        """
        if self.current_transition:
            self.current_transition.render(canvas)
