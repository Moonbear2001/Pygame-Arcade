from states.state import State


class Settings(State):

    def __init__(self, game):
        super().__init__(game)

    def update(self, delta_time, action):
        self.game.reset_actions()

    def render(self):
        self.game.canvas.fill(self.game.colors["white"])
        self.game.render_text(self.game.canvas, "Settings", self.game.colors["black"], self.game.canvas_width / 2, self.game.canvas_height / 2)

