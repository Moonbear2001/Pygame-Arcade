from states.state import State

import Game

class Settings(State):

    def __init__(self, game):
        super().__init__(game)

    def update(self, delta_time):
        super().update(delta_time)

    def handle_event(self, event):
        super().handle_event(event)

    def render(self):
        self.game.canvas.fill("white")
        self.game.render_text(self.game.canvas, "Settings", "roboto", "black", Game.canvas_width / 2, self.game.Game.canvas_height / 2)
        super().render()
