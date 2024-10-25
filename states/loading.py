import threading
from states import State, Title
# from visual_elems.LoadingCircle import LoadingCircle

from managers import StateManager
from utilities import render_text


class Loading(State):
    """
    Simulates a loading state.
    Doesn't actually load anything.
    """

    def __init__(self):
        super().__init__()
        self.name = "Loading"
        # self.loading_circle = LoadingCircle(self, self.canvas_width/2, self.canvas_height * 0.65, 200, 200, center=True)
        self.timer = threading.Timer(1, self.go_next)
        self.timer.start()

    def update(self, delta_time):
        super().update(delta_time)
        # self.loading_circle.update()

    def handle_event(self, event):
        super().handle_event(event)

    def render(self):
        self.canvas.fill("white")
        render_text(self.canvas, "Pygame Arcade", "roboto", "black",
                              self.canvas_width/2, self.canvas_height/2, size=30, center=True)
        # self.loading_circle.render()
        return self.canvas

    def go_next(self):
        StateManager().set_state("title")

