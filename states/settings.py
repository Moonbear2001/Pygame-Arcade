from states.state import State

from utilities import render_text


class Settings(State):
    """
    Settings menu.
    """

    def __init__(self):
        super().__init__()

    def update(self, delta_time):
        pass

    def handle_event(self, event):
        pass

    def render(self):
        self.canvas.fill("white")
        render_text(self.canvas, "Settings", "roboto", "black", self.canvas_width / 2, self.canvas_height / 2)
        return self.canvas