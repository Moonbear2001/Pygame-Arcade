from .manager import Manager
from .scene_manager import SceneManager
from transitions import FadeToColor, FadeFromColor


class TransitionManager(Manager):
    """
    Manages transitions between scenes and their visual effects.
    """

    def _init(self):
        self.current_transition = None
        self.next_scene_name = ""
        self.transitions = {
            "fade_to_black": FadeToColor,
            "fade_from_black": FadeFromColor,
        }

    def start_transition(
        self, transition_out_name, next_scene_name, transition_in_name=None
    ):
        """
        Starts a transition out, given the name of that transition and the next scene to
        transition to.
        Optionally can provide a second transition that will be run after the next scene
        has been loaded.
        """
        self.next_scene_name = next_scene_name
        transition_out_class = self.transitions.get(transition_out_name)
        transition_in_class = (
            self.transitions.get(transition_in_name) if transition_in_name else None
        )
        self.current_transition = (
            transition_out_class() if transition_out_class else None
        )
        self.transition_in = transition_in_class() if transition_in_class else None

    def update(self, delta_time):
        """
        Updates the current transition and switches to the next scene if finished.
        """
        if self.current_transition:
            if not self.current_transition.finished:
                self.current_transition.update(delta_time)
            else:
                self._handle_transition_end()

    def _handle_transition_end(self):
        """
        Handles the logic when the current transition finishes.
        """
        SceneManager().set_scene(self.next_scene_name)
        self.next_scene_name = ""
        self.current_transition = self.transition_in
        self.transition_in = None

    def render(self, canvas):
        """
        Render the current transition effect if active.
        """
        if self.current_transition:
            self.current_transition.render(canvas)
