from states.state import State
from states.gameplay import Gameplay


class Title(State):

    def __init__(self, game):
        super().__init__(game)

    def update(self, delta_time, action):
        if self.game.actions["start"]:
            Gameplay(self.game).enter_state()
        self.game.reset_actions()

    def render(self):
        self.game.canvas.fill(self.game.colors["white"])
        self.game.render_text(self.game.canvas, "Title screen", self.game.colors["black"], self.game.canvas_width / 2, self.game.canvas_height / 2)

