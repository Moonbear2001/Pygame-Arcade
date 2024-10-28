import threading
from states import State, Title
# from visual_elems.LoadingCircle import LoadingCircle

from managers import StateManager, TransitionManager
from utilities import render_text


class Loading(State):
    """
    Simulates a loading state.
    Doesn't actually load anything.
    """

    def __init__(self):
        super().__init__()
        self.name = "Loading"
        self.timer = threading.Timer(1, lambda: TransitionManager().start_transition("fade_to_black", "title"))
        self.timer.start()

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)

    def render(self):
        self.canvas.fill("white")
        render_text(self.canvas, "Pygame Arcade", "roboto", "black", size=30)
        return self.canvas
        