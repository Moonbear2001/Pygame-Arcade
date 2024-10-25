from states.state import State

from utilities import render_text


class Settings(State):

    def __init__(self, game):
        super().__init__(game)

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)

    def render(self):
        canvas.fill("white")
        render_text(self.game.canvas, "Settings", "roboto", "black", self.canvas_width / 2, self.canvas_height / 2)
        super().render()
