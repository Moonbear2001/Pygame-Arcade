import threading
from states.state import State
from states.title import Title
from visual_elems.LoadingCircle import LoadingCircle


class Loading(State):

    def __init__(self, game):
        super().__init__(game)
        self.name = "Loading"
        self.timer = threading.Timer(3, self.go_next)
        self.timer.start()
        self.loading_circle = LoadingCircle(self, self.game.canvas_width/2, self.game.canvas_height * 0.65, 200, 200, center=True)

    def update(self):
        super().update()
        self.loading_circle.update()

    def handle_event(self, event):
        super().handle_event(event)

    def render(self):
        self.game.canvas.fill(self.game.colors["white"])
        self.game.render_text(self.game.canvas, self.game.game_name, "roboto", self.game.colors["black"],
                              self.game.canvas_width/2, self.game.canvas_height/2, size=30, center=True)
        self.loading_circle.render()
        super().render()

    def go_next(self):
        Title(self.game).enter_state()

