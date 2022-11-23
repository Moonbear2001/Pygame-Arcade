from states.state import State


class Settings(State):

    def __init__(self, game):
        super().__init__(game)

    def update(self):
        super().update()

    def handle_event(self, event):
        super().handle_event(event)

    def render(self):
        self.game.canvas.fill(self.game.colors["white"])
        self.game.render_text(self.game.canvas, "Settings", "roboto", self.game.colors["black"], self.game.canvas_width / 2, self.game.canvas_height / 2)
        super().render()
